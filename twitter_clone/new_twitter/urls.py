from django.urls import path
from new_twitter.views import (
   user_tweet,
   timeline,
   following,
   follow,
) 

urlpatterns = [
   path('user_info', user_tweet),
   path('user_timeline', timeline),
   path('user_following', following),
   path('user_follow', follow),
  # path('user_info', user_tweet),

    ]