from django.urls import path
from .views import UserView, ProfileView, ProfileResultsView

urlpatterns = [
    path('api/users/', UserView.as_view(), name='users-view'),
    path('api/users/<int:pk>/', UserView.as_view(), name='user-view'),
    path('api/profile/<int:pk>/', ProfileView.as_view(), name='profile-view'),
    path('api/profile/<int:pk>/results/', ProfileResultsView.as_view(), name='profile-result-view')
]
