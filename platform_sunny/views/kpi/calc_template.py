# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import JsonResponse, HttpResponseBadRequest
from django.core.files.uploadedfile import UploadedFile
import datetime
import json
import xlrd

#class UploadFileForm(forms.Form):
#    file = forms.FileField()

def calc_template(request):
    
    return render_to_response('kpi/calc.html')

def fileupload(request):
    if request.method == 'POST':
        
        cc = request.POST.get('cc');

        myexcel = request.FILES['files[]']
        excel_obj = UploadedFile(myexcel)
        workbook = xlrd.open_workbook(file_contents = excel_obj.read())
        all_worksheets = workbook.sheet_names()
        
        worksheet_name = all_worksheets[0]
        worksheet = workbook.sheet_by_name(worksheet_name)
        
        for rownum in xrange(worksheet.nrows):
            tmp = []
            for entry in worksheet.row_values(rownum):
                tmp.append(entry)
            print tmp
        
        return JsonResponse({'status': 'fileupload_ok'})