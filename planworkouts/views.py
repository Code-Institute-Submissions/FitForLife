from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from plans.models import Plan
from workouts.models import Workout
from .models import PlanWorkout


# Create your views here.


def all_planworkouts(request):
    """ A view to show all planworkouts, including sorting and search queries """

    planworkouts = PlanWorkout.objects.all()
    query = None

    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                planworkouts = planworkouts.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            planworkouts = planworkouts.order_by(sortkey)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               ("You didn't enter any search criteria!"))
                return redirect(reverse('planworkouts'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            planworkouts = planworkouts.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'planworkouts': planworkouts,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'planworkouts/planworkouts.html', context)


def planworkout_detail(request, planworkout_id):
    """ A view to show individual planworkouts details """

    planworkout = get_object_or_404(PlanWorkout, pk=planworkout_id)

    context = {
        'planworkout': planworkout,
    }

    return render(request, 'planworkouts/planworkout_detail.html', context)







