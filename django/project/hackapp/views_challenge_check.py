from hackapp.models import Challenge_Check
from hackapp.serializer import Challenge_CheckSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# 유저 부분
class Challenge_CheckList(APIView):
    def get(self, request):
        checks = Challenge_Check.objects.all()
        serializer = Challenge_CheckSerializer(checks, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = Challenge_CheckSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Challenge_CheckRegister(APIView):
    def post(self, request):
        serializer = Challenge_CheckSerializer(data=request.data)

        if serializer.is_valid():
            
            serializer.save()
            return Response({"MESSAGE" : "Success!"}, status=status.HTTP_201_CREATED)        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)     

class Challenge_CheckDetail(APIView):
    def get_object(self, pk):
        try:
            return Challenge_Check.objects.get(pk=pk)
        except Challenge_Check.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        check = self.get_object(pk)
        serializer = Challenge_Check(check)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        check = self.get_object(pk)
        serializer = Challenge_Check(check, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        check = self.get_object(pk)
        check.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)