from django.db import models
from user_account.models import CustomUser
from django.urls import reverse
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True,blank=True)
    description = models.TextField(blank=True)
    is_enable = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse(self.name)

class Tag(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default='')
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.name

class Artical(models.Model):
    STATUS = (
        ('first','published'),
        ('second','draft')
    )
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True,blank=True)
    content = models.TextField()
    avatar = models.ImageField(upload_to='static/images/main')
    author = models.CharField(max_length=20,default='Admin')
    published_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100,choices=STATUS,default='second')

    def __str__(self):
        return self.title
    
class SaveArtical(models.Model):
    username = models.CharField(max_length=100,default='')
    artical = models.ForeignKey(Artical,on_delete=models.CASCADE)
    saved = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)

class Images(models.Model):
    artical = models.ForeignKey(Artical,on_delete=models.CASCADE)
    description = models.TextField(default='')
    avatar = models.ImageField(upload_to='static/images/information')
    created_time = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("artical",args=[self.id])

class Comment(models.Model):
    username = models.CharField(max_length=100,default='')
    artical = models.ForeignKey(Artical,on_delete=models.CASCADE)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

class AnswerComment(models.Model):
    username = models.CharField(max_length=100,default='')
    comment = models.ForeignKey(Comment,on_delete=models.CASCADE)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

class Subscriber(models.Model):
    email = models.EmailField()
    subscribed_date = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    username = models.CharField(max_length=100 , default='')
    page_name = models.CharField(max_length=100, default='')
    is_like = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)

class PageView(models.Model):
    ip = models.GenericIPAddressField(default=0)
    page_name = models.CharField(max_length=200)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.page_name