from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    image=models.ImageField(upload_to='profile_pics',blank=True,null=True)
    bio=models.TextField(blank=True,null=True)
    phone_no=models.CharField(max_length=20,blank=True,null=True)
    facebook=models.CharField(max_length=130)
    instagram=models.CharField(max_length=130)
    linkdein=models.CharField(max_length=130)

    def __str__(self):
        return self.user
    

class BlogPost(models.Model):
    title=models.CharField(max_length=200)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    slug=models.CharField(max_length=130)
    image=models.ImageField(upload_to='profile_pics',blank=True,null=True)
    datetime=models.DateTimeField(auto_now_add=True)
    likes=models.IntegerField(default=0)

    def __str__(self):
        return str(self.title)
    
class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    content=models.TextField()
    blog=models.ForeignKey(BlogPost,on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.SET_NULL,blank=True,null=True)
    datetime=models.DateTimeField(default=now)
    likes=models.IntegerField(default=0)

    def __str__(self):
        return str(self.user.username)+"Comments: "+self.content
