from django.db import models


class Gig(models.Model):
    when = models.DateTimeField()
    where = models.CharField(max_length=200)
    description = models.TextField()
    more = models.URLField('More info URL', blank=True)

    def __unicode__(self):
        return self.where
    