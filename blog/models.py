from django.db import models
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager

class Post(models.Model):
    title           = models.CharField(max_length=160, null=False)
    content         = models.TextField(null=False, blank=True)
    slug            = models.SlugField(unique = True)
    tags            = TaggableManager(blank=True)
     
    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug':self.slug})
        
    def __str__(self):
        return self.title
