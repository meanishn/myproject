from django.conf.urls import url, include, patterns
from api import views

urlpatterns = patterns('',
    #url(r'^employees/$', views.EmployeeList.as_view(), name = "employee_list"),
    url(r'^employees/$', views.EmployeeList.as_view()),
    url(r'^employees/(?P<pk>\d+)/$', views.EmployeeDetail.as_view()),
    url(r'^employees/(?P<pk>\d+)/works/$', views.EmployeeWorkList.as_view()),
    url(r'^works/$', views.MonthlyWorkList.as_view()),
    url(r'^works/week/(?P<year>\d+)/(?P<week_num>\d+)/$', views.WeeklyWorkList.as_view()),
    url(r'^api_demo/$', views.DemoCreate.as_view()),
    )