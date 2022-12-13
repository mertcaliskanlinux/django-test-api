
from test_app.models import TestModel
from test_app.serializers import SimpleSerializer
from rest_framework import viewsets


    
    
class SimleViewset(viewsets.ModelViewSet):
    
    queryset = TestModel.objects.all()
    serializer_class = SimpleSerializer
    
    
    