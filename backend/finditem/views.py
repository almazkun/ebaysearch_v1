from django.shortcuts import render

from .findItemByKeywords import api_request, to_text, to_json_development


def homepageview(request):

    # if "keywords" in request.GET:
    #    found_items = to_json(to_text(api_request(request.GET["keywords"])))

    # For development only, not to make to many calls to the ebay_api
    if "keywords" in request.GET:
        found_items = to_json_development(to_text(api_request(request.GET["keywords"])))

    return render(request, "home.html", {"found_items": found_items})
