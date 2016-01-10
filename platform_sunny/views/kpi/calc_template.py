# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import JsonResponse
import datetime
import json

def calc_template(request):
    
    return render_to_response('kpi/calc.html')