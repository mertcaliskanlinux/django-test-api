from django.contrib import admin
from test_app.models import TestModel,ModelX,ModelY

admin.site.register((TestModel,ModelX,ModelY))
