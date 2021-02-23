import pandas as pd
import pygal

df = pd.read_csv("../datasource/Latest_ratings_2_2021_Loc.csv")
# # print(df)

cant = df.loc[df['LocationLocalAuthority']=='Cornwall']
# cont = df.groupby(['Domain'])['LatestRating'].count()
# print(cont)
# cont = df.groupby(['Domain','LatestRating'])['LatestRating'].count()
cont = cant.groupby(['Domain','LatestRating'])['LatestRating'].count()
print(cont)
# cont.to_json(r'short_1_df.json')


# cont = df.groupby([ 'LocationLocalAuthority', 'Domain'])['LatestRating'].count()
# print(cont)
# # df.to_json(r'short_2_df.json')


# print("\n---------------------------------\n")


# cont = df[["LocationID", "LocationName", "LocationPrimaryInspectionCategory", "LocationPostCode"]].loc[df['Domain'] == 'Overall']
# print(cont)
# # df.to_json(r'short_df.json')


# line_chart = pygal.Bar()
# line_chart.title = 'Browser usage evolution (in %)'
# line_chart.x_labels = map(str, range(2002, 2013))
# line_chart.add('Firefox', [None, None, 0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
# line_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
# line_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
# line_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
# line_chart.render_to_file('line_chart.svg') 


# new_df = df.groupby('Domain','LatestRating')['LatestRating'].counts()

bar_chart = pygal.Bar(width=1000, height=600,
                            legend_at_bottom=True, human_readable=True,
                            title='versions vs colors',
                            x_title='Domain',
                            y_title='Number')
versions = []    

for index, row in cont.iteritems():
    versions.append(index[0])
    bar_chart.add(index[1], row)

bar_chart.x_labels = map(str, versions)

bar_chart.render_to_file('bar-chart.svg')