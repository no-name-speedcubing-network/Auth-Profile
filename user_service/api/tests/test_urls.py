from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import ProfileView, ProfileResultsView, UserView
# from user_service.api.views import ProfileView, ProfileResultsView, UserView


class TestUrls(SimpleTestCase):

    def test_users_url(self):
        url = reverse('users-view')
        self.assertEquals(resolve(url).func.view_class, UserView)

    def test_user_url(self):
        url = reverse('user-view', args=['6'])
        self.assertEquals(resolve(url).func.view_class, UserView)

    def test_profile_url(self):
        url = reverse('profile-view', args=['6'])
        self.assertEquals(resolve(url).func.view_class, ProfileView)

    def test_profile_results_url(self):
        url = reverse('profile-result-view', args=['6'])
        self.assertEquals(resolve(url).func.view_class, ProfileResultsView)


