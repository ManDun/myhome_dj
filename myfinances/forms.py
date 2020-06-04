from myfinances.models import Expenses, Files
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field, Div

class DateInput(forms.DateInput):
    input_type = 'date'

class ExpenseForm(forms.ModelForm):

    bill = forms.FileField()

    class Meta:
        model = Expenses
        widgets = {
            'date_of_expense': DateInput,
            'details': forms.Textarea(attrs={'rows':3})
        }
        fields = ['name', 'type', 'amount', 'details', 'date_of_expense']

class SearchExpenseForm(forms.Form):

    freq_choices = (('daily', 'Daily'), ('monthly', 'Monthly'), ('yearly', 'Yearly'))
    frequency = forms.ChoiceField(choices=freq_choices)
    date = forms.DateField(widget=DateInput)

    FormHelper.layout = Layout(
        Field('frequency', css_class="custom-select btn-secondary"),
        Field('date', css_class="form-control")
    )

    FormHelper.layout = Layout(
    Div(
        Field('name'), css_class="my_fancy_class_name"
    ),
    Field('description'),
)
