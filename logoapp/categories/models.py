# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Categories(models.Model):

    name = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.name