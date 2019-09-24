from django.shortcuts import render
import requests, json

from ebay_api_auth_keys_secret import security_appname


def homepageview(request):
    to_json = {}

    ebay_conf = {
        "SECURITY-APPNAME": security_appname,
        "OPERATION-NAME": "findItemsByKeywords",
        "SERVICE-VERSION": "1.0.0",
        "RESPONSE-DATA-FORMAT": "JSON",
        "callback": "_cb_findItemsByKeywords",
        "REST-PAYLOAD": "REST-PAYLOAD",
        "keywords": "",
        "paginationInput": 10,
        "GLOBAL-ID": "EBAY-US",
        "siteid": "0",
    }
    
    if "keywords" in request.GET:
        ebay_conf.update({"keywords": request.GET["keywords"]})
        url = "https://svcs.ebay.com/services/search/FindingService/v1?SECURITY-APPNAME={SECURITY-APPNAME}&OPERATION-NAME={OPERATION-NAME}&SERVICE-VERSION={SERVICE-VERSION}&RESPONSE-DATA-FORMAT={RESPONSE-DATA-FORMAT}&callback={callback}&REST-PAYLOAD&keywords={keywords}&paginationInput.entriesPerPage={paginationInput}&GLOBAL-ID={GLOBAL-ID}&siteid={siteid}".format(**ebay_conf)
        response = requests.get(url)
        to_text = response.text[28:-1]
        to_json = json.loads(to_text)
    return render(request, "home.html", {"to_json": to_json})
