from django.urls import path
from mypersonals.views import index, logshome

app_name = "mypersonals"

urlpatterns = [
    path("", view=index, name="index"),
    # logs
    path("logs", view=logshome, name="logshome"),
]
