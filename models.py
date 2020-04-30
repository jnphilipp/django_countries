# -*- coding: utf-8 -*-
# Copyright (C) 2020 J. Nathanael Philipp (jnphilipp) <nathanael@philipp.land>
#
# This file is part of django_countries.
#
# django_countries is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# django_countries is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with django_countries. If not, see <http://www.gnu.org/licenses/>.

from django.db import models
from django.utils.translation import ugettext_lazy as _


class Country(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name=_('Updated at'))

    name = models.CharField(max_length=256, unique=True,
                            verbose_name=_('Name'))
    locale_name = models.CharField(max_length=256, unique=True,
                                   verbose_name=_('Locale name'))
    code = models.CharField(max_length=2, unique=True,
                            verbose_name=_('ISO code'))
    phone_prefix = models.CharField(max_length=5, unique=True,
                                    verbose_name=_('Phone prefix'))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('code',)
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')


class Language(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name=_('Created at'))
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name=_('Updated at'))

    name = models.CharField(max_length=256, unique=True,
                            verbose_name=_('Name'))
    code = models.CharField(max_length=3, unique=True,
                            verbose_name=_('ISO code'))
    countries = models.ManyToManyField(Country, blank=True,
                                       related_name='languages',
                                       verbose_name=_('Countries'))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = _('Language')
        verbose_name_plural = _('Languages')
