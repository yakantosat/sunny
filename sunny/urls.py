from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    #url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'platform_sunny.views._index.index_page'),
    url(r'^index.html$', 'platform_sunny.views._index.index_page'),
    url(r'^dashboard.html$', 'platform_sunny.views._dashboard.dashboard'),
    
    url(r'^sunny/kpi/kpi.html', 'platform_sunny.views.kpi.kpi_template.kpi_template'),
    url(r'^sunny/kpi/submit_template/', 'platform_sunny.views.kpi.kpi_template.submit_template'),
)
