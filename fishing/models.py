from django.shortcuts import reverse, Http404
from django.db import models
from django.contrib.auth.models import User

from django.contrib.postgres.fields import JSONField
import hashlib

from django.utils import timezone 
from django.template.defaultfilters import slugify


from django.conf import settings





def arabic_slugify(str):
    str = str.replace(" ", "-")
    str = str.replace(" ' ", "-")
    str = str.replace('"', '-')
    str = str.replace(" ّ ", "-")
    str = str.replace(".", "")
    str = str.replace("،", "-")
    str = str.replace(",", "-")
    str = str.replace("(", "-")
    str = str.replace(")", "")
    str = str.replace("؟", "")
    return str


class author(models.Model):
    name = models.CharField(max_length =1000)
   
    profile_picture = models.ImageField(blank = True, upload_to = 'Avatar', default= 'Avatar/deafult-profile-image.png')
    
    def __str__(self):
        return self.name

    def snippet(self):
        return '%s %s ' % (self.name[:4])


class Pokes(models.Model):
    
    avatar = models.ForeignKey(author, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=9500, unique_for_date='publish', allow_unicode=True)
    poke_avatar = models.ImageField(blank = True, upload_to = 'Avatar_pokes')
    poke_user = models.CharField(max_length =1000)
    poke_date = models.CharField(max_length =9000)
    poke_avatar1 = models.ImageField(blank = True, upload_to = 'Avatar_pokes')
    poke_user1 = models.CharField(max_length =1000)
    poke_date1 = models.CharField(max_length =9000)
    poke_avatar2 = models.ImageField(blank = True, upload_to = 'Avatar_pokes')
    poke_user2 = models.CharField(max_length =1000)
    poke_date2 = models.CharField(max_length =9000)
    poke_avatar3 = models.ImageField(blank = True, upload_to = 'Avatar_pokes')
    poke_user3 = models.CharField(max_length =1000)
    poke_date3 = models.CharField(max_length =9000)
    poke_add_image = models.ImageField(blank = True, upload_to = 'Avatar_pokes')
    poke_add_me = models.CharField(max_length =1000)
    poke_vectim_link = models.URLField(blank=True, null=True, max_length = 128)

    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
  
    publish = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.avatar.name

    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
    
        if not self.slug:
            self.slug = slugify(self.title)
            if not self.slug:
                self.slug = arabic_slugify(self.title)

        super(Pokes, self).save(*args, **kwargs)
# Create your models here.
   


class articles(models.Model):
    poke = models.ForeignKey(Pokes, on_delete = models.CASCADE)
    title = models.CharField('العنوان', max_length=9500, null=True, blank = True)
    slug = models.SlugField(max_length=9500, unique_for_date='publish', allow_unicode=True)
    image = models.ImageField('صورة مناسبة', upload_to = 'Images', null=True, blank = True)
   

    posted_on = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True, auto_now_add=False)
  
    publish = models.DateTimeField(default=timezone.now) 


   
    
    
    
    def __str__(self):
        return self.slug

    def save(self, *args, **kwargs):
    
        if not self.slug:
            self.slug = slugify(self.title)
            if not self.slug:
                self.slug = arabic_slugify(self.title)

        super(articles, self).save(*args, **kwargs)

   

    

    


    def get_absolute_url(self):
        return reverse('fishing:show_article', kwargs={'id':self.id, 'slug': self.slug})
    

   
