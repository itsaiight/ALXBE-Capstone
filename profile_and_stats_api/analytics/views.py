from django.shortcuts import render, get_object_or_404
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from core.models import Driver, Result
from django.db.models import Sum
# Create your views here.
"""GET /api/drivers/:id/stats/
GET /api/drivers/:id/circuits/ might drop this
GET /api/drivers/:id/seasons/ might drop this
GET /api/comparison/?a=hamilton&b=alonso
GET /api/analytics/fastest-driver/
"""
class DriverStatsView(GenericAPIView):
       def get(self, request, driver_id):
        driver = get_object_or_404(Driver, pk=Driver.driver_id)

        qs = Result.objects.filter(driver=driver)
        total_starts = qs.count()
        wins = qs.filter(position=1).count()
        points = qs.aggregate(Sum("points"))["points__sum"] or 0

        return Response({
           "driver": driver.full_name,
           "starts": total_starts,
           "wins": wins,
           "points": points,
       })

class DriverComparisonsView(GenericAPIView):
        def get(self, request):
        # Get query parameters
            driver_a_id = request.query_params.get("a")
            driver_b_id = request.query_params.get("b")

            if not driver_a_id or not driver_b_id:
                return Response({"error": "Please provide 'a' and 'b' query params"}, status=400)

            driver_a = get_object_or_404(Driver, pk=driver_a_id)
            driver_b = get_object_or_404(Driver, pk=driver_b_id)

            # Query results for both drivers in the season
            results_a = Result.objects.filter(driver=driver_a)
            results_b = Result.objects.filter(driver=driver_b)

            # Aggregate stats
            stats_a = {
                "wins": results_a.filter(position=1).count(),
                "podiums": results_a.filter(position__lte=3).count(),
                "points": results_a.aggregate(Sum("points"))["points__sum"] or 0,
            }

            stats_b = {
                "wins": results_b.filter(position=1).count(),
                "podiums": results_b.filter(position__lte=3).count(),
                "points": results_b.aggregate(Sum("points"))["points__sum"] or 0,
            }

            # Head-to-head (same races, compare finishing positions)
            shared_races = results_a.values_list("race_id", flat=True).intersection(
                results_b.values_list("race_id", flat=True)
            )
            a_wins = 0
            b_wins = 0
            for race_id in shared_races:
                pos_a = results_a.get(race_id=race_id).position
                pos_b = results_b.get(race_id=race_id).position
                if pos_a < pos_b:
                    a_wins += 1
                elif pos_b < pos_a:
                    b_wins += 1

            return Response({
                driver_a.last_name.lower(): stats_a,
                driver_b.last_name.lower(): stats_b,
                "head_to_head": {
                    "races": len(shared_races),
                    "a_wins": a_wins,
                    "b_wins": b_wins,
                }
            })

