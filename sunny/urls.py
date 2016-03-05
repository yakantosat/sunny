from django.conf.urls import patterns, include, url
from django.contrib import admin

from tastypie.api import Api
from platform_sunny.api import (KpiTemplates,
                                KpiTemplateRecords)

v1_api = Api(api_name='v0.1a')
v1_api.register(KpiTemplates())
v1_api.register(KpiTemplateRecords())

urlpatterns = patterns('',
    (r"^api/", include(v1_api.urls)),
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'platform_sunny.views._index.index_page'),
    url(r'^index.html$', 'platform_sunny.views._index.index_page'),
    url(r'^dashboard.html$', 'platform_sunny.views._dashboard.dashboard'),
    
    url(r'^sunny/kpi/kpi.html', 'platform_sunny.views.kpi.kpi_template.kpi_template'),
    url(r'^sunny/kpi/submit_template/', 'platform_sunny.views.kpi.kpi_template.submit_template'),
    url(r'^sunny/kpi/delete_template/', 'platform_sunny.views.kpi.kpi_template.delete_template'),
    url(r'^sunny/kpi/update_template/', 'platform_sunny.views.kpi.kpi_template.update_template'),
    url(r'^sunny/kpi/delete_record/', 'platform_sunny.views.kpi.kpi_template.delete_record'),
    url(r'^sunny/kpi/save_modify_new/', 'platform_sunny.views.kpi.kpi_template.save_modify_new'),
    
    url(r'^sunny/kpi/calc.html', 'platform_sunny.views.kpi.calc_template.calc_template'),
    url(r'^sunny/kpi/file_upload/', 'platform_sunny.views.kpi.calc_template.fileupload'),
)
