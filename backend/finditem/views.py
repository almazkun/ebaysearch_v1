from django.shortcuts import render
from django.http import HttpResponse


from .findItemByKeywords import api_request, to_json, json_items, in_json_items


def homepageview(request):
    found_items = None

    if "keywords" in request.GET:
        found_items = json_items(to_json(api_request(request.GET["keywords"])))

    return render(request, "home.html", {"found_items": found_items})


def keywordSearchView(request):
    
    if "keywords" in request.GET:
        response = in_json_items(json_items(to_json(api_request(request.GET["keywords"]))))

        return HttpResponse(response, content_type='application/json')