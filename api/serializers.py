from rest_framework import serializers
from employer.models import Employee
from timetable.models import Work
from api.models import Demo
from django.contrib.auth import get_user_model

class DemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demo
        fields = ('post',)
        
class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ('employee', 'work_date', 'has_work', 'start_time', 'end_time', 'notes')
        read_only_fields = ('employee',)
        

class EmployeeSerializer(serializers.ModelSerializer):
    #emp_id = serializers.ReadOnlyField()
    #works = serializers.PrimaryKeyRelatedField(many= True, read_only = True)
    works = WorkSerializer(many=True)
    class Meta:
        model = Employee
        fields = ('id', 'emp_id', 'first_name', 'last_name', 'email', 'is_supervisor','works')
        read_only_fields = ('emp_id', 'is_supervisor')

