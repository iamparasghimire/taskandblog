from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Timestamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True

class Task(Timestamp):

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

  

    def __str__(self):
        return self.title

class Blog(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userblog")
    image = models.ImageField(upload_to='static/profile/', null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=100)
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        
        while Blog.objects.filter(slug=self.slug).exclude(id=self.id).exists():
            self.slug = f"{self.slug}-{self.id}"
        
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name


class Comment(Timestamp):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE,related_name='comments') 
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"Comment by {self.author} on {self.blog.name}. "
    
class Userprofile(Timestamp):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="profile")
    image = models.ImageField(upload_to='image/',null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)


    def __str__(self):
        return self.user.username

    
    



    