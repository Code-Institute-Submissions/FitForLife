import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@csrf_exempt  
#@require_POST
def webhook(request):
    jsondata = request.body
    # data = json.loads(jsondata)
    # for answer in data['form_response']['answers']: # go through all the answers
    #   type = answer['type']
    print("webhook called") # print value of answers

    return HttpResponse(status=200)