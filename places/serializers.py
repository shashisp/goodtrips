from django.conf.urls import url, include
from places.models import Place, Feedback, WishList
from rest_framework import serializers
from rest_framework import exceptions

class PlaceSerializer(serializers.ModelSerializer):
	feedbacks = serializers.CharField(source='get_all_feedbacks', read_only=True)

	class Meta:
		model = Place
		fields = ('id', 'name', 'latitiude', 'longitude', 'description', 'thumbnail', 'feedbacks', 'extra_data')


class FeedbackSerializer(serializers.ModelSerializer):
	place_name = serializers.ReadOnlyField(source='place.name', read_only=True)
	thumbnail = serializers.ReadOnlyField(source='place.thumbnail', read_only=True)
	user = serializers.ReadOnlyField(source='given_by.user.first_name', read_only=True)
	user_picture = serializers.ReadOnlyField(source='given_by.profile_pic', read_only=True)

	class Meta:
		model = Feedback
		fields = ('id', 'place_name', 'description', 'user', 'is_postive', 'thumbnail', 'user_picture',
			      'place', 'given_by')

	def create(self, validated_data):
		return Feedback.objects.create(**validated_data)


class WishlistSerializer(serializers.ModelSerializer):

	class Meta:
		model = WishList
		fields = ('id', 'created_by', 'place')

	def update(self, validated_data):
		place = validated_data.get('place')[0]
		created_by = validated_data.get('created_by')
		if WishList.objects.filter(place=place, created_by=created_by).exists():
			return self.context['request'].user.userprofile.wishlists.remove(place)
		else:
		 return self.context['request'].user.userprofile.wishlists.add(place)