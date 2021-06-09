from django.core import paginator
from django.db.models import query
from myApp.forms import DocumentForm
from myApp.models import Document
from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import Document
import os
from django.conf import settings
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    # query = request.GET['query']
    documents = Document.objects.all().order_by('-creation_time')

    paginator = Paginator(documents, 3)

    
    page = request.GET.get('page')
    
    # ?page=2
    
    documents = paginator.get_page(page)

    params = {'documents': documents}
    # return render(request, 'index.html',{'shelf':shelf})
    return render(request, 'myApp/index.html', params)

def create(request):
    newUpload = DocumentForm()
    if  request.method == 'POST':
        newUpload = DocumentForm(request.POST,request.FILES)
        # newUpload.creation_time = datetime.now()
        if newUpload.is_valid():
            newUpload.save()
            return redirect("Home")
        else:
            return HttpResponse("Some Error has occurred, please upload after some time<br/> <a href='/create'>Retry</a>")

    params = { "uploadForm": newUpload}
    print(type(newUpload))
    return render(request, "myApp/create.html", params)


def update(request, document_id):
    document_id = int(document_id)
    try:
        document_self = Document.objects.get(id = document_id)
    except Document.DoesNotExist:
        return redirect('Home')
    if request.method == 'POST':
        document_form = DocumentForm(request.POST, request.FILES, instance=document_self)
        if document_form.is_valid():
            document_form.save()
            return redirect("Home") # updated
        else:
            document_form = DocumentForm(request.POST, instance=document_self)
            if document_form.is_valid():
                document_form.save()
                return redirect("Home") # updated
            else:
                return HttpResponse("Some Error has occurred, <a href='/update/" + str(document_id) + "'>Retry</a>")
    else:
        document_form = DocumentForm(None, instance=document_self)
    params = {"document_form": document_form}
    return render(request, 'myApp/update.html', params)

def delete(request, document_id):
    if request.method == "POST":
        document_id = int(document_id)
        try:
            document_self = Document.objects.get(id = document_id)
            document_self.delete()
            return redirect("Home")
        except Document.DoesNotExist:
            return redirect("Home")
    else:
        return redirect("Home")


def search(request):
    try:
        mixed_query = request.GET['mixed_query']
    except:
        mixed_query = ""
    try:
        title_query = request.GET['title_query']
    except:
        title_query = ""
    try:
        author_query = request.GET['author_query']
    except:
        author_query = ""
    try:
        subject_query = request.GET['subject_query']
    except:
        subject_query = ""
    try:
        document_type_query = request.GET['document_type_query']
    except:
        document_type_query = ""
    
    query = {"mixed_query": mixed_query, "title_query": title_query, "author_query": author_query, "subject_query": subject_query, "document_type_query": document_type_query}

    if len(title_query) or len(author_query) or len(subject_query) or len(document_type_query):
        documents = Document.objects.filter(document_title__icontains = title_query).filter(author__icontains = author_query).filter(subject__icontains = subject_query, document_type__icontains = document_type_query).order_by('-creation_time')
    else:
        documents1 = Document.objects.filter(document_title__icontains = mixed_query)
        documents2 = Document.objects.filter(author__icontains = mixed_query)
        documents3 = Document.objects.filter(subject__icontains = mixed_query)
        documents4 = Document.objects.filter(document_type__icontains = mixed_query) 
        # documents5 = Document.objects.filter(document_file__icontains = mixed_query) 
        # documents = documents1.union(documents2, documents3, documents4, documents5).order_by
        documents = documents1.union(documents2, documents3, documents4).order_by('-creation_time')

    paginator = Paginator(documents, 3)
    page = request.GET.get('page')
    # ?page=2
    documents = paginator.get_page(page)
    params = {'query': query, 'documents': documents}
    return render(request, 'myApp/search.html', params)
