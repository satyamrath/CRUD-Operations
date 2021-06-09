from django import forms
from django.db.models import fields
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'
