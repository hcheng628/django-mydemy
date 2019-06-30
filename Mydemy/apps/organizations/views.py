from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from Mydemy.settings import PAGINATION_SETTINGS
from .models import City, CourseOrg


class OrgView(View):
    def get(self, request):
        all_cities = City.objects.all()
        all_orgs = CourseOrg.objects.all()
        top_orgs = all_orgs.order_by('-click_count')[:5]
        city_filter = request.GET.get('city_filter', '')
        provider_type = request.GET.get('provider_type', '')
        org_list_order_by = request.GET.get('org_list_order_by', '')

        if city_filter:
            all_orgs = all_orgs.filter(city=city_filter)

        if provider_type:
            all_orgs = all_orgs.filter(category=provider_type)

        if org_list_order_by:
            if org_list_order_by == 'student':
                all_orgs = all_orgs.order_by('-student_count')
            elif org_list_order_by == 'course':
                all_orgs = all_orgs.order_by('-course_count')
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_orgs, PAGINATION_SETTINGS['PAGE_RANGE_DISPLAYED'], request=request)
        ret_orgs = p.page(page)

        return render(request, 'org-list.html', {
            'all_cities': all_cities,
            'all_orgs': ret_orgs,
            'top_orgs': top_orgs,
            'org_count': all_orgs.count(),
            'city_filter': city_filter,
            'provider_type': provider_type,
            'org_list_order_by': org_list_order_by,
        })
