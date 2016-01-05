# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.
# t_kpi 模板表
class t_kpi(models.Model):
    rule = models.CharField(verbose_name="规则", max_length=10)
    name = models.CharField(verbose_name="模板名称", max_length=100)
    create_date = models.DateTimeField(verbose_name="录入日期")
    
    class Meta:
        db_table = "t_kpi"
        ordering = ['-create_date']
        
# t_kpi_records 模板记录
class t_kpi_records(models.Model):
    tid = models.IntegerField(verbose_name="模板表ID")
    stall = models.CharField(verbose_name="档位", max_length=100)
    coeff = models.FloatField(verbose_name="系数")
    
    class Meta:
        db_table = "t_kpi_records"