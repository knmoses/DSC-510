#File: MosesKrystina 12, Final Project
#Name: Krystina Moses
#Date: June 2019 // Week 12
#Course: Intro to Programming

import json
import requests
from requests.exceptions import HTTPError
from pprint import pprint

#General api information
api_token = '4b23db9d32cc6cab99868a89e4c8a974'
api_url_base = "http://api.openweathermap.org/data/2.5/weather?"
unit = 'imperial'

def welcome():
    #Welcome message to user
    print('Hello, Welcome to the Weather Information Center!')
    mainweather()

def mainweather():
    #Run program
    weatherfunction()

def weathercity():
    #Prompt user to enter in a city
    c = input('Please enter a US city.\n')

    #Get data from webservice
    c_url = api_url_base + "appid=" + api_token + "&q=" + c + "&units=" + unit
    c_data = requests.get(c_url).json()

    try:
        cd = requests.get(c_url)
        cd.raise_for_status()
    except Exception as err:
        print('Error occurred: {err}')
    else:
        print('Connection Successful\n')

    try:
            #Retrieve data
            ccity = c_data['name']
            cid = c_data['id']
            ctemp = c_data['main']['temp']
            cmintemp = c_data['main']['temp_min']
            cmaxtemp = c_data['main']['temp_max']
            cpres = c_data['main']['pressure']
            chumid = c_data['main']['humidity']
            cwmain = c_data['weather'][0]['main']
            cdescrip = c_data['weather'][0]['description']
            cwind = c_data['wind']['speed']
            cclouds = c_data['clouds']['all']

            #print("\nWeather for " + c +":\n")
            #pprint(c_data)

            #Print in a readable format
            print("\nCity: {}".format(ccity))
            print("\nCity ID: {}".format(cid))
            print("\nTemperature, in fahrenheit: {}".format(ctemp))
            print("\nMin Temperature, in fahrenheit: {}".format(cmintemp))
            print("\nMax Temperature, in fahrenheit: {}".format(cmaxtemp))
            print("\nPressure, hPa: {}".format(cpres))
            print("\nPercentage of Humidity: {}".format(chumid))
            print("\nWeather parameters: {}".format(cwmain))
            print("\nDescription: {}".format(cdescrip))
            print("\nWind Speed, in miles/hour: {}".format(cwind))
            print("\nPercentage of Cloud Coverage: {}".format(cclouds))
            mainweather()
    #Catch error
    except requests.exceptions.RequestException as e:
        print (e)
        sys.exit(1)

def weatherzc():
    #Prompt user to enter in a zip code
    zc = input('Please enter a zip code.\n')

    zc_url = api_url_base + "appid=" + api_token + "&zip=" + zc + "&units=" + unit
    zc_data = requests.get(zc_url).json()

    try:
        zcd = requests.get(zc_url)
        zcd.raise_for_status()
    except Exception as err:
        print('Error occurred: {err}')
    else:
        print('Connection Successful\n')

    #Get data from webservice
    try:
        #Retrieve data
        zccity = zc_data['name']
        zcid = zc_data['id']
        zctemp = zc_data['main']['temp']
        zcmintemp = zc_data['main']['temp_min']
        zcmaxtemp = zc_data['main']['temp_max']
        zcpres = zc_data['main']['pressure']
        zchumid = zc_data['main']['humidity']
        zcwmain = zc_data['weather'][0]['main']
        zcdescrip = zc_data['weather'][0]['description']
        zcwind = zc_data['wind']['speed']
        zcclouds = zc_data['clouds']['all']

        #print("\nWeather for " + c +":\n")
        #pprint(c_data)

        #print in a readable format
        print("\nCity: {}".format(zccity))
        print("\nCity ID: {}".format(zcid))
        print("\nTemperature, in fahrenheit: {}".format(zctemp))
        print("\nMin Temperature, in fahrenheit: {}".format(zcmintemp))
        print("\nMax Temperature, in fahrenheit: {}".format(zcmaxtemp))
        print("\nPressure, hPa: {}".format(zcpres))
        print("\nPercentage of Humidity: {}".format(zchumid))
        print("\nWeather parameters: {}".format(zcwmain))
        print("\nDescription: {}".format(zcdescrip))
        print("\nWind Speed, in miles/hour: {}".format(zcwind))
        print("\nPercentage of Cloud Coverage: {}".format(zcclouds))
        mainweather()
    #Catch error
    except requests.exceptions.RequestException as e:
        print (e)
        sys.exit(1)

def weatherfunction():
        try:
            #Prompt the user to enter if they would like to search for a city or zip code.
            mw = input('\nTo enter a US city, enter "city", to enter a zip code enter "zip code". To exit, enter "quit"\n')

            if mw == "city":
                weathercity()
            elif mw == "zip code":
                weatherzc()
            elif mw == "quit":
                print('Thank you for visiting!\n')
            else:
                print('Invalid input, please try again\n')
                mainweather()
        except:
            print('That was an invalid response.\n')
            mainweather()

welcome()
