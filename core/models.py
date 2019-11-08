from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.urls import reverse
from PIL import Image

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(upload_to='', null=False,blank=False)
    slug = AutoSlugField(populate_from='title')
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #     ordering = ['-created_on']

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title
    
    @property
    def short_description(self):
        return self.text[:60]+'...'

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_posts')
    comment = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    news = models.ForeignKey(
        Post,
        verbose_name = 'Post',
        on_delete = models.CASCADE
    )
    
    def __str__(self):
        return 'Comment by {}'.format(self.author)