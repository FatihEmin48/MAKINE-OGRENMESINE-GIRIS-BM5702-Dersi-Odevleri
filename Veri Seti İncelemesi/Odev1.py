# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 14:41:22 2024

@author: fatih
"""


#1. kutuphane
import pandas as pd

#2. Veri Onisleme
data = pd.read_excel('VeriOnIsleme.xlsx')
print("Veri seti:\n")
print(data)

#3 Veri setinin ilk birkaç satırını göster
print("\nVeri setinin ilk birkaç satırı:")
print(data.head())

#4 Veri setinin temel istatistiksel bilgilerini al
print("\nVeri setinin temel istatistikleri:")
print(data.describe())

#5 Veri setindeki eksik değerleri kontrol et
print("\nEksik değerlerin sayısı:")
print(data.isnull().sum())














