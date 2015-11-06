from datetime import date, timedelta
from django.shortcuts import render
import django_filters
from employer.models import Employee, Employer
from timetable.models import Work
from api.models import Demo
from django.views.generic import ListView, DetailView
from rest_framework import generics
from rest_framework import permissions
from rest_framework import filters
from api.serializers import EmployeeSerializer, WorkSerializer, DemoSerializer
from api.permissions import IsOwnerAndSuperVisorOrReadOnly

#weekly date extract code
def allmondays(year):
    """This code was provided in the previous answer! It's not mine!"""
    d = date(year, 1, 1)# January 1st
    print(d.weekday())
    if d.weekday() != 0:
        
        d = d+timedelta(days = -d.weekday(), weeks = 1)  # First Monday                                                     
    while d.year == year:
        yield d
        d += timedelta(days = 7)
        
def week_dict(year):
    week_dates = {}
    for wn, day in enumerate(allmondays(year)):
        #week_dates[wn+1] = [(day+timedelta(days=k)) for k in range(0,7)]
        week_dates[wn+1] = (day, day+timedelta(days=7))
    return week_dates
    
class DemoCreate(generics.ListCreateAPIView):
    queryset = Demo.objects.all()
    serializer_class = DemoSerializer
    


class EmployeeList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('first_name',)
    
class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerAndSuperVisorOrReadOnly)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class WorkList(generics.ListAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    
class WorkFilter(django_filters.FilterSet):
    year = django_filters.DateFilter(name="work_date", lookup_type="year")
    month = django_filters.NumberFilter()
    class Meta:
        model = Work
        fields = ('year', 'month', 'has_work')
        
    
class EmployeeWorkList(generics.ListAPIView):
    serializer_class = WorkSerializer
  
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = WorkFilter
    
    def get_queryset(self):
        emp_pk=self.kwargs['pk']
        employee = Employee.objects.get(id=emp_pk)
        return Work.objects.filter(employee=employee)

class MonthlyWorkList(generics.ListAPIView):
    serializer_class = WorkSerializer
    
    def get_queryset(self):
        queryset = Work.objects.all()
        month = self.request.query_params.get('month', None)
        year = self.request.query_params.get('year', None)
        if month is not None and year is not None:
            queryset = queryset.filter(work_date__month = int(month), work_date__year = int(year))
        return queryset
        
class WeeklyWorkList(generics.ListAPIView):
    serializer_class = WorkSerializer
    
    def get_queryset(self):
        year = self.kwargs['year']
        week_num= self.kwargs['week_num']
        week_dates = week_dict(int(year))[int(week_num)]
        
        queryset = Work.objects.filter(work_date__range=week_dates)
        return queryset
        
        
        
        
