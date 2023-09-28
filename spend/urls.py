from django.urls import path

from spend.views import spend_list

urlpatterns = [
    path("", spend_list, name="spend-list")
]

app_name = "spend"
