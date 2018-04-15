from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Author(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=255)
    link = models.URLField(default='')
    views = models.IntegerField(default=0)
    file = models.FileField()


    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = Author.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)


#class list(models.Model):
#    user = models.ForeignKey(User)
