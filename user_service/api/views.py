from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.db import transaction

from .serializers import UserProfileSerializer, ProfileResultsSerializer, UserSerializer, FullUserInfoSerializer
from .models import UserProfile, ProfileResults


class UserView(APIView):

    def get(self, request, pk):
        user = User.objects.get(id=pk)
        serializer = FullUserInfoSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        with transaction.atomic():
            serializer = UserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                user = User.objects.get(email=request.data.get('email'))
                user_profile = UserProfile(user=user)
                user_results = ProfileResults(user=user)
                user_results.save()
                user_profile.save()
                return Response('saved', status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # TODO write tests and change get to filter. Also in another places
        user = User.objects.filter(id=pk)
        user.delete()
        return Response('user deleted', status=status.HTTP_200_OK)


class ProfileView(APIView):

    def get(self, request, pk):
        profiles = UserProfile.objects.get(user=pk)
        serializer = UserProfileSerializer(profiles, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):

        profile = UserProfile.objects.get(user=pk)
        serializer = UserProfileSerializer(instance=profile, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response('saved', status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileResultsView(APIView):

    def put(self, request, pk):
        results = ProfileResults.objects.get(user=pk)
        serializer = ProfileResultsSerializer(instance=results, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('saved', status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

