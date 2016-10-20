from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import resolve_url as r
from furafila.core.models import WorkGroup
from furafila.groups.forms import GroupForm


def new(request):
    if request.method == 'POST':
        return create(request)

    return empty_form(request)


def empty_form(request):
    return render(request, 'groups/group_form.html',
                  {'form': GroupForm()})


def create(request):
    form = GroupForm(request.POST)
    if not form.is_valid():
        return render(request, 'groups/group_form.html',
                      {'form': form})

    group = WorkGroup.objects.create(**form.cleaned_data)
    return HttpResponseRedirect(r('group:detail', group.pk))


def detail(request, pk):
    try:
        group = WorkGroup.objects.get(pk=pk)
    except WorkGroup.DoesNotExist:
        raise Http404

    return render(request, 'groups/group_detail.html', {'form': group})
