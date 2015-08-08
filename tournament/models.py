from django.db import models


class Tournament(models.Model):
    """
    my doc string
    """
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Participant(models.Model):
    """
    my doc string
    """
    name = models.CharField(max_length=200)
    tournament = models.ForeignKey(Tournament)

    def __unicode__(self):
        return u"{name} {tournament}".format(
                                        name=self.name,
                                        team=self.tournament.name
                                        )
