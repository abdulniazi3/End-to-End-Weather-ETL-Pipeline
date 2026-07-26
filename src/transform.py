import pandas as pd


def clean_weather(data):

    row = {

        "city":data["name"],

        "temperature":
        data["main"]["temp"],

        "humidity":
        data["main"]["humidity"],

        "condition":
        data["weather"][0]["description"]

    }


    df=pd.DataFrame([row])


    return df