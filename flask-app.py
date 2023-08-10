# A very simple Flask Hello World app for you to get started with...

from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route('/')
def home():
    return '<h2>CSC 221 - Final Challenge<h2> <p>23984215<br />Leon Belegu</p>'

@app.route('/id')
def info():
    return '23984215_Belegu'

@app.route('/hot_and_new/<zipcode>')
def hotandnew(zipcode):
    url = "https://api.yelp.com/v3/businesses/search?location=" + str(zipcode) + "&radius=5000&attributes=hot_and_new&sort_by=best_match&limit=10"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer 2-aNvKrC3GzYdgaXiL9l4ssiPyjcLuGTnxkuOLdq_P7-OtdJeyVelKEplVRnJMldxtny-m4NP_Toscq8Ppoaq1Icr5gpyht2A3n6iWxtk4v9IgP-ehanBQZ3YlpJZHYx"
    }

    r = requests.get(url, headers=headers)
    response = r.json()
    output = []

    # for each business in businesses, get its name, url, location, distance (in miles), categories, location, phone
    for business in response['businesses']:
        # making a dictonarry to store info for each busniess
        info = {"categories":[], "distance":[], "location":[], "name":[],"phone":[],"url":[]}

        # adding in all the info for each busniess:

        # for loop to extract all titles from categories
        for title in business['categories']:
            info["categories"].append(title['title'])

        info["distance"].append(round(business['distance']*0.00062137,1))
        info["location"].append(business['location']['display_address'])
        info["name"].append(business['name'])
        info["phone"].append(business['display_phone'])
        info["url"].append(business['url'])
        output.append(info)

    # must return a string, using json.dumps to turn our output into a string
    return json.dumps(output, sort_keys=True)

@app.route('/hot_and_new_html/<zipcode>')
def hotandnewHTML(zipcode):
    url = "https://api.yelp.com/v3/businesses/search?location=" + str(zipcode) + "&radius=5000&attributes=hot_and_new&sort_by=best_match&limit=10"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer 2-aNvKrC3GzYdgaXiL9l4ssiPyjcLuGTnxkuOLdq_P7-OtdJeyVelKEplVRnJMldxtny-m4NP_Toscq8Ppoaq1Icr5gpyht2A3n6iWxtk4v9IgP-ehanBQZ3YlpJZHYx"
    }

    r = requests.get(url, headers=headers)
    response = r.json()
    output = []

    # for each business in businesses, get its name, url, location, distance (in miles), categories, location, phone
    for business in response['businesses']:
        # making a dictonarry to store info for each busniess
        info = {"categories":[], "distance":[], "location":[], "name":[],"phone":[],"url":[]}

        # adding in all the info for each busniess:

        # for loop to extract all titles from categories
        for title in business['categories']:
            info["categories"].append(title['title'])

        info["distance"].append(round(business['distance']*0.00062137,1))
        info["location"].append(business['location']['display_address'])
        info["name"].append(business['name'])
        if(len(business['display_phone']) > 1):
            info["phone"].append(business['display_phone'])
        info["url"].append(business['url'])
        output.append(info)

    html = "<h2>New and Hot businesses near {zipcode}</h2>".format(zipcode=zipcode)

    for restaurant in output:
        name = " ".join(restaurant["name"])
        distance = restaurant["distance"][0]
        categories = "/".join(restaurant["categories"])

        address1 = ""
        for i in range(0,len(restaurant["location"][0])):
            address1 += restaurant["location"][0][i] + "<br>"
        address1 = address1[:-2]

        phone = " ".join(restaurant["phone"])
        url = " ".join(restaurant["url"])

        html += '<link rel="stylesheet" href="https://ssl.gstatic.com/docs/script/css/add-ons1.css">'
        html += "<h3><a href='{url}'>{name}</a> ({distance} miles away)</h3>".format(url=url, name=name, distance=distance)
        html += "<b>{categories}</b><br>{address1}</br><br>{phone}</br>".format(categories=categories, address1=address1, phone=phone)

    return html




