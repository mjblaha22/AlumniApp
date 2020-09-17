from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Users, Events, Messages, Businesses, Locations, Emails, Responses, User_Business
from .serializers import UsersSerializer, EventsSerializer, MessagesSerializer, BusinessesSerializer, LocationsSerializer, EmailsSerializer, ResponsesSerializer, User_BusinessSerializer
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
# from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
# from .serializers import UserSerializerWithToken


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
# Create your views here.
# EXTRA TEST
# class SignUpView(viewsets.ModelViewSet):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'registration/signup.html'
# remake stuff
class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

class EventsViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

class MessagesViewSet(viewsets.ModelViewSet):
    queryset = Messages.objects.all()
    serializer_class = MessagesSerializer

class BusinessesViewSet(viewsets.ModelViewSet):
    queryset = Businesses.objects.all()
    serializer_class = BusinessesSerializer

class LocationsViewSet(viewsets.ModelViewSet):
    queryset = Locations.objects.all()
    serializer_class = LocationsSerializer

class EmailsViewSet(viewsets.ModelViewSet):
    queryset = Emails.objects.all()
    serializer_class = EmailsSerializer

class ResponsesViewSet(viewsets.ModelViewSet):
    queryset = Responses.objects.all()
    serializer_class = ResponsesSerializer

class User_BusinessViewSet(viewsets.ModelViewSet):
    queryset = User_Business.objects.all()
    serializer_class = User_BusinessSerializer

