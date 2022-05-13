# -*- coding: utf-8 -*-
"""
Created on Fri May 13 10:16:34 2022

@author: samrit
"""

import matplotlib.pyplot as plt


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