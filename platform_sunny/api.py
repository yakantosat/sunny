from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie import fields
from tastypie.authorization import DjangoAuthorization, Authorization
from tastypie.authentication import BasicAuthentication, Authentication
from platform_sunny.models import (t_kpi,
                                   t_kpi_records)
from platform_sunny.serializers import DateTimeSerializer
from django.db.models import Count, Sum, Avg
import datetime

class KpiTemplates(ModelResource):
    
    class Meta:
        limit = 0
        queryset = t_kpi.objects.all()
        resource_name = "templates"
        allowed_methods = ['get', ]
        fields = ['id', 'rule', 'name', 'create_date']
        authentication = Authentication()
        authorization = Authorization()
        always_return_data = True
        serializer = DateTimeSerializer()
        filtering = {'id': ALL}
        
class KpiTemplateRecords(ModelResource):
    
    class Meta:
        limit = 0
        queryset = t_kpi_records.objects.all()
        resource_name = 'template_records'
        allowed_methods = ['get', ]
        fields = ['id', 'tid', 'stall', 'coeff']
        authentication = Authentication()
        authorization = Authorization()
        always_return_data = True
        filtering = {'id': ALL, 'tid': ALL_WITH_RELATIONS}

