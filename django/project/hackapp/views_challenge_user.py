from hackapp.models import Challenge_User
from hackapp.serializer import Challenge_UserSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.db.models import Q

import datetime as dt

# 도전 부분
class Challenge_UserList(APIView):
    def get(self, request):
        challenge_users = Challenge_User.objects.all()
        serializer = Challenge_UserSerializer(challenge_users, many=True)
        print(serializer.data)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Challenge_UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Challenge_UserRegister(APIView):
    def post(self, request):
        serializer = Challenge_UserSerializer(data=request.data)
        if serializer.is_valid():
            n = dt.datetime.now()
            s = dt.datetime.strptime(request.data['start_date'], "%Y-%m-%d")
            
            if n > s:
                return Response({"ERROR" : "The Start Date is before Today's Date."}, status=status.HTTP_202_ACCEPTED)

            if Challenge_User.objects.filter(Q(challenge_id=request.data['challenge_id']) & Q(user_id=request.data['user_id'])).exists():
                return Response({"ERROR" : "Challenge ID and User ID that already exist."}, status=status.HTTP_200_OK)
            serializer.save()
            return Response({"MESSAGE" : "Success!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Challenge_UserDetail(APIView):
    def get_object(self, pk):
        try:
            return Challenge_User.objects.filter(pk=pk)
        except Challenge_User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        challenge_user = self.get_object(pk)        
        serializer = Challenge_UserSerializer(challenge_user, many=True)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        challenge_user = self.get_object(pk)
        serializer = Challenge_UserSerializer(challenge_user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        challenge_user = self.get_object(pk)
        challenge_user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
