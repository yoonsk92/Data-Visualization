import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.patches as mpatches
from mpl_toolkits.basemap import Basemap
import os

#Geographical Chart
df = pd.read_excel('Data.xlsx')
lats = df['Latitude']
lngs = df['Longitude']      
lvl = df['Impact Level'] + 16
lvls = [p * p for p in lvl]

def f(row):
    if row['Legend'] == 'Initiatives':
        val = 'black'
    elif row['Legend'] == 'Alumni Achievement':
        val = 'orange'
    elif row['Legend'] == 'Chairs/Professorships':
        val = 'blue'
    elif row['Legend'] == 'Faculty Achievement':
        val = 'green'
    else:
        val = 'red'
    return val

df['color_index'] = df.apply(f, axis=1)

def geo_chart(lats = lats, lngs = lngs, lvls = lvls): 
    m = Basemap(projection = 'cyl', lon_0 = 0, resolution = 'c')
    m.drawmapboundary(fill_color = '#85A6D9')
    m.fillcontinents(color = 'white', lake_color = '#85A6D9')
    m.drawcoastlines(color = '#6D5F47', linewidth=.4)
    m.drawcountries(color='#6D5F47', linewidth=.4)
    x,y = m(lngs, lats)
    m.scatter(x,y, s = lvls, c = df['color_index'],
              marker = 'o', alpha = 0.65, zorder = 2)
    
    #Create legend
    init = mpatches.Patch(color = 'black', label = 'Initiatives')
    alum = mpatches.Patch(color = 'orange', label = 'Alumni Achievement')
    CP = mpatches.Patch(color = 'blue', label = 'Chairs/Professorships')
    fac = mpatches.Patch(color = 'green', label = 'Faculty Achievement')
    stud = mpatches.Patch(color = 'red', label = 'Student Achievement')
    plt.legend(handles=[alum,CP,fac,init,stud])
    plt.title('Schulich Global')
    
geo_chart()


#Yearly Chart
alumni_achi = df.loc[df['Legend'] == 'Alumni Achievement']
alumni_achi_1 = alumni_achi.groupby("Year")["Impact Level"].sum()

chairs_profs = df.loc[df['Legend'] == 'Chairs/Professorships']
chairs_profs_1 = chairs_profs.groupby("Year")["Impact Level"].sum()

fac_achi = df.loc[df['Legend'] == 'Faculty Achievement']
fac_achi_1 = fac_achi.groupby("Year")["Impact Level"].sum()

init = df.loc[df['Legend'] == 'Initiatives']
init_1 = init.groupby("Year")["Impact Level"].sum()

stud_achi = df.loc[df['Legend'] == 'Student Achievement']
stud_achi_1 = stud_achi.groupby("Year")["Impact Level"].sum()

def ts_plot():
    plt.plot(alumni_achi_1, color = 'orange', label = 'Alumni Achievement')
    plt.plot(chairs_profs_1, color = 'blue', label = 'Chairs/Professorships')
    plt.plot(fac_achi_1, color = 'green', label = 'Faculty Achievement')
    plt.plot(init_1, color = 'black', label = 'Initiatives')
    plt.plot(stud_achi_1, color = 'red', label = 'Student Achievement')
    plt.legend()
    plt.xlabel('Year')
    plt.ylabel('# of Global Achievements')
    plt.title('Schulich Global Time Series')

ts_plot()







    
