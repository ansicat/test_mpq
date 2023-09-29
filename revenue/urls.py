from django.urls import path

from revenue.views import RevenueListView

urlpatterns = [
    path("", RevenueListView.as_view(), name="revenue-list")
]

app_name = "revenue"
