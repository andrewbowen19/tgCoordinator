from django.contrib import admin

# Register your models here.
# Need to add other coords & Hillary as admins
from .models import Question
from .models import Guide, Visitor



admin.site.register(Question)
admin.site.register(Guide)
admin.site.register(Visitor)




