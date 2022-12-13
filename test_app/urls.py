from django.urls import path
from test_app.views import SimleViewset

urlpatterns = [

    path('',SimleViewset.as_view()),


]
