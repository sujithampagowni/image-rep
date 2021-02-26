from django.shortcuts import render

from image_repo.permissions import IsOwner
from .models import MyImage
from .serializers import ImageSerializer
from django.http import Http404
from rest_framework.views import APIView
# from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status

# class ImageListView(generics.ListCreateAPIView):
#     permission_classes = [IsOwner]
#     queryset = MyImage.objects.all()
#     serializer_class = ImageListSerializer
    
#     def get_queryset(self):
#         user = self.request.user
#         return MyImage.objects.filter(owner=user)

# class ImageRetriveView(generics.RetrieveAPIView):
#     queryset = MyImage.objects.all()
#     serializer_class = ImageSerializer
#     permission_classes = [IsOwner]

class ImageListView(APIView):

	def get(self, request):
		title = self.request.query_params.get('title', None)
		if title:
			images = MyImage.objects.filter(title=title).order_by('-uploaded_at')
			if not images:
				raise Http404
		else:
			images = MyImage.objects.all().order_by('-uploaded_at')

		serializer = ImageSerializer(images, many=True)
		return Response(serializer.data)

	def post(self, request):
		serializer = ImageSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ImageDetailView(APIView):

    def get_object(self, pk):
        try:
            return MyImage.objects.get(pk=pk)
        except Exception as e:
            raise Http404

    def get(self, request, pk):
        image = self.get_object(pk)
        serializer = ImageSerializer(image)
        return Response(serializer.data)

    def delete(self, request, pk):
        image = self.get_object(pk)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

