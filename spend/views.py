from django.db.models import (
    Sum,
    OuterRef,
    Subquery,
    DecimalField,
)
from django.db.models.functions import Coalesce
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from revenue.models import RevenueStatistic
from spend.models import SpendStatistic


class SpendListView(APIView):
    def get(self, request):
        revenue_subquery = (
            RevenueStatistic.objects.filter(spend=OuterRef("pk"))
            .values("spend")
            .annotate(sum_revenue=Sum("revenue"))
            .values("sum_revenue")
        )

        queryset = (
            SpendStatistic.objects.values("date", "name")
            .annotate(
                sum_spend=Sum("spend"),
                sum_impressions=Sum("impressions"),
                sum_clicks=Sum("clicks"),
                sum_conversion=Sum("conversion"),
                sum_revenue=Coalesce(
                    Sum(Subquery(revenue_subquery)), 0, output_field=DecimalField()
                ),
            )
            .order_by("date", "name")
        )

        return JsonResponse(list(queryset), safe=False)
