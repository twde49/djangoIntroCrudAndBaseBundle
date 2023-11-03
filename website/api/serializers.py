from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from website.models import Message, Category, Response


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class ResponseSerializer(ModelSerializer):
    author = UserSerializer()

    class Meta:
        model = Response
        fields = ["id", "content", "author"]


class MessageSerializer(ModelSerializer):
    category = CategorySerializer()
    responses = ResponseSerializer(many=True)
    author = UserSerializer()

    class Meta:
        model = Message
        fields = ["author", "title", "content", 'category', 'responses']
        # depth = 1


class MessageCreateSerializer(ModelSerializer):

    class Meta:
        model = Message
        fields = ["title", "content", "author"]


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]
