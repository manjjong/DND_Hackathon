from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from hackapp import views, views_challenge, views_challenge_user

urlpatterns = [
    path('user/', views.UserList.as_view()),
    path('user/register/', views.UserRegister.as_view()),
    path('user/login/', views.UserLogin.as_view()),
    path('user/detail/<str:pk>/', views.UserDetail.as_view()),
    path('follow/', views.FollowList.as_view()),
    path('follow/register/', views.FollowRegister.as_view()),
    path('follow/list/', views.FollowUser.as_view()),
    path('follow/check/', views.FollowCheck.as_view()),
    path('follow/detail/<str:user_id>&<str:target_id>/', views.FollowDetail.as_view()),
    path('challenge/', views_challenge.ChallengeList.as_view()),
    path('challenge/register/', views_challenge.ChallengeRegister.as_view()),
    path('challenge/detail/<int:pk>/', views_challenge.ChallengeDetail.as_view()),
    path('challenge/modify/<int:pk>/', views_challenge.ChallengeModify.as_view()),
    path('challengeuser/', views_challenge_user.Challenge_UserList.as_view()),
    path('challengeuser/register/', views_challenge_user.Challenge_UserRegister.as_view()),
    path('challengeuser/detail/<int:pk>/', views_challenge_user.Challenge_UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)