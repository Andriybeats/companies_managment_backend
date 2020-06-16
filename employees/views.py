from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response

from employees.models import Employee
from employees.serializers import EmployeeSerializer


class CreateRetrieveUpdateDeleteEmployeeView(generics.CreateAPIView,
                                             generics.UpdateAPIView,
                                             generics.RetrieveAPIView,
                                             generics.DestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


    def put(self, request, *args, **kwargs):
        #instance = self.get_object()
        serializer = EmployeeSerializer(self.get_object(), data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.serializer_class = EmployeeSerializer
        return super().retrieve(request, *args, **kwargs)

class EmployeeListAPIView(generics.ListAPIView):

    queryset = EmployeeSerializer
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data)