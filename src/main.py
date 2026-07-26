from extract import get_weather
from transform import clean_weather
from load import load


data=get_weather()

df=clean_weather(data)

load(df)


print("ETL Completed")