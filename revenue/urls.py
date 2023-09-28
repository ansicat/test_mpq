from django.urls import path

from revenue.views import revenue_list

urlpatterns = [
    path("", revenue_list, name="revenue-list")
]

app_name = "revenue"
