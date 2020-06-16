from rest_framework import serializers
from employees.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'
    # id = serializers.IntegerField(read_only=True)
    # name = serializers.CharField(required=True, max_length=25)
    # surname = serializers.CharField(required=True, max_length=25)
    # address = serializers.CharField(required=True, max_length=25)
    # city_birthday = serializers.CharField(required=True, max_length=25)
    # date_birthday = serializers.DateField(required=True)
    # start_work = serializers.DateField(required=True)


    #
    # def create(self, validated_data):
    #     body = validated_data.get('body')
    #     return body

