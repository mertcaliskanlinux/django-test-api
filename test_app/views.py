
from test_app.models import TestModel
from test_app.serializers import SimpleSerializer
from rest_framework import generics



    
    
class SimpleGenerics(generics.ListCreateAPIView):
    
    queryset = TestModel.objects.all()
    serializer_class = SimpleSerializer

class SimpleUpdateGenerics(generics.UpdateAPIView):
    
    queryset = TestModel.objects.all()
    serializer_class = SimpleSerializer
    lookup_field = "id"
    
    