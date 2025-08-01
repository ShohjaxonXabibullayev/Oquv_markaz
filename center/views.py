from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.generics import GenericAPIView
from rest_framework import mixins

class ListCreateAPI(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
    queryset = Oquv_markaz.objects.all()
    serializer_class = Oquv_markazSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class DetailUpdateDlete(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    queryset = Oquv_markaz.objects.all()
    serializer_class = Oquv_markazSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk)

    def patch(self, request, pk):
        return self.partial_update(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)

