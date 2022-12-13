from rest_framework import serializers
from test_app.models import TestModel


class SimpleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = TestModel
        fields = '__all__'
    
    
    def create(self, validated_data):
        return TestModel.objects.create(**validated_data)
        
            
    def update(self, instance, validated_data):
        TestModel.objects.filter(id=instance.id).update(**validated_data)
        return TestModel.objects.get(id=instance.id)