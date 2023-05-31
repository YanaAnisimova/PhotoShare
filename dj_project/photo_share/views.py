from django.forms import model_to_dict
from rest_framework import generics, viewsets
from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from photo_share.models import Photo, Tag
from photo_share.serializer import PhotoSerializer


# class PhotoAPIList(ListCreateAPIView):
#     queryset = Photo.objects.all()
#     serializer_class = PhotoSerializer
#
#
# class PhotoAPIUpdate(UpdateAPIView):
#     queryset = Photo.objects.all()
#     serializer_class = PhotoSerializer


class PhotoAPIView(APIView):

    # parser_classes = (MultiPartParser, FormParser)

    def get(self, request):
        photos = Photo.objects.all()
        return Response({'photos': PhotoSerializer(photos, many=True).data})

    def post(self, request):
        serializer = PhotoSerializer(
            data=request.data,
            # data={'descriptions': 'It is photo', 'author_id': 1, 'tags': [{'name': 'home'}, {'name': 'work'}]}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'photo': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            return Response({'error': 'Method RUP not allowed.'})
        try:
            instance = Photo.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exist.'})
        serializer = PhotoSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({'photo': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if not pk:
            return Response({'error': 'Method DELETE not allowed.'})
        try:
            photo = Photo.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exist.'})
        photo.delete()
        return Response({'photo': 'photo (' + str(pk) + ') is deleted.'})


# class PhotoAPIView(generics.ListAPIView):
#     queryset = Photo.objects.all()
#     serializer_class = PhotoSerializer
