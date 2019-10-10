from django.shortcuts import render

from .findItemByKeywords import api_request, to_json, json_items
from .findItemByKeywords import to_json_development


def homepageview(request):
    found_items = None

    if "keywords" in request.GET:
        found_items = json_items(to_json(api_request(request.GET["keywords"])))

    return render(request, "home.html", {"found_items": found_items})


def devview(request):
    found_items = None

    if "keywords" in request.GET:
        found_items = json_items()

    return render(request, "dev.html", {"found_items": found_items})
