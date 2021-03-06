from datetime import datetime

from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import resolve_url as r
from django.shortcuts import render

from furafila.core.models import Ticket, Service
from furafila.tickets.forms import TicketForm


def new(request):
    """Dispacher - Ponto de Entrada"""
    if request.method == 'POST':
        return create(request)

    return empty_form(request)


def empty_form(request):
    """Se o pedido vier como GET - mostra o formulário vazio"""
    return render(request, 'tickets/ticket_form.html',
                  {'form': TicketForm()})


def create(request):
    """Se o pedido vier como POST"""
    form = TicketForm(request.POST)

    if not form.is_valid():
        """Caso de insucesso - aborta o pedido"""
        return render(request, 'tickets/ticket_form.html',
                      {'form': form})

    service = Service.objects.get(pk=request.POST.get('service'))
    # service = Service.objects.get(name='Atendimento Geral')

    pos = Ticket.objects.filter(service_id=service.pk, created_at__date=datetime.now().date()).last()

    try:
        new_ticket = counter(service.prefixo, pos.ticket[1:])
    except:
        new_ticket = counter(service.prefixo, 0)

    ticket = Ticket.objects.create(service_id=service.pk,
                                   ticket=new_ticket)  # Quando é utilizado o forms.Form no form.

    return HttpResponseRedirect(r('ticket:detail', ticket.pk))


def detail(request, pk):
    try:
        ticket = Ticket.objects.get(pk=pk)
    except Ticket.DoesNotExist:  # Levanta o erro se não existir na base de dados.
        raise Http404

    return render(request, 'tickets/ticket_detail.html', {'form': ticket})


def counter(prefixo, pos=0):
    pos = int(pos)
    pos += 1
    return prefixo + str(pos)
