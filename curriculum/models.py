from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import os
from django.urls import reverse

# Create your models here.

class Standard(models.Model):
    name= models.CharField(max_length=40, unique=True)
    slug = models.SlugField(null =True,blank=True)  # name of teh chatper using we will go to url path
    desc=  models.TextField(max_length=500, blank=True)

    def __str__(self):

        return self.name

    def save(self,*args,**kwargs):
        self.slug =  slugify(self.name)
        super().save(*args,**kwargs)

def save_subject_image(instance,filename):
    upload_to = 'images/'
    ext = filename.split('.')[-1]

    # get file name
    if instance.subject_id:

        # filename = 'User_Prof_Pic/{}.{}'.format(instance.user.username,ext)
        filename = f'Subject_pictures/ {instance.subject_id}.{ext}'
    return os.path.join(upload_to,filename)

class Subject(models.Model):
    subject_id = models.CharField(max_length=30,unique=True)
    name = models.CharField(max_length=30)
    slug = models.SlugField(null=True,blank=True)
    standard = models.ForeignKey(Standard,on_delete=models.CASCADE,related_name='subjects')
    image = models.ImageField(upload_to=save_subject_image, blank=True,verbose_name='subject image')
    desc = models.TextField(max_length=500,blank=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug =  slugify(self.subject_id)
        super().save(*args,**kwargs)


def save_lesson_files(instance,filename):
    upload_to = 'images/'
    ext = filename.split('.')[-1]

    # get file name
    if instance.lesson_id:

        # filename = 'User_Prof_Pic/{}.{}'.format(instance.user.username,ext)
        filename = f'Lesson_files/{instance.lesson_id}/{instance.lesson_id}.{ext}'
        if os.path.exists(filename):
            new_name= str(instance.lesson_id)+ str(1)
            filename = f'Lesson_files/{instance.lesson_id}/{new_name}.{ext}'

    return os.path.join(upload_to,filename)

class Lessons(models.Model):
    lesson_id = models.CharField(max_length=100,unique=True)
    standard = models.ForeignKey(Standard,on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE, related_name='lessons')
    name = models.CharField(max_length=200)
    position =  models.PositiveSmallIntegerField(verbose_name='chapter_no')
    slug = models.SlugField(null=True,blank=True)
    video = models.FileField(upload_to=save_lesson_files,verbose_name='video',blank=True,null=True)
    ppt = models.FileField(upload_to=save_lesson_files,verbose_name='Presentaion',blank=True,null=True)
    notes = models.FileField(upload_to=save_lesson_files,verbose_name='Notes',blank=True,null=True)


    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug =  slugify(self.name)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('lessondetail',kwargs={'slug':self.subject.slug,'standard':self.standard.slug})


# class Comment(models.Model):
#     lesson_name = models.ForeignKey(Lessons,null=True,on_delete=models.CASCADE,related_name='comments')
#     comm_name = models.CharField(max_length=100,blank=True)
#     # reply = models.ForeignKey(Comment,null=True,blank=True,on_delete=models.CASCADE,related_name='replies')
#     author = models.ForeignKey(User,on_delete=models.CASCADE)
#     body = models.TextField(max_length=500)
#     date_added = models.DateTimeField(auto_now_add=True)

#     def save(self,*args,**kwargs):
#         self.comm_name = slugify('comment by -'+ str(self.author) + "on" + str(self.date_added))
#         super().save(*args,**kwargs)

#     def __str__(self):
#         return self.comm_name

#     class Meta:
#         ordering = ['-date_added']


# class Reply(models.Model):
#     comment_name = models.ForeignKey(Comment.on_delete=models.CASCADE,related_name='replies')
#     reply_body = models.TextField(max_length=100)
#     author = models.ForeignKey(User,on_delete=models.CASCADE)
#     date_added = models.DateTimeField(auto_now_add=True)
#     def __str__(self):
#         return "reply to" + str(self.comment_name.comm_name)













