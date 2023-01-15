from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
admin.site.register(Member)
admin.site.register(Document)
admin.site.register(Ajax)
admin.site.register(CsvUpload)