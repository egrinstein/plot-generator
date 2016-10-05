from __future__ import unicode_literals

from django.db import models

# Create your models here.


class TripleToWord(models.Model):
    id = models.IntegerField(primary_key=True)
    word1 = models.TextField(blank=False,null=False)
    word2 = models.TextField(blank=False,null=False)
    word3 = models.TextField(blank=False,null=False)
    next_word = models.TextField(blank=False,null=False)
    frequency = models.IntegerField(default=0)
    
    class Meta: 
        unique_together = ('word1', 'word2', 'word3','next_word')
        db_table = 'triple_to_word'
        managed = False
        
class StartTriple(models.Model):
    id = models.IntegerField(primary_key=True)
    word1 = models.TextField(blank=False,null=False)
    word2 = models.TextField(blank=False,null=False)
    word3 = models.TextField(blank=False,null=False)
    
    class Meta: 
        unique_together = ('word1', 'word2', 'word3')
        db_table = 'start_triple'
        managed = False
