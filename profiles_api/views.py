from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

class HelloApiView(APIView):
    """API VIEW"""
    serializer_class=serializers.HelloSeiralizer
    def get(self,request,format=None):
        an_apiview=[
        'Uses HTTP methods as function (get,post,patch,put,delete)',
        "Is similar to traditional django view"
        ]
        return Response({'message':'Hello','api':an_apiview})

    def post(self,request):
        serializer =self.serializer_class(data=request.data)

        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            email=serializer.validated_data.get('email')
            message=f" Hello {name} {email}"
            return Response({'message':message})
        else:
            return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
            )

    def put(self,request,pk=None):
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
            return Response({'method':'Patch'})

    def delete(self,request,pk=None):
        return Response({'method':'delete'})        
