from django.shortcuts import render, get_object_or_404
from .serializers import MenuItemSerializer
from .models import MenuItem
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class MenuItemView(generics.ListCreateAPIView):
    
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    
    
class SingleMenuItemView(APIView):
    
    def get(self, request, pk):
        menu_item = get_object_or_404(MenuItem, pk=pk)
        serializer = MenuItemSerializer(menu_item)
        return Response(serializer.data)
    
    def put(self, request, pk):
        menu_item = get_object_or_404(MenuItem, pk=pk)
        serializer = MenuItemSerializer(menu_item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        menu_item = get_object_or_404(MenuItem, pk=pk)
        menu_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
@api_view()
@permission_classes([IsAuthenticated])
# @authentication_classes([TokenAuthentication])
def msg(request):
    return Response({"message": "This view is protected"})

