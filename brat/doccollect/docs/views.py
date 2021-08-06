from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse, reverse_lazy
from django.db import transaction
from .models import Document
from .forms import DocumentForm, AttributeFormSet
from .read_pdf import extract_text

class DocumentView(generic.DetailView):
    model = Document
    template_name = 'docs/document_detail.html'

class DocumentListView(generic.ListView):
    model = Document
    template_name = 'docs/document_list.html'

class DocumentCreateView(CreateView):
    model = Document
    template_name = 'docs/document_create.html'
    form_class = DocumentForm

    def get_success_url(self):
        return reverse_lazy('view_doc', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['attributes'] = AttributeFormSet(self.request.POST)
        else:
            data['attributes'] = AttributeFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        attributes = context['attributes']
        with transaction.atomic():
            self.object = form.save()
            self.object.text = extract_text(self.object.file.path)
            if attributes.is_valid():
                attributes.instance = self.object
                attributes.save()
        return super().form_valid(form)

class DocumentUpdateView(UpdateView):
    model = Document
    template_name = 'docs/document_create.html'
    form_class = DocumentForm

    def get_success_url(self):
        return reverse_lazy('view_doc', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data['attributes'] = AttributeFormSet(self.request.POST, instance=self.object)
        else:
            data['attributes'] = AttributeFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        attributes = context['attributes']
        with transaction.atomic():
            self.object = form.save()
            if attributes.is_valid():
                attributes.instance = self.object
                attributes.save()
        return super().form_valid(form)
