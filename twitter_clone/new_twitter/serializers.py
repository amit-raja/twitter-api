from rest_framework import serializers
from new_twitter.models import user_detail,userFollowing
from django.conf import settings

class user_detailSerializer(serializers.ModelSerializer):
    class Meta:
        model = user_detail
        fields = "__all__"

class userFollowingSerializer(serializers.ModelSerializer):

    class Meta:
        model = userFollowing
        fields = "__all__"

'''class FollowersSerializer(serializers.ModelSerializer):
    class Meta:
        model = userFollowing
        fields = ("id", "user_id")'''

