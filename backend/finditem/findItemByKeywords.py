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
        "paginationInput": 1,
        "GLOBAL-ID": "EBAY-US",
        "siteid": "0",
        "topRatedListing": "true",
        "Condition": "New",
    }
    url = "https://svcs.ebay.com/services/search/FindingService/v1?SECURITY-APPNAME={SECURITY-APPNAME}&OPERATION-NAME={OPERATION-NAME}&SERVICE-VERSION={SERVICE-VERSION}&RESPONSE-DATA-FORMAT={RESPONSE-DATA-FORMAT}&REST-PAYLOAD&keywords={keywords}&paginationInput.entriesPerPage={paginationInput}&GLOBAL-ID={GLOBAL-ID}&siteid={siteid}&topRatedListing={topRatedListing}&itemFilter(0).name=Condition&itemFilter(0).value={Condition}".format(
        **ebay_conf
    )

    return requests.get(url)


def to_json(response):
    return response.json()


def json_items(to_json):
    items = []

    a = to_json["findItemsByKeywordsResponse"][0]

    if "searchResult" in a:
        for item in a["searchResult"][0]["item"]:
            i = dict()
            i["title"] = item.get("title")[0]
            i["price"] = item["sellingStatus"][0]["currentPrice"][0]["__value__"]
            i["pic_url"] = item["galleryURL"][0]
            i["ebay_url"] = item["viewItemURL"][0]
            i["condition"] = item["condition"][0]["conditionDisplayName"][0]
            items.append(i)
    else:
        return ["Please try again"]

    return items
