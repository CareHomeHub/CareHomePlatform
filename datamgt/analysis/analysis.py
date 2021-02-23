import pandas as pd

df = pd.read_csv("location_rating.csv")
print(df)

cont = df.groupby('RATING').count()
print(cont)

cont = df.groupby('POSTCODE').count()
print(cont)


cont = df.groupby([ 'POSTCODE','RATING'])['RATING'].count()
print(cont)
cont = df.groupby([ 'RATING', 'POSTCODE'])['RATING'].count()
print(cont)

