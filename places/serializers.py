from django.conf.urls import url, include
from places.models import Place, Feedback
from rest_framework import serializers


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('id', 'name', 'latitiude', 'longitude', 'description', 'thumbnail')


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('id', 'place', 'description', 'given_by', 'is_postive')