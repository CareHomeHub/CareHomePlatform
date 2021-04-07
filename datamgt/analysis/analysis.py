"""  analysis.py
"""
import pandas as pd

df = pd.read_csv("location_rating.csv")
cont = df.groupby('RATING').count()
print(cont)
cont1 = df.groupby('POSTCODE').count()
print(cont1)
cont2 = df.groupby([ 'POSTCODE','RATING'])['RATING'].count()
print(cont2)
cont3 = df.groupby([ 'RATING', 'POSTCODE'])['RATING'].count()
print(cont3)
