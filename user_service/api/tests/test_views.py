from collections import OrderedDict
import datetime

from rest_framework.test import APIClient
from django.test import TransactionTestCase

from ..models import ProfileResults, UserProfile
from django.contrib.auth.models import User


class SetUpClass(TransactionTestCase):
    reset_sequences = True
    current_saved_time = str(datetime.datetime.now().date())

    def setUp(self):
        self.client = APIClient()

        user = User(email="example@gmail.com", username="antonsav")
        user.set_password("1234567")
        user.save()
        user = User.objects.get(email='example@gmail.com')
        user_profile = UserProfile(user=user, first_name='Anton', last_name='Savytskyi')
        user_results = ProfileResults(user=user, two_by_two='00:00.23', three_by_three='00:59.23', four_by_four='02:12.45')
        user_results.save()
        user_profile.save()


class TestUserView(SetUpClass):

    def test_users_GET_valid(self):
        response = self.client.get('/api/users/1/')

        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data, {'username': 'antonsav', 'email': 'example@gmail.com',
                                          'userprofile': OrderedDict([('first_name', 'Anton'),
                                                                      ('last_name', 'Savytskyi'),
                                                                      ('signup_date', self.current_saved_time)]),
                                          'profileresults': OrderedDict([('two_by_two', '00:00.23'),
                                                                         ('three_by_three', '00:59.23'),
                                                                         ('four_by_four', '02:12.45')])})

    def test_users_POST_valid(self):
        response = self.client.post('/api/users/', {"username": "My_username", "email": "mymail@gmail.com",
                                                    "password": "12345678"}, format='json')
        user = User.objects.get(id=2)
        self.assertEquals(response.status_code, 201)
        self.assertEquals(user.email, "mymail@gmail.com")
        self.assertTrue(user.check_password("12345678"))

    # def test_users_POST_invalid(self):
    #     response = self.client.post('/api/users/', {"username": "My_username", "email": "mymail@gmail.com",
    #                                                 "password": "12345678"}, format='json')
    #     user = User.objects.get(id=2)
    #     self.assertEquals(response.status_code, 201)
    #     self.assertEquals(user.email, "mymail@gmail.com")
    #     self.assertTrue(user.check_password("12345678"))

    def test_users_DELETE(self):
        response = self.client.delete('/api/users/1/')
        user_exists = User.objects.filter(id=1).exists()
        self.assertEquals(response.status_code, 200)
        self.assertFalse(user_exists)


class TestUeserProfile(SetUpClass):

    def test_GET(self):
        response = self.client.get('/api/profile/1/')
        self.assertEquals(response.data, {'first_name': 'Anton', 'last_name': 'Savytskyi', 'signup_date': self.current_saved_time})

    def test_PUT(self):
        response = self.client.put('/api/profile/1/', {'first_name': 'Jack', 'last_name': 'Samurai'})
        profile = UserProfile.objects.get(id=1)
        self.assertEquals((profile.first_name, profile.last_name), ('Jack', 'Samurai'))
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data, 'saved')


class TestProfilResults(SetUpClass):

    def test_PUT(self):
        response = self.client.put('/api/profile/1/results/',  {'two_by_two': '00:13.23',
                                                                'three_by_three': '00:55.23',
                                                                'four_by_four': '22:12.45'})
        results = ProfileResults.objects.get(id=1)
        self.assertEquals(results.three_by_three, '00:55.23')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data, 'saved')

