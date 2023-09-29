from django.urls import path

from spend.views import SpendListView

urlpatterns = [
    path("", SpendListView.as_view(), name="spend-list")
]

app_name = "spend"
