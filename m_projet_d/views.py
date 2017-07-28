from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render_to_response

def indexdef(request):
    return render_to_response('Google.html')




# def indexdef(request):
#     return HttpResponse('Google.html')