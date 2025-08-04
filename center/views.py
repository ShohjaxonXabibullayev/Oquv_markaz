from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import *
from .serializer import *
from rest_framework.generics import GenericAPIView
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q


#APIView uchun

# class OquvmarkazAPIView(APIView):
#     def get(self, request):
#         oquv_markaz = Oquv_markaz.objects.all()
#         category = request.GET.get('category')
#         name = request.GET.get('name')
#         if category:
#             oquv_markaz = oquv_markaz.filter(Category__name=category)
#         if name:
#             oquv_markaz = oquv_markaz.filter(name=name)
#         search = request.GET.get('search')
#         if search:
#             oquv_markaz = oquv_markaz.filter(Q(name__icontains=search) | Q(desc__icontains=search))
#         ordering = request.GET.get('ordering')
#         if ordering:
#             oquv_markaz = oquv_markaz.order_by(ordering)
#         serializer = Oquv_markazSerializer(oquv_markaz, many=True)
#         return Response(serializer.data)


#GenericAPIView(mixinsiz)

# class Oquv_markazAPIView(GenericAPIView):
#     serializer_class = Oquv_markazSerializer
#     queryset = Oquv_markaz.objects.all()
#
#     def get(self, request):
#         oquv_markaz = self.get_queryset()
#         category = request.GET.get('category')
#         name = request.GET.get('name')
#         if category:
#             oquv_markaz = oquv_markaz.filter(Category__name=category)
#         if name:
#             oquv_markaz = oquv_markaz.filter(name=name)
#         search = request.GET.get('search')
#         if search:
#             oquv_markaz = oquv_markaz.filter(Q(name__icontains=search) | Q(desc__icontains=search))
#         ordering = request.GET.get('ordering')
#         if ordering:
#             oquv_markaz = oquv_markaz.order_by(ordering)
#         serializer = self.get_serializer(oquv_markaz, many=True)
#         return Response(serializer.data)

#GenericAPIView(mixins bilan)

class Oquv_markaz_mixins(mixins.ListModelMixin, GenericAPIView):
    queryset = Oquv_markaz.objects.all()
    serializer_class = Oquv_markazSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['Category__name', 'name']
    search_fields = ['name', 'desc']
    ordering_fields = ['number_of_teacher', 'name', 'number_of_students']
    ordering = ['name']

    def get(self, request):
        return self.list(request)



























# class ListCreateAPI(mixins.ListModelMixin, mixins.CreateModelMixin, GenericAPIView):
#     queryset = Oquv_markaz.objects.all()
#     serializer_class = Oquv_markazSerializer
#
#     def get(self, request):
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
# class DetailUpdateDlete(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView):
#     queryset = Oquv_markaz.objects.all()
#     serializer_class = Oquv_markazSerializer
#
#     def get(self, request, pk):
#         return self.retrieve(request, pk=pk)
#
#     def put(self, request, pk):
#         return self.update(request, pk)
#
#     def patch(self, request, pk):
#         return self.partial_update(request, pk)
#
#     def delete(self, request, pk):
#         return self.destroy(request, pk)
#
