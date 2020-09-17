from django.urls import path, include
from rest_framework import viewsets
from .views import SignUpView, UsersViewSet, EventsViewSet, UsersViewSet, LocationsViewSet, BusinessesViewSet, EmailsViewSet, MessagesViewSet, ResponsesViewSet, User_BusinessViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('user/', UsersViewSet, name='user'),
    path('emails', EmailsViewSet, name='emails'),
    path('events', EventsViewSet, name='events'),
    path('locations', LocationsViewSet, name='locations'),
    path('businesses', BusinessesViewSet, name='businesses'),
    path('messages', MessagesViewSet, name='messages'),
    path('responses', ResponsesViewSet, name='responses'),
    path('userbusiness', User_BusinessViewSet, name='userbusiness'),

]
# router = DefaultRouter()
# router.register(r'signup', SignUpView.as_view(template_name='home.html'), basename='signup')
# router.register(r'user', UsersViewSet, basename='user')
# router.register(r'emails', EmailsViewSet, basename='emails')
# router.register(r'events', EventsViewSet, basename='events')
# router.register(r'locations', LocationsViewSet, basename='locations')
# router.register(r'businesses', BusinessesViewSet, basename='businesses')
# router.register(r'messages', MessagesViewSet, basename='messages')
# router.register(r'responses', ResponsesViewSet, basename='responses')
# router.register(r'userbusiness', User_BusinessViewSet, basename='userbusiness')
# urlpatterns = router.urls
