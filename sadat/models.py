from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    topic_name = models.CharField( max_length = 264, unique = True)

    def __str__(self):
        return self.topic_name


class Webpage(models.Model):
    topic = models.ForeignKey('Topic' , on_delete=models.CASCADE)
    name = models.CharField( max_length = 264, unique = True)
    url = models.URLField(unique = True)
    item_status = models.CharField(max_length=264, default = "deposited")

    def __str__(self):
        return self.name


class AccessRecords(models.Model):
    name = models.ForeignKey('Webpage' , on_delete=models.CASCADE)
    date = models.DateField()
    

    def __str__(self):
        return str(self.date)

class User_Signup(models.Model):
    user_name = models.CharField(max_length = 264, unique = True)
    first_name = models.CharField( max_length = 264)
    last_name = models.CharField( max_length = 264)
    # user_password = models.PasswordField()
    
    def __str__(self):
        return self.user_name

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Additional Classes if we want to incl

    portfolio_site = models.URLField(blank = True)
    profile_pic = models.ImageField(upload_to = 'profile_pics',blank = True)

    def __str__(self):
        return self.user.username