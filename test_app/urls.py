from django.urls import path
from test_app.views import SimleViewset

urlpatterns = [

    path('simple-generics',SimleViewset.as_view()),


]
