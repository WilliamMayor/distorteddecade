from django.db import models


class Intro(models.Model):
    name = models.CharField(max_length=200, help_text='If the name is "Intro" then it will be used on the homepage')
    intro = models.TextField(help_text='The text to display on the homepage')

    def __unicode__(self):
        return self.name

class Gig(models.Model):
    when = models.DateTimeField()
    where = models.CharField(max_length=200)
    description = models.TextField()
    more = models.URLField('More info URL', blank=True)

    def __unicode__(self):
        return self.where
    