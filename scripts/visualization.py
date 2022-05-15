# -*- coding: utf-8 -*-
"""
Created on Fri May 13 10:16:34 2022

@author: samrit
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import plotly.express as px



def plot_univariate(df, col1, col2):
    plt.figure(figsize = (12, 8))

    plt.subplot(2, 2, 1)
    plt.hist(df[col1], bins = 20, color = 'lavender', edgecolor = 'gray', linewidth = 0.5)
    plt.title(f'Histogram of {col1}', size=14)

    plt.subplot(2, 2, 2)
    plt.boxplot(df[col1])
    plt.title(f'Boxplot of {col1}', size=14)

    plt.subplot(2, 2, 3)
    plt.hist(df[col2], bins=20, color='lavender', edgecolor='gray', linewidth=0.5)
    plt.title(f'Histogram of {col2}', size=14)
    
    
    plt.subplot(2, 2, 4)
    plt.boxplot(df[col2])
    plt.title(f'Boxplot of {col2}', size=14)

    plt.show()
    
def hist(sr):
    x = ["Id: " + str(i) for i in sr.index]
    fig = px.histogram(x=x, y=sr.values)
    fig.show()
   

def plot_scatter(df: pd.DataFrame, x_col: str, y_col:str, title: str) -> None:
    plt.figure(figsize=(12, 7))
    sns.scatterplot(data = df, x=x_col, y=y_col)
    plt.title(title, size=20)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.show()

def plot_heatmap(df:pd.DataFrame, title:str, cmap='Reds')->None:
    plt.figure(figsize=(12,7))
    sns.heatmap(df, annot=True, cmap=cmap, vmin=0, vmax=1, fmt='.2f', linewidths=.7, cbar=True )
    plt.title(title, size=20, fontweight='bold')
    plt.show()