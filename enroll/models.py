
from email.policy import default
from turtle import title
from django.db import models
from django.urls import reverse

# Create your models here.
class TblTeam(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    designation = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    profile_pic = models.FileField(upload_to= 'images/',null=True,blank=True)
    fblink = models.CharField(max_length=100,default="")
    inlink = models.CharField(max_length=100,default="")
    twlink = models.CharField(max_length=100,default="")
    linlink = models.CharField(max_length=100,default="")

    def __str__(self):
        return "%s" %(self.name)

class Tblslider(models.Model):
    slide_title = models.CharField(max_length=100,default="enter title")
    slide_description = models.TextField(max_length=200,default="enter description")
    slider_image = models.FileField(upload_to= 'slid_imgs/',null=True,blank=True)

    def __str__(self):
        return "%s" %(self.slide_title)

class Tblclient(models.Model):
    c_name = models.CharField(max_length=100,default="enter client name")
    client_img = models.FileField(upload_to= 'clients/')
    
    def __str__(self):
        return "%s" %(self.c_name)

class Tblrecentwork(models.Model):
    title = models.CharField(max_length=100,help_text="enter title")
    portfol_img = models.FileField(upload_to= 'portfolio/')
    navigatelink = models.CharField(max_length=100,help_text="enter product navigate link")
    description = models.TextField(max_length=100,help_text="enter product description")
    category = models.CharField(max_length=100,default="enter caegory")

    def __str__(self):
        return "%s" %(self.title)    

class Tblcontact(models.Model):
    email = models.EmailField(max_length=254,help_text="Enter company emal")
    mobile = models.CharField(max_length=20,unique=True,help_text="enter mobile number")

    def __str__(self):
        return "%s %s" %(self.email, self.mobile)    


class Tbltestimonial(models.Model):
    title = models.CharField(max_length=100,help_text="enter testimonial title here")
    designation = models.CharField(max_length=100,help_text="enter designation here")
    description = models.TextField(max_length=100,help_text="enter description here")
    testi_img = models.FileField(upload_to= 'testimonialimages/')

    def __str__(self):
        return "%s" %(self.title)

class Tblenquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    description = models.TextField(max_length=200)

    def __str__(self):
        return "%s" %(self.name)

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True)
    class Meta:
        ordering=('-name',)

    def __str__(self):
        return "%s" %(self.name)   

    def get_absolute_url(self):
        return reverse('enroll:story_category',args=[self.slug])        

class Story(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    portfol_img = models.FileField(upload_to= 'portfolio/',default="hh")
    navigatelink = models.CharField(max_length=100,help_text="enter product navigate link",default="hello")
    description = models.TextField(max_length=100,help_text="enter product description",default="hello")
    publish = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering=('publish',)

    def __str__(self):
        return "%s" %(self.title)    