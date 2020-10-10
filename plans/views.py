from django.shortcuts import render, get_object_or_404
from .models import Plan

# Create your views here.

def all_plans(request):
    """ A view to show all plans, including sorting and search queries """

    plans = Plan.objects.all()

    context = {
        'plans': plans,
    }

    return render(request, 'plans/plans.html', context)


def plan_detail(request, plan_id):
    """ A view to show individual plan details """

    plan = get_object_or_404(Plan, pk=plan_id)

    context = {
        'plan': plan,
    }

    return render(request, 'plans/plan_detail.html', context)