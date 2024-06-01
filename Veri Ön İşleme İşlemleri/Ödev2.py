# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 20:58:09 2024

@author: fatih
"""


#1.kutuphaneler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#2. Veri Ön işleme
#2.1 veri yükleme
veriler = pd.read_excel('EnergyStarScore.xlsx')
print(veriler)


#Eksik verileri düzeltme
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

sayısal = veriler.iloc[:,2:8].values
imputer = imputer.fit(sayısal[:,2:8])
sayısal[:,2:8] = imputer.transform(sayısal[:,2:8])
print(sayısal)



#Encoder (Nominal Ordinal) -> Numeric
#Veri dönüşümü
binaAdı = veriler.iloc[:,1:2].values
print(binaAdı)

from sklearn import preprocessing

le = preprocessing.LabelEncoder()

binaAdı[:,0] = le.fit_transform(veriler.iloc[:,0])
ohe = preprocessing.OneHotEncoder()
binaAdı = ohe.fit_transform(binaAdı).toarray()
print(binaAdı)


