from django.contrib import admin
from .models import Post, Contractor, WorkInstance

# Register your models here.
admin.site.register(Post)
admin.site.register(Contractor)
admin.site.register(WorkInstance)