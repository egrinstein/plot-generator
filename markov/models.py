from __future__ import unicode_literals

from django.db import models

# Create your models here.


class TripleToWord(models.Model):
    word1 = models.TextField(blank=False,null=False)
    word2 = models.TextField(blank=False,null=False)
    word3 = models.TextField(blank=False,null=False)
    next_word = models.TextField(blank=False,null=False)
    frequency = models.IntegerField(default=0)

class StartTriple(models.Model):
    word1 = models.TextField(blank=False,null=False)
    word2 = models.TextField(blank=False,null=False)
    word3 = models.TextField(blank=False,null=False)

