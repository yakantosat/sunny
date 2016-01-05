from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie import fields
from tastypie.authorization import DjangoAuthorization, Authorization
from tastypie.authentication import BasicAuthentication, Authentication
from platform_sunny.models import (t_kpi,
                                   t_kpi_records)
from platform_sunny.serializers import DateTimeSerializer
from django.db.models import Count, Sum, Avg
import datetime

