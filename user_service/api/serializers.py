from rest_framework import serializers
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
import re

from .models import UserProfile, ProfileResults


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'signup_date')


def validate_time_format(value):
    time_format_pattern = r"^[0-5][0-9]:[0-5][0-9].[0-9]{2}$"
    if not re.match(time_format_pattern, value):
        raise ValidationError("Invalid time format")


class ProfileResultsSerializer(serializers.ModelSerializer):
    two_by_two = serializers.CharField(validators=[validate_time_format])
    three_by_three = serializers.CharField(validators=[validate_time_format])
    four_by_four = serializers.CharField(validators=[validate_time_format])

    class Meta:
        model = ProfileResults
        fields = ('two_by_two', 'three_by_three', 'four_by_four')


class FullUserInfoSerializer(serializers.ModelSerializer):
    userprofile = UserProfileSerializer()
    profileresults = ProfileResultsSerializer()

    class Meta:
        model = User
        fields = ['username', 'email', 'userprofile', 'profileresults']
