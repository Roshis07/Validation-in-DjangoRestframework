from rest_framework.decorators import api_view
from rest_framework.response import Response
from newApi.models import User  # Make sure you import the correct User model
# Correct the typo in 'serializers'
from newApi.serializers import UserSerializer


@api_view(['GET', 'POST'])  # Specify the HTTP method you want to use
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


@api_view(['GET', 'PUT', 'DELETE'])  # Specify the HTTP method you want to use
def user_details(request, pk):
    if request.method == 'GET':
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    if request.method == 'PUT':

        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    if request.method == 'DELETE':
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(user.name)
