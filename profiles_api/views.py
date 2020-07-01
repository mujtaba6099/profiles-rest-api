from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """API VIEW"""
    def get(self,request,format=None):
        an_apiview=[
        'Uses HTTP methods as function (get,post,patch,put,delete)',
        "Is similar to traditional django view"
        ]
        return Response({'message':'Hello','api':an_apiview})
