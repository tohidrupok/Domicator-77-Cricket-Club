from django.db import models

class Home(models.Model):
    slide_video = models.FileField(upload_to='Home/Video/')
    content = models.CharField(max_length=1000, blank=True, null=True)
    content1 = models.CharField(max_length=1000, blank=True, null=True)
    content3 = models.CharField(max_length=1000, blank=True, null=True)
    image1 = models.ImageField(upload_to='Home/images', blank=True, null=True)
    image2 = models.ImageField(upload_to='Home/images', blank=True, null=True)
    image3 = models.ImageField(upload_to='Home/images', blank=True, null=True)
    image4 = models.ImageField(upload_to='Home/images', blank=True, null=True)
    about_img = models.ImageField(upload_to='Home/images', blank=True, null=True)

class Player(models.Model):
       
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)     
    date_of_birth = models.DateField()
    description = models.TextField()
    age = models.IntegerField()
    place_of_birth = models.CharField(max_length=100)
    nickname = models.CharField(max_length=50, blank=True, null=True)
    jersey_name = models.CharField(max_length=50)
    jersey_number = models.CharField(max_length=50)
    height_cm = models.IntegerField()
    batting_style = models.CharField(max_length=20)
    bowling_style = models.CharField(max_length=100)
    role = models.CharField(max_length=50)
    relationship_status = models.CharField(max_length=50)
    image = models.ImageField(upload_to='leader_images/')
    facebook = models.CharField(max_length=200)  
    linkedin = models.CharField(max_length=200, blank=True, null=True)  
    email = models.EmailField()
    blood = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return self.name




