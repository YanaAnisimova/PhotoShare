from collections import OrderedDict

from rest_framework import serializers

from posts.models import Photo, Tag, PhotoRating


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']
        extra_kwargs = {
            'name': {'validators': []},  # exclude UniqueValidator
        }


class PhotoSerializer(serializers.HyperlinkedModelSerializer):
    """Handling GET, POST, PATCH, DELETE HTTP methods.

    The 'tag' in the request using form-data must be sent in the form 'tags[0]name'.

    """
    tags = TagSerializer(many=True,
                         required=False,
                         # allow_null=True
                         )
    # owner = serializers.ReadOnlyField(source='author.username')
    # author = serializers.HiddenField(default=serializers.CurrentUserDefault()) # for not Hyperlinked
    author = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        read_only=True,
    )  # for Hyperlinked need to user read_only=True or queryset.

    class Meta:
        model = Photo
        fields = ['url', 'author', 'image_url', 'tags', 'descriptions']
        extra_kwargs = {'image_url': {'write_only': True},
                        'tags': {'lookup_field': 'name'}}

    def get_or_create_tags(self, tags: list[OrderedDict]) -> list[int]:
        tag_ids = []
        for tag in tags:
            tag_instance, created = Tag.objects.get_or_create(name=dict(tag)['name'])
            tag_ids.append(tag_instance.pk)
        return tag_ids

    def create(self, validated_data):

        tags: list[OrderedDict] = validated_data.pop('tags', [])
        # tags: list[str] = self.get_tags()
        instance = Photo.objects.create(** validated_data)
        if tags:
            instance.tags.set(self.get_or_create_tags(tags))
        return instance

    def update(self, instance, validated_data):
        """Updating fields 'tags' and 'descriptions'.

        Only PATCH method is handled.

        """

        if 'tags' in validated_data:
            tags: list[OrderedDict] = validated_data.pop('tags', [])
            instance.tags.set(self.get_or_create_tags(tags))

        fields = ['descriptions', ]
        for field in fields:
            try:
                setattr(instance, field, validated_data[field])
            except KeyError:  # validated_data may not contain all fields during HTTP PATCH
                pass
        instance.save()

        return instance


class PhotoRatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoRating
        fields = '__all__'


