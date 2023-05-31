import io
from collections import OrderedDict

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.utils.serializer_helpers import ReturnDict

from photo_share.models import Photo, Tag


# class TagSerializer(serializers.Serializer):
#     # id = serializers.IntegerField()
#     name = serializers.CharField(max_length=50)
#
# class PhotoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Photo
#         fields = '__all__'

class PhotoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    descriptions = serializers.CharField(default='')
    author_id = serializers.IntegerField()
    image_url = serializers.ImageField()
    average_rating = serializers.FloatField(read_only=True)
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), many=True
    )
    # tags = TagSerializer(many=True)
    # tags = serializers.SlugRelatedField(
    #     queryset=Tag.objects.all(),
    #     many=True,
    #     slug_field='name'
    # )

    def create(self, validated_data):
        tags: list[Tag] = validated_data.pop('tags', [])
        photo_new = Photo.objects.create(** validated_data)
        photo_new.tags.set(tags)
        return photo_new

    def update(self, instance, validated_data):
        tags: list[Tag] = validated_data.pop('tags', [])
        instance.tags.set(tags)
        fields = ['descriptions', 'author_id', 'image_url']
        try:
            for field in fields:
                setattr(instance, field, validated_data[field])
        except KeyError: # validated_data may not contain all fields during HTTP PATCH
            pass
        instance.save()

        # instance.descriptions = validated_data.get('descriptions', instance.descriptions)
        # instance.author_id = validated_data.get('author_id', instance.author_id)
        # instance.image_url = validated_data.get('image_url', instance.image_url)
        return instance







# class WomenModel:
#     def __init__(self, title, cont):
#         self.title = title
#         self.cont = cont

# class WomenSelial(serializers.Serializer):
#     title = serializers.CharField(max_length=255)
#     cont = serializers.CharField()


# def encode():
#     model: WomenModel = WomenModel('Aa', 'AAAAAA')
#     model_sr: WomenSelial = WomenSelial(model)
#     model_sr_data: ReturnDict = model_sr.data
#     json: bytes = JSONRenderer().render(model_sr_data)


# def decode():
#     stream: io.BytesIO = io.BytesIO(b'{"title":"Aa","cont":"AAAAAA"}')
#     data: dict = JSONParser().parse(stream)
#     serial: WomenSelial = WomenSelial(data=data)
#     serial.is_valid()
#     val_data: OrderedDict = serial.validated_data


# class PhotoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Photo
#         fields = '__all__'

    # class Meta:
    #     # Each room only has one event per day.
    #     validators = [
    #         UniqueTogetherValidator(
    #             queryset=Event.objects.all(),
    #             fields=['room_number', 'date']
    #         )
    #     ]
