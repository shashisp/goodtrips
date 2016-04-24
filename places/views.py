from django.shortcuts import render
from places.models import Place, Feedback, WishList
from places.serializers import PlaceSerializer, FeedbackSerializer, WishlistSerializer
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from utils import querytext_index


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


@api_view(['GET'])
def instagram_photos(request):
	place_id = request.GET['place_id']
	place = Place.objects.get(id=place_id)
	lat = str(place.latitiude)
	lng = str(place.longitude)
	access_token = '145499438.1677ed0.f96d57af717a4f19bfb2705506ef5efe'
	url = 'https://api.instagram.com/v1/locations/search?lat='+lat+'&lng='+lng+'&access_token='+access_token
	res = requests.get(url)
	location_id = res.json()['data'][0]['id']
	final_url = 'https://api.instagram.com/v1/locations/'+location_id+'/media/recent?access_token='+access_token
	result = requests.get(final_url)
	return Response(result.json())

def dashboard(request):
	return render(request, 'dashboard.html')

def wishlist(request):
	wishlists = WishList.objects.filter(created_by=request.user.userprofile)
	context = {
		'wishlists': wishlists
	}
	return render(request, 'wishlist.html', context)

def stats(request, pk):
	place = Place.objects.get(pk=pk)
	wants_to_visit = WishList.objects.filter(place=place).count()
	visted = Feedback.objects.filter(place=place).count()
	feedbacks = Feedback.objects.filter(place=place).values('created_at')
	context = {
	  'wants_to_visit': wants_to_visit,
	  'visted': visted,
	  'feedbacks': feedbacks
	}
	return render(request, 'stats.html', context)

