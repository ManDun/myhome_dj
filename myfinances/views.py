from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.http import HttpResponse
from django.utils.translation import ugettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from myfinances import forms
from myfinances.models import Files, Expenses
from django.conf import settings
from django.db.models.functions import ExtractYear, ExtractMonth, ExtractDay
import datetime


def index(request):

    return render(request, 'index.html')


def expensehome(request):

    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    else:
        user_id = request.user.id
        today = datetime.date.today()
        expenses = Expenses.objects.filter(user_id=user_id)

        expenses_filtered = Expenses.objects.filter(user_id=user_id, dateOfExpense = today)

        form = forms.SearchExpenseForm()

        if request.method == 'POST':
            form = forms.SearchExpenseForm(request.POST)

            if form.is_valid():
                print('POST in expensehome')
                frequency = form.cleaned_data['frequency']
                selecteddate = form.cleaned_data['date']
                print(f'Frequency selected: {frequency}')
                print(f'Date selected: {selecteddate}')
                print(request.user.id)
                today = datetime.date.today()    

                if frequency in 'yearly':
                    expenses_filtered = expenses.filter(Expenses.dateOfExpense.year == selecteddate.year)
                elif frequency in 'monthly':
                    expenses_filtered = expenses.filter(Expenses.dateOfExpense.month == selecteddate.month)
                elif frequency in 'daily':
                    expenses_filtered = expenses.query.filter(ExtractDay(Expenses.dateOfExpense) == selecteddate.day).all()
                else:
                    expenses_filtered = expenses.filter(Expenses.dateOfExpense == today)

        return render(request, 'expenses/expenseshome.html', {'form': form, 'expenses': expenses_filtered})


def addexpense(request):

    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    else:
        today = datetime.date.today()
        user_id = request.user.id
        expenses = Expenses.objects.filter(user_id = user_id, dateOfExpense = today)

        form = forms.ExpenseForm()

        if request.method == 'POST':
            form = forms.ExpenseForm(request.POST, request.FILES)

            if form.is_valid():
                print('POST')
                print(form.cleaned_data['name'])
                Files.name = request.FILES['bill']
                form.instance.user = request.user
                form.save(commit=True)
                print(request.FILES['bill'])

        return render(request, 'expenses/addexpense.html', {'form': form, 'expenses': expenses})


# def deleteexpense(request, expense_id):

#     if not request.user.is_authenticated:
#         print('User tried accessing financials.delete and not authorized')
#         return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

#     else:
#         print(f'User authenticated {request.user.username} and accessed delete in expenses')
#         print(f'Deleting expense id {expense_id}')
#         expense = Expenses.query.get_or_404(expense_id)
#         db.session.delete(expense)
#         if files:
#             print(f'File {files.name} attached to expense, deleting it')
#             db.session.delete(files)
#         db.session.commit()

#         return redirect(request.referrer)


def incomeshome(request):

    return render(request, 'incomes/incomeshome.html')


def addincome(request):

    return render(request, 'incomes/addincome.html')

# Create your views here.
