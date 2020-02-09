from django.contrib import admin
from sadat.models import Topic, Webpage, AccessRecords,User_Signup,UserProfileInfo

# Register your models here.
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecords)
admin.site.register(User_Signup)
admin.site.register(UserProfileInfo)
