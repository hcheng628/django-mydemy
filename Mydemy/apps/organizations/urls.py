# -*- coding: utf-8 -*-

from django.conf.urls import url

from organizations.views import OrgView, UserRequestView, OrgOverviewView, OrgInfoView, OrgInstructorView, OrgCourseView

urlpatterns = [
    url(r'^list/$', OrgView.as_view(), name='list'),
    url(r'^user_request/$', UserRequestView.as_view(), name='user_request'),
    url(r'^org_overview/(?P<org_id>\d+)/$', OrgOverviewView.as_view(), name='org_overview'),
    url(r'^org_info/(?P<org_id>\d+)/$', OrgInfoView.as_view(), name='org_info'),
    url(r'^org_instructor/(?P<org_id>\d+)/$', OrgInstructorView.as_view(), name='org_instructor'),
    url(r'^org_course/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name='org_course'),
]