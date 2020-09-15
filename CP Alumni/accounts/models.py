from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
    user_name = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    cohort = models.CharField(max_length=200)
    business_name =models.CharField(max_length=200)
    street_address =models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=6)
    profile_image = models.CharField(max_length=1000)



    def __str__(self):
        return f"id={self.id}, user_name={self.user_name}, first_name={self.first_name}, last_name={self.last_name}, password={self.password}, email={self.email}, cohort={self.cohort}, business_name={self.business_name}, street_address={self.street_address}, city={self.city}, state={self.state}, zipcode={self.zipcode}, profile_image={self.profile_image}"


