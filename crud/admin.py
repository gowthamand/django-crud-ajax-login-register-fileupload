from django.contrib import admin

# Register your models here.
from .models import Member
from .models import Document
from .models import Ajax

admin.site.register(Member)
admin.site.register(Document)
admin.site.register(Ajax)