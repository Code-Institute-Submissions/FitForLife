from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from plans.models import Plan
from scorecards.models import Scorecard
from .models import Scorecard


# Create your views here.


def all_scorecards(request):
    """ A view to show all scorecards, including sorting and search queries """

    scorecards = Scorecard.objects.all()
    query = None

    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                scorecards = scorecards.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            scorecards = scorecards.order_by(sortkey)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request,
                               ("You didn't enter any search criteria!"))
                return redirect(reverse('scorecards'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            scorecards = scorecards.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'scorecards': scorecards,
        'search_term': query,
        'current_sorting': current_sorting,
    }

    return render(request, 'scorecards/scorecards.html', context)










