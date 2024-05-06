from django.db import models

class blog(models.Model):
    title=models.CharField(max_length=200,blank=True,null=True)
    content=models.TextField(max_length=5000,blank=True,null=True)
    inside_content=models.TextField(max_length=10000,blank=True,null=True)
    created_on=models.DateTimeField(auto_now=False,auto_now_add=True)
    thumbnail=models.ImageField(upload_to='thumbnail/',blank=True,null=True)
    author=models.CharField(max_length=50,null=True)
    slug= models.SlugField(max_length=100,null=True)
    
    def __str__(self):
        return self.title
