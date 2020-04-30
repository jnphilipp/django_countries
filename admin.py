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

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from .models import Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['name', 'locale_name', 'code', 'phone_prefix']}),
    ]
    list_display = ('name', 'locale_name', 'code')
    search_fields = ('name', 'locale_name', 'code')
    ordering = ('code',)
