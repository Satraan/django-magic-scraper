#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.db import models


class Merchant(models.Model):

    title = models.CharField(default="Title", max_length=200)
    website = models.CharField(default="Website", max_length=200)

    def _str_(self):
        return self.title
