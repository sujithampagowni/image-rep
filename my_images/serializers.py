from rest_framework import serializers
from .models import MyImage
# from django.contrib.auth.models import User


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyImage
        fields = '__all__'


# class ImageListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = MyImage
#         fields = ['title', 'uploaded_at']
