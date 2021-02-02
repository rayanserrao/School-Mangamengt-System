from django.db import models
from  django.contrib.auth.models import User
import os

def path_rename(instance,filename):
    upload_to = 'images/'
    ext = filename.split('.')[-1]

    # get file name
    if instance.user.username:

        # filename = 'User_Prof_Pic/{}.{}'.format(instance.user.username,ext)
        filename = f'user_profile_picture/ {instance.user.username}.{ext}'
    return os.path.join(upload_to,filename)

# Create your models here.
class User_profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    bio = models.CharField(max_length=100,blank=True)
    profile_pic = models.ImageField(upload_to =path_rename, verbose_name='prof_pic', blank=True)


    teacher = 'teacher'
    student = 'student'
    parent = 'parent'

    user_types = [
        (teacher,'teacher'),
        (student,'student'),
        (parent,'parent'),
    ]

    user_types= models.CharField(max_length=20,choices=user_types,default=student)

    def __str__(self):
        return self.user.username


