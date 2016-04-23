from django.shortcuts import render
from places.models import Place, Feedback, WishList
from places.serializers import PlaceSerializer, FeedbackSerializer, WishlistSerializer
from rest_framework import viewsets


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class WishListViewSet(viewsets.ModelViewSet):
	queryset = WishList.objects.none()
	serializer_class = WishlistSerializer

	def get_queryset(self):
		return WishList.objects.filter(created_by=self.request.user.userprofile)
