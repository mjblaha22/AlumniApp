from django.urls import path, include
from rest_framework import viewsets
from .views import SignUpView, UsersViewSet, EventsViewSet, UsersViewSet, LocationsViewSet, BusinessesViewSet, EmailsViewSet, MessagesViewSet, ResponsesViewSet, User_BusinessViewSet
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('user/', UsersViewSet.as_view({'get': 'list'}), name='user'),
    path('emails/', EmailsViewSet.as_view({'get': 'list'}), name='emails'),
    path('events/', EventsViewSet.as_view({'get': 'list'}), name='events'),
    path('locations/', LocationsViewSet.as_view({'get': 'list'}), name='locations'),
    path('businesses/', BusinessesViewSet.as_view({'get': 'list'}), name='businesses'),
    path('messages/', MessagesViewSet.as_view({'get': 'list'}), name='messages'),
    path('responses/', ResponsesViewSet.as_view({'get': 'list'}), name='responses'),
    path('userbusiness/', User_BusinessViewSet.as_view({'get': 'list'}), name='userbusiness'),

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
