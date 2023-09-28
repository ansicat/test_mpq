from django.db.models import Sum
from django.http import JsonResponse
from rest_framework.decorators import api_view

from revenue.models import RevenueStatistic


@api_view(["GET"])
def revenue_list(request):
    queryset = (
        RevenueStatistic.objects.values("date", "name")
        .annotate(
            sum_revenue=Sum("revenue"),
            sum_spend=Sum("spend__spend"),
            sum_impressions=Sum("spend__impressions"),
            sum_clicks=Sum("spend__clicks"),
            sum_conversion=Sum("spend__conversion"),
        )
        .order_by("date", "name")
    )

    return JsonResponse(list(queryset), safe=False)
