from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import resolve_url as r
from furafila.accesspoint.forms import AccessPointForm
from furafila.core.models import AccessPoint


def new(request):
    """Dispacher - Ponto de Entrada"""
    if request.method == 'POST':
        return create(request)

    return empty_form(request)


def empty_form(request):
    """Se o pedido vier como GET - mostra o formulário vazio"""
    return render(request, 'accesspoint/accesspoint_form.html',
                  {'form': AccessPointForm()})


def create(request):
    """Se o pedido vier como POST"""
    form = AccessPointForm(request.POST)
    if not form.is_valid():
        return render(request, 'accesspoint/accesspoint_form.html',
                      {'form': form})

    ap = AccessPoint.objects.create(**form.cleaned_data)

    return HttpResponseRedirect(r('accesspoint:detail', ap.pk))


def detail(request, pk):
    try:
        ap = AccessPoint.objects.get(pk=pk)
    except AccessPoint.DoesNotExist:
        raise Http404

    return render(request, 'accesspoint/accesspoint_detail.html', {'form': ap})

