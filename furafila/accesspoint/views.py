from django.shortcuts import render


def new(request):
    return render(request, 'accesspoint/accesspoint_form.html')