from django.urls import path
from test_app.views import SimpleGenerics,SimpleUpdateGenerics

urlpatterns = [

    path('simple-generics',SimpleGenerics.as_view()),
    path('simple-generics/<int:id>',SimpleUpdateGenerics.as_view()),


]
