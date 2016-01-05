# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
#from django.db import transaction
from django.http import JsonResponse
import datetime
import json
from platform_sunny.models import t_kpi, t_kpi_records

def kpi_template(request):
    
    return render_to_response('kpi/kpi.html')

def submit_template(request):
    """
    records is a list which consist of dicts, 
    each dict has keys 'stall' and 'coeff'
    """
    if request.method == 'POST':
        #templates = request.POST.get('records')
        #template_name = request.POST.get('name')
        #rule = request.POST.get('rule')
        data = json.loads(request.body)
        templates = data['records']
        template_name =data['name']
        rule = data['rule']
        create_date = datetime.datetime.now()
        
        print(templates)
        
        kpi = t_kpi.objects.create(rule=rule,
                                   name=template_name,
                                   create_date=create_date)
        
        kpi_record_l = []
        for t in templates:
            kpi_record = t_kpi_records(tid=kpi.id,
                                       stall=t['stall'],
                                       coeff=t['coeff'])
            kpi_record_l.append(kpi_record)
        t_kpi_records.objects.bulk_create(kpi_record_l)
        
        return JsonResponse({'status': 'submit_kpi_template_ok'})