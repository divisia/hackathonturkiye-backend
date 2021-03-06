from blog.models import *
from profile.serializers import *
from rest_framework import serializers
from action_serializer import ModelActionSerializer
from common.serializers import TagSerializer

class PostTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTag
        fields = ['name']

class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCategory
        fields = ['name']


class PostSerializer(ModelActionSerializer):
    category = PostCategorySerializer(many=False, read_only=False)
    tags = TagSerializer(many=True, read_only=False)
    author = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Post
        fields = [
            'slug',
            'pk',
            'title',
            'summary',
            'body',
            'published_at',
            'author',
            'category',
            'tags',
            'read',
            'time',
            'thumbnail',
            'priority',
        ]
        action_fields = {"list": {"fields": (
            "slug",
            'summary',
            "title",
            'author',
            'category',
            'tags',
            'read',
            'time',
            'thumbnail',
            'published_at',
        )}}
    
    def create(self, validated_data):
        request = self.context["request"]
        user = request.user
        category = PostCategory.objects.get(name=validated_data['category'])

        validated_data.update({
            'author': user,
            'time': len(validated_data['body'])//500,
        })

        return Event.objects.create(added_by=user, **validated_data)


