# from django.urls import include, path
# # from rest_framework import routers
# from tutorial.quickstart import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]


from django.conf.urls import url
# from django.contrib import admin
from .views import ImageListView, ImageDetailView

urlpatterns = [
    url(r'^$', ImageListView.as_view(), name='image-list'),
    url(r'^(?P<pk>\d+)/$', ImageDetailView.as_view(), name='image-detail'),
]