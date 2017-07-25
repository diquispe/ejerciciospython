from urllib.request import urlopen
import json

def manipularJSON(data):

    JSON = json.loads(data)
    #if "title" in JSON["metadata"]:
    #    print(JSON["metadata"]["title"])

    #numeroterremotos = JSON["metadata"]["count"]


    #print("El numero de terremotos es: %s" % numeroterremotos)


    # for i in JSON["features"]:
    #     print(i["properties"]["mag"])

    # for i in JSON["features"]:
    #     if i["properties"]["mag"] >= 4:
    #         print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])

    print("============================================")

    for i in JSON["features"]:
        cantidaddepersonas = i["properties"]["felt"]
        if cantidaddepersonas != None and cantidaddepersonas > 2:
            print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])
            print(cantidaddepersonas)
    pass

def main():

    url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    response = urlopen(url)

    if response.getcode() == 200:
        manipularJSON(response.read())


    pass

if __name__ == '__main__':
    main()
