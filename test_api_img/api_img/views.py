from django.contrib.auth.models import User

from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import Img
from .serializers import ImgSerializer, RegisterUserSerializer, UserSerializer


class ViewAndCreate(generics.ListCreateAPIView):
    serializer_class = ImgSerializer

    def get_queryset(self):
        queryset = Img.objects.filter(user=self.request.user.id)
        return queryset


class Update(generics.UpdateAPIView):
    queryset = Img.objects.all()
    serializer_class = ImgSerializer


class AboutMe(generics.ListAPIView):

    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.filter(username=self.request.user)
        return queryset


class DeleteForUser(generics.DestroyAPIView):

    serializer_class = ImgSerializer

    def get_queryset(self):
        queryset = Img.objects.filter(user=self.request.user)
        return queryset

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(data='Data deleted', status=status.HTTP_204_NO_CONTENT)


class DeleteForAdmin(generics.DestroyAPIView):
    queryset = Img.objects.all()
    serializer_class = ImgSerializer
    permission_classes = (IsAdminUser, )

    def delete(self, request, *args, **kwargs):
        for instance in Img.objects.all():
            self.perform_destroy(instance)
        return Response(data='Data deleted', status=status.HTTP_204_NO_CONTENT)


class RegisterUser(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterUserSerializer

    def post(self, request, *args, **kwargs):

        serializer = RegisterUserSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()
            return Response(data='Registration completed successfully', status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)
