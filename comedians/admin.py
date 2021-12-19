from django.contrib import admin
from django.db import models
from .models import *

admin.site.register(Comedian)
admin.site.register(Company)
admin.site.register(Group)
admin.site.register(Tag)
admin.site.register(GroupTagGroup)
admin.site.register(ComedianTagGroup)