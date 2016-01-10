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
    
def delete_template(request):
    """
    tid is the id of template which will be deleted.
    """
    if request.method == 'POST':
        tid = int(request.POST.get('tid'))
        t_kpi.objects.filter(id=tid).delete()
        
        return JsonResponse({'status': 'delete_kpi_template_ok'})
    
def update_template(request):
    """
    rid is the id of t_kpi_records
    stall
    coeff
    """
    if request.method == 'POST':
        rid = int(request.POST.get('rid'))
        stall = request.POST.get('stall')
        coeff = request.POST.get('coeff')
        
        t_kpi_records.objects.filter(id=rid).update(stall=stall, coeff=coeff)
        return JsonResponse({'status': 'confirm_kpi_record_ok'})
    
def delete_record(request):
    """
    rid is the id of t_kpi_records
    """
    if request.method == 'POST':
        rid = int(request.POST.get('rid'))
        
        t_kpi_records.objects.filter(id=rid).delete()
        return JsonResponse({'status': 'delete_kpi_record_ok'})
    
def save_modify_new(request):
    """
    To save the new t_kpi_records in modify.
    """
    if request.method == 'POST':
        tid = int(request.POST.get('tid'))
        stall = request.POST.get('stall')
        coeff = request.POST.get('coeff')
        
        t = t_kpi_records.objects.create(tid = tid, stall = stall, coeff = coeff)
        
        return JsonResponse({'status': 'save_modify_new_ok', 'new_id': t.id})