from django.conf.urls import url, include
from places.models import Place, Feedback
from rest_framework import serializers


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'name', 'latitiude', 'longitude', 'description', 'thumbnail')


class FeedbackSerializer(serializers.ModelSerializer):
	place_name = serializers.ReadOnlyField(source='place.name', read_only=True)
	thumbnail = serializers.ReadOnlyField(source='place.thumbnail', read_only=True)
	user = serializers.ReadOnlyField(source='given_by.user.first_name', read_only=True)
	picture = serializers.ReadOnlyField(source='given_by.profile_pic', read_only=True)

	class Meta:
		model = Feedback
		fields = ('id', 'place_name', 'description', 'user', 'is_postive', 'thumbnail', 'picture')