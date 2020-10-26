from rest_framework import status
from django.http import JsonResponse
from django.conf import settings
from datetime import datetime, timezone, timedelta
from rest_framework.decorators import api_view, authentication_classes, permission_classes 
from rest_framework.response import Response
from new_twitter.models import user_detail,userFollowing
from rest_framework.permissions import IsAuthenticated
from new_twitter.serializers import  user_detailSerializer, userFollowingSerializer

User = settings.AUTH_USER_MODEL

@api_view(['GET', 'POST'])
def user_tweet(request):
    
    if request.method == 'GET':
        user_detail = user_detail.objects.all()
        serializer = user_detailSerializer(user_detail, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = user_detailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def timeline(request):
    timeline=datetime.datetime.now()-datetime.timedelta(days=1)
    current_user = userFollowing.following
    current_user = current_user.user_id
    followed_people = userFollowing.objects.filter(follower=current_user).values('following')
    tweet = user_detail.objects.filter(user_id__in =  followed_people).filter(created__gt=timeline)
    serializer = user_detailSerializer(tweet, many= True)
    return Response(serializer.data)

@api_view(['GET'])
def following(request):
    current_user = userFollowing.following
    current_user = current_user.user_id
    following_people = userFollowing.objects.filter(follower=current_user).values('following')
    serializer = userFollowingSerializer(following_people, many= True)
    return Response(serializer.data)

@api_view(['GET'])
def follow(request):
    current_user = userFollowing.followers
    current_user = current_user.user_id
    follower_people = userFollowing.objects.filter(following=current_user).values('followers')
    serializer = userFollowingSerializer(follower_people, many= True)
    return Response(serializer.data)


