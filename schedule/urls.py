from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'timetable.views.home', name='home'),
    url(r'^accounts/', include('registration.urls', namespace='registration')),
    url(r'^schedule/', include('timetable.urls', namespace='employee_schedule')),
    url(r'^messageboard/', include('messageboard.urls', namespace='messageboard')),
    url(r'^employer/', include('employer.urls', namespace="employer")),
    url(r'^api/',include('api.urls', namespace = "api")),
    url(r'^api-auth/', include('rest_framework.urls', namespace = "rest_framework")),
    url(r'mydemo/$','timetable.views.demo'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
