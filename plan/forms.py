__author__ = 'Martin'
from django import forms
from plan.models import ModuleSelections, Module
from django.forms.widgets import CheckboxSelectMultiple

"""
class ModuleForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        self.fields["modules"].widget = CheckboxSelectMultiple()
        self.fields["modules"].queryset = Module.objects.all()

"""
class TestForm(forms.Form):

    Choices2 = Module.objects.all()
    Choices2 = ((x.id, x.name) for x in Choices2)
    CHOICES = (('hi', 'Wert1',), ('ho','Wert2',))
    section = forms.CharField(widget=forms.HiddenInput())
    stuff = forms.MultipleChoiceField(Choices2, widget=forms.CheckboxSelectMultiple(), required=False)


