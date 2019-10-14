from django.shortcuts import render

from .findItemByKeywords import api_request, to_json, json_items


def homepageview(request):
    found_items = None

    if "keywords" in request.GET:
        found_items = json_items(to_json(api_request(request.GET["keywords"])))

    return render(request, "home.html", {"found_items": found_items})
