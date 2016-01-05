# -*- coding:utf-8 -*-

from tastypie.serializers import Serializer

class DateTimeSerializer(Serializer):
    def format_datetime(self, data):
        return data.strftime("%Y-%m-%d %H:%M:%S")