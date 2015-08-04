from django.db import models

# Create your models here.

class Team(models.Model):

    """docstring for Team"""

    name = models.CharField(max_length=200)
    coach = models.ForeignKey('Coach', null=True, blank=True)
        
    def __unicode__(self):
        return self.name

class Players(models.Model):

    """docstring for Players"""

    name = models.CharField(max_length=200)
    team = models.ForeignKey(Team)
    
    def __unicode__(self):
        return u"{name} {team}".format(name=self.name, team=self.team.name)


class Coach(models.Model):

    """docstring for Couch"""
    class Meta:
        verbose_name_plural = "Coaches"

    name = models.CharField(max_length=200)


    def __unicode__(self):
        return self.name




    
        
        