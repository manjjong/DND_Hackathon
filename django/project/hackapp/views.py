from hackapp.models import User, Follow
from hackapp.serializer import UserSerializer, FollowSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# 유저 부분
class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRegister(APIView):
    def post(self, request):
        users = User.objects.all()

        for user in users:
            if user.user_id == request.data['user_id']:
                 return Response({"ERROR" : "This ID already exists."}, status=status.HTTP_400_BAD_REQUEST)
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"MESSAGE" : "Success!"}, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

class UserLogin(APIView):
    def post(self, request):
        users = User.objects.all()

        for user in users:
            if user.user_id == request.data['user_id'] and user.user_pw == request.data['user_pw']:
                return Response({"MESSAGE" : "Success!"}, status=status.HTTP_201_CREATED)
        return Response({"ERROR" : "The ID or password is wrong."}, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# 팔로우 부분
class FollowList(APIView):
    def get(self, request):
        follows = Follow.objects.all()
        serializer = FollowSerializer(follows, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = FollowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FollowCheck(APIView):
    def post(self, request):
        if User.objects.filter(user_id=request.data['user_id']).exists() and User.objects.filter(user_id=request.data['target_id']).exists():
            if Follow.objects.filter(user_id=request.data['user_id']).filter(target_id=request.data['target_id']).exists():
                return Response({"Message":True}, status.HTTP_202_ACCEPTED)
            return Response({"Message":False}, status.HTTP_202_ACCEPTED)
        return Response({"ERROR" : "User ID or Target ID does not exist."}, status=status.HTTP_400_BAD_REQUEST)

class FollowUser(APIView):
    def post(self, request):
        if User.objects.filter(user_id=request.data['user_id']).exists():
            follows = Follow.objects.filter(user_id=request.data['user_id'])
            arr = [x.target_id.user_id for x in follows]
            return Response({"follow":arr}, status.HTTP_202_ACCEPTED)
        return Response({"ERROR" : "User ID does not exist."}, status=status.HTTP_400_BAD_REQUEST)


class FollowRegister(APIView):
    def post(self, request):
        serializer = FollowSerializer(data=request.data)
        if serializer.is_valid():
            if Follow.objects.filter(user_id=request.data['user_id']).filter(target_id=request.data['target_id']).exists():
                return Response({"ERROR" : "It's a follow that already exists."})
            if User.objects.filter(user_id=request.data['user_id']).exists() and User.objects.filter(user_id=request.data['target_id']).exists():
                serializer.save()
                return Response({"MESSAGE" : "Success!"}, status=status.HTTP_201_CREATED)
            return Response({"ERROR" : "User ID or Follow ID does not exist."}, status=status.HTTP_400_BAD_REQUEST)  
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

class FollowDetail(APIView):
    def get_object(self, user_id, target_id):
        try:
            return Follow.objects.filter(user_id=user_id).filter(target_id=target_id)
        except Follow.DoesNotExist:
            raise Http404

    def get(self, request, user_id, target_id, format=None):
        follow = self.get_object(user_id, target_id)
        serializer = FollowSerializer(follow, many=True)
        return Response(serializer.data)
    
    def put(self, request, user_id, target_id, format=None):
        follow = self.get_object(user_id, target_id)
        serializer = FollowSerializer(follow, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id, target_id, format=None):
        follow = self.get_object(user_id, target_id)
        follow.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)