import requests, json

from ebay_api_auth_keys_secret import security_appname


def api_request(keyword):
    ebay_conf = {
        "SECURITY-APPNAME": security_appname,
        "OPERATION-NAME": "findItemsByKeywords",
        "SERVICE-VERSION": "1.0.0",
        "RESPONSE-DATA-FORMAT": "JSON",
        "REST-PAYLOAD": "REST-PAYLOAD",
        "keywords": keyword,
        "paginationInput": 10,
        "GLOBAL-ID": "EBAY-US",
        "siteid": "0",
    }
    url = "https://svcs.ebay.com/services/search/FindingService/v1?SECURITY-APPNAME={SECURITY-APPNAME}&OPERATION-NAME={OPERATION-NAME}&SERVICE-VERSION={SERVICE-VERSION}&RESPONSE-DATA-FORMAT={RESPONSE-DATA-FORMAT}&REST-PAYLOAD&keywords={keywords}&paginationInput.entriesPerPage={paginationInput}&GLOBAL-ID={GLOBAL-ID}&siteid={siteid}".format(
        **ebay_conf
    )

    return requests.get(url)


def to_text(response):
    return response.text


def to_json(text):
    return json.loads(text)


# For development only, not to make to many calls to the ebay_api
def to_json_development():

    with open("response.json", "r") as file:
        found_items = file.read()

    return json.loads(found_items)
