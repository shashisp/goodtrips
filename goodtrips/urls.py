from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers, serializers, viewsets
from places.views import PlaceViewSet, FeedbackViewSet, WishListViewSet

router = routers.DefaultRouter()
router.register(r'places', PlaceViewSet)
router.register(r'feedbacks', FeedbackViewSet)
router.register(r'wishlist', WishListViewSet)


urlpatterns = [
    # Examples:
    # url(r'^$', 'goodtrips.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^insta/', 'places.views.instagram_photos'),
	url(r'^dashboard/', 'places.views.dashboard'),
	url(r'^wishlist/', 'places.views.wishlist'),
	url(r'^stats/places/(?P<pk>\d+)/$', 'places.views.stats'),
	url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/v1/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/', include(router.urls)),
]
