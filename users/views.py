from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserCreateSerializer, UserListSerializer, UserLoginSerializer
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsLibrarian


class UserCreateView(APIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    @extend_schema(request=UserCreateSerializer)
    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                return Response({
                    "message": "User created successfully",
                }, status=status.HTTP_201_CREATED)

        response = {
            "errors": serializer.errors
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated, IsLibrarian]


class UserDetailsView(generics.RetrieveUpdateDestroyAPIView):
    http_method_names = ['get', 'post', 'put', 'delete']
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated, IsLibrarian]


class UserLoginView(APIView):
    @extend_schema(request=UserLoginSerializer)
    def post(self, request):
        print()
        print(request.data)
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid login credentials, user not found")

        try:
            refresh = RefreshToken.for_user(user)
            refresh_token = str(refresh)
            access_token = str(refresh.access_token)

            validation = {
                'access': access_token,
                'refresh': refresh_token,
                'username': user.username,
                'role': user.role,
            }

            return Response(validation, status=status.HTTP_200_OK)
        except:
            pass

        raise serializers.ValidationError("Invalid login credentials")