from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from website.api.serializers import MessageSerializer, MessageCreateSerializer, UserSerializer, UserCreateSerializer
from website.models import Message


@api_view(['GET'])
def get_messages(request):
    messages = Message.objects.all()
    serialized_messages = MessageSerializer(messages, many=True)

    return Response(serialized_messages.data, status=200)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_message(request, id):
    message = Message.objects.get(id=id)
    serialized_message = MessageSerializer(message, many=False)
    return Response(serialized_message.data, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_message(request):

    if request.method == 'POST':
        new_message = Message()
        new_message.author = User.objects.get(id=1)
        #category_id = request.data['category']
        #new_message.category = Category.objects.get(id=category_id)
        message = MessageCreateSerializer(data=request.data, instance=new_message)
        if message.is_valid():
            message.save()
            return Response(message.data, status=status.HTTP_201_CREATED)
    return Response("nope sorry", status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        user = UserCreateSerializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response(user.data.username, status=status.HTTP_201_CREATED)
    return Response("nope sorry", status=status.HTTP_400_BAD_REQUEST)
