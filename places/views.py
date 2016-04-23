from django.shortcuts import render
from places.models import Place, Feedback
from places.serializers import PlaceSerializer, FeedbackSerializer
from rest_framework import viewsets


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
