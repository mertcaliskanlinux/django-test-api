from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.views import APIView
from test_app.models import TestModel
from django.forms.models import model_to_dict
from test_app.serializers import SimpleSerializer


class Simple(APIView):
    
    def post(self,request):
        serializer = SimpleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
   
        return JsonResponse({
            'data':serializer.data
            })
        
    def get(self,request):
        content = TestModel.objects.all()
        return JsonResponse({
            'data':SimpleSerializer(content,many=True).data
        })
        
    def put(self,request,*args,**kwargs):
        model_id = kwargs.get('id',None)
        if not model_id:
            return JsonResponse({
                'error':'method /PUT/ NOW ALLOWED'
            })    
            
        try:
            instance = TestModel.objects.get(id=model_id)
        except:
                return JsonResponse({
                'error':'Objects DOES NOT EXİST'
            }) 
    
        serializer = SimpleSerializer(data=request.data,instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({'data':serializer.data})