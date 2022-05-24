from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework import filters
from rest_framework import status, viewsets
from rest_framework.response import Response
class TransactionView(viewsets.ModelViewSet):  
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Transaction.objects.all()
    serializer_class=TransactionSerializer



class TransactionUserArtistID(generics.GenericAPIView):
    def get(self,request,format=None,user_id=None):
        try:
            print(user_id)
            transaction_items = Transaction.objects.filter(artist_id=user_id)
            serializers = TransactionSerializer(transaction_items,many=True)
            print(serializers.data)
            return Response(data=serializers.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])

class TransactionUserClientID(generics.GenericAPIView):
    def get(self,request,format=None,user_id=None):
        try:
            print(user_id)
            transaction_items = Transaction.objects.filter(user_id=user_id)
            serializers = TransactionSerializer(transaction_items,many=True)
            print(serializers.data)
            return Response(data=serializers.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])
