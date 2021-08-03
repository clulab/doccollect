from django.forms import ModelForm, Textarea
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from .models import Document, Attribute
from .custom_layout_object import Formset

class DocumentForm(ModelForm):
    class Meta:
        model = Document
        exclude = ['text']

    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('title'),
                Field('file'),
                Fieldset('add attributes', Formset('attributes')),
                HTML('<br>'),
                ButtonHolder(Submit('submit', 'submit'))
            )
        )

class AttributeForm(ModelForm):
    class Meta:
        model = Attribute
        exclude = []
        widgets = {
            'value': Textarea(attrs={'rows': 1, 'cols': 30})
        }

AttributeFormSet = inlineformset_factory(
    Document, Attribute, form=AttributeForm,
    fields=['name', 'value'], extra=1, can_delete=True,
)
