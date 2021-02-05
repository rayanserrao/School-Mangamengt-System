from django.db import models
from django.template.defaultfilters import slugify

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
    standard - models.ForeignKey(Standard,on_delete=models.CASCADE,related_name='subjects')
    image = models.ImageField(upload_to=save_subject_image, blank=True,verbose_name='subject image')
    desc = models.TextField(max_length=500,blank=True)

     def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug =  slugify(self.subject_id)
        super().save(*args,**kwargs)


