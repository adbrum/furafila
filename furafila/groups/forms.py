'''
Created on //2016

@author: Adriano Regis Vidal Leal
@email: adriano.regis.vidal.leal@outlook.com
'''
from django import forms

from furafila.core.models import WorkGroup


class GroupForm(forms.ModelForm):
    class Meta:
        model = WorkGroup
        fields = ['name', 'description']
