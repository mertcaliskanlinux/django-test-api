from django.urls import path
from test_app.views import Simple

urlpatterns = [
    path('',Simple.as_view(),name='simple'),
    path('<int:id>',Simple.as_view()),
]
