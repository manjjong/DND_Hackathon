from hackapp.models import Challenge
from hackapp.serializer import ChallengeSerializer, Challenge_UserSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers, status
from django.http import Http404

import datetime as dt
import requests

# 도전 부분
class ChallengeList(APIView):
    def get(self, request):
        challenges = Challenge.objects.all()
        serializer = ChallengeSerializer(challenges, many=True)
        print(serializer.data)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ChallengeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChallengeRegister(APIView):
    def post(self, request):
        serializer = ChallengeSerializer(data=request.data)
        if serializer.is_valid():
            n = dt.datetime.now()
            s = dt.datetime.strptime(request.data['start_date'], "%Y-%m-%d")
            e = dt.datetime.strptime(request.data['end_date'], "%Y-%m-%d")
            if n > s and e > s:
                return Response({"ERROR" : "The Start Date or End Date is before Today's Date."}, status=status.HTTP_202_ACCEPTED)
            if s > e:
                return Response({"ERROR": "The End Date is before Start Date."}, status=status.HTTP_202_ACCEPTED)
            serializer.save()
            ser = Challenge_UserSerializer(data={"challenge_id": serializer.data['challenge_id'], 'user_id':request.data['creator_id'], 'start_date':request.data['start_date']})
            if ser.is_valid():
                ser.save()
            return Response({"MESSAGE" : "Success!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChallengeModify(APIView):
    def put(self, request, pk, format=None):
        challenge = Challenge.objects.filter(pk=pk)[0]
        if len(request.data['name']) != 0 and len(request.data['contents']) != 0:
            challenge.name = request.data['name']
            challenge.contents = request.data['contents']
            challenge.save()
            return Response({"MESSAGE":"Success!"}, status=status.HTTP_200_OK)
        return Response({"ERROR" : "The length of the name or content is zero."}, status=status.HTTP_200_OK)

class ChallengeDetail(APIView):
    def get_object(self, pk):
        try:
            return Challenge.objects.filter(pk=pk)
        except Challenge.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        challenge = self.get_object(pk)
        serializer = ChallengeSerializer(challenge, many=True)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        challenge = self.get_object(pk)
        serializer = ChallengeSerializer(challenge, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        challenge = self.get_object(pk)
        challenge.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
