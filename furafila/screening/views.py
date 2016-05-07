from django.shortcuts import render


def new(request):
    return render(request, 'screening/screening_form.html')