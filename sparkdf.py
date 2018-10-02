# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 20:21:28 2018

@author: Pc
"""


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns
import matplotlib.pyplot as plt


# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list the files in the input directory



# Read datas
data = pd.read_csv('statesPopulation.csv', encoding="windows-1252")
data.head()
data.info()
data.Population.value_counts()

data['State'].value_counts()
'''
sns.countplot(x=data['State'],data=d,palette='hls')
plt.show()
plt.savefig('yes-no sayisi')'''
data['State'].unique()
len(data['State'].unique())

state_list = list(data['State'].unique())
state_popu = []
for i in state_list :
    x = data[data['State']==i]
    state_populasyon = sum(x.Population)
    state_popu.append(state_populasyon)
data2 = pd.DataFrame({'eyletler':state_list ,'toplam populasyon':state_popu})


'''
new_index = (data2['state_popu'].sort_values(ascending=False)).index.values
sorted_data = data.reindex(new_index)

# visualization
plt.figure(figsize=(15,10))
sns.barplot(x=sorted_data['state_list'], y=sorted_data['state_popu'])
plt.xticks(rotation= 45)
plt.xlabel('Bölgeler')
plt.ylabel('Populasyon')
plt.title('Bölgelere göre populasyon')'''


data['Year'].unique()

data2010= data[data.Year==2010]
state_list_2010 = list(data['State'].unique())
state_popu_2010 = []
for i in state_list_2010 :
    x = data2010[data2010['State']==i]
    state_populasyon_2010 = sum(x.Population)
    state_popu_2010.append(state_populasyon_2010)
data_2010 = pd.DataFrame({'eyletler':state_list_2010 ,'toplam_populasyon':state_popu_2010})


data2014=data[data.Year==2014]
state_list_2014= list(data['State'].unique())
state_popu_2014 = []
for i in state_list_2014:
    x = data2014[data2014['State']==i]
    state_populasyon_2014 = sum(x.Population)
    state_popu_2014.append(state_populasyon_2014)
data_2014 = pd.DataFrame({'eyletler':state_list_2014 ,'toplam_populasyon':state_popu_2014})

s1=data_2014['toplam_populasyon']
s2=data_2010['toplam_populasyon']
s3=s1-s2

sondata=data_2014.iloc[:,0:1]
r =pd.Series.to_frame(s3)
son_son =pd.concat([sondata,r],axis=1)
son_son.sort_values(by=['toplam_populasyon'], ascending=False).head(3)
