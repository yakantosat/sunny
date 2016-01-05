from django.shortcuts import render_to_response

def index_page(request):
    
    return render_to_response('index.html')