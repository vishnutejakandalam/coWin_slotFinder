import requests
import json

"""This code can be used to send a request to coWin API and get the details of availabe vaccine slots for given date at given pin code cneters."""

"""Just add all the required pincodes to pincodes list and all the dates to dates list below. This code will parse through al the given dates with all the given pincodes. """

""" To get complete information about a specific center set the center_id variable to a center_id (as int itself)"""

pincodes = ["110001"]
dates = ['1-06-2021']
center_id = 702998

for p in pincodes:
    for d in dates:
        params = {'pincode':p,
                    'date': d
        }
        rep = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin", params = params)
        response = rep.json()
        for key,item in response.items():
            for k in item:
                if center_id == None:
                    id = k["center_id"]
                    name = k["name"]
                    address = k["address"]
                    if k["available_capacity_dose1"] == 0:
                        print("no dose 1 at", name, address)
                    else:
                        print("dose 1 available at id",id,name, address,"available:",k["available_capacity_dose1"], sep=",")
                    if k["available_capacity_dose2"] == 0:
                        print("no dose 2 at", name, address)
                    else:
                        print("dose 2 available at id:",id,name, address,"available:", k["available_capacity_dose2"],sep = ",")
                elif center_id == k["center_id"]:
                    for e,i in k.items():
                        print(e," : ",i)