from django.urls import path
from myfinances.views import index, expensehome, addexpense, incomeshome, addincome

app_name = "myfinances"

urlpatterns = [
    path("", view=index, name="index"),
    # expenses
    path("expensehome", view=expensehome, name="expensehome"),
    path("addexpense", view=addexpense, name="addexpense"),
    # incomes
    path("incomeshome", view=incomeshome, name="incomeshome"),
    path("addincome", view=addincome, name="addincome"),
]
