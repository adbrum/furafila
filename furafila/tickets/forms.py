'''
Created on //2016

@author: Adriano Regis Vidal Leal
@email: adriano.regis.vidal.leal@outlook.com
'''
from django import forms

from furafila.core.models import Ticket


class TicketForm(forms.Form):
    class Meta:
        model = Ticket
        fields = ['service', 'ticket']
