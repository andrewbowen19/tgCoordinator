from django.contrib import admin

# Register your models here.
# Need to add other coords & Hillary as admins
from .models import Question

admin.site.register(Question)






