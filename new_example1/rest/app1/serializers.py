from .models import Post,PostDetails,Format
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['name','id']

class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostDetails
        fields = ['description']

class FormatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Format
        fields = '__all__'




