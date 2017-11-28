# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Member
from .models import Document
from .models import Ajax
from .models import Music

admin.site.register(Member)
admin.site.register(Document)
admin.site.register(Ajax)
admin.site.register(Music)