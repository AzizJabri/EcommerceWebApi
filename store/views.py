from django.http import Http404
from django.shortcuts import render
from .serializers import StoreSerializer, AdressSerializer, ReviewSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Store, Adress, Review
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class StoreListView(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        stores = Store.objects.all()
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.auth.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class StoreDetailView(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Store.objects.get(pk=pk)
        except Store.DoesNotExist:
            return Http404

    def get(self, request, pk):
        store = self.get_object(pk)
        serializer = StoreSerializer(store)
        return Response(serializer.data)

    def put(self, request, pk):
        store = self.get_object(pk)
        serializer = StoreSerializer(store, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        store = self.get_object(pk)
        store.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
