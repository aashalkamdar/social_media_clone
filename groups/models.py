from django.db import models
from django.utils.text import slugify
import misaka
from django.urls import reverse
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()

from django import template
register = template.Library()
#this is how we can use custom template tags



class Group(models.Model):
    name = models.CharField(max_length=255,unique = True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    description = models.TextField(blank=True,default='')
    description_html = models.TextField(editable=False,default='',blank=True)
    members = models.ManyToManyField(User,through='GroupMember')

    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        self.description_html = misaka.html(self.description)
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('groups:single',kwargs={'slug':self.slug})

    class Meta:
        ordering = ['name']

class GroupMember(models.Model):
    group = models.ForeignKey(Group,related_name='memberships',on_delete='CASCADE')
    #group member is related to group class using related_name
    user = models.ForeignKey(User,related_name='user_groups',on_delete='CASCADE')
    #current user whose logged in whose part of groups so we wanna link group member class to both user and groups

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group','user')
