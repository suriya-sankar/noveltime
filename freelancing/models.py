from django.db import models
from django.conf import settings

class story(models.Model):
   
    story_title=models.CharField(max_length=30,blank=False)
    story_descrtiption=models.TextField()
    story_title_pic=models.ImageField()
    upload_time=models.DateTimeField(auto_now_add=True)

    category=models.CharField(max_length=20 ,blank=True)


    def __str__(self):
        return self.story_title

 
class chappter(models.Model):
    story_name=models.CharField(max_length=30,blank=False)
    chapter_name=models.CharField(max_length=30,blank=False)
    author_name=models.CharField(max_length=30,default='not mentioned',blank=True)
    chapter_description=models.CharField(max_length=500,default='chapter description not mentioned')
    chapter_story=models.FileField()
    chapter_image=models.ImageField()
    chapter_number=models.CharField(max_length=5)
    chapter_time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.chapter_name          
class comments(models.Model):
    story_name=models.CharField(max_length=30,blank=False)
    chapter_name=models.CharField(max_length=40,blank=False)
    chapter_number=models.CharField(max_length=5)
    commenter_name=models.CharField(max_length=20,blank=False)
    comments=models.TextField()
    comment_time=models.DateTimeField(auto_now_add=True)        
    def __str__(self):
        return self.story_name