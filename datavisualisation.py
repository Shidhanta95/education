import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from datapreprocessing import dataPrepocessing
import numpy as np


def dataVisuals():
    df = dataPrepocessing()

    # numerical features
    numerical_features = [
    features for features in df.columns if df[features].dtype != 'O']

    # discrete features
    discrete_features = [features for features in numerical_features if len(
        df[features].unique()) <= 12]


    print(len(discrete_features))
    print(discrete_features)
    print(df[discrete_features].head())

    sns.heatmap(df[numerical_features].corr(), cmap='crest',annot = True, fmt='.1g')
    plt.show()


    # finding relationship between discrete variables and G3

    # for features in discrete_features:
    #     data = df.copy()
    #     data.groupby(features)['G3'].median().plot                                                                                                                                                                                                                                                                                                                                                                                                          .bar()
    #     plt.xlabel(features)
    #     plt.ylabel('G3')
    #     plt.title(features)
    #     plt.show()


    # continous features
    continous_features = [
        features for features in numerical_features if features not in discrete_features]

    # fig, axes = plt.subplots(1, len(discrete_features))
    for i,feature in enumerate(discrete_features):
        sns.boxplot( data=df,x=feature, y='G3', orient='v')
        plt.show()

    # plotting features to find relaion

    for i,features in enumerate(continous_features):
        data = df.copy()
        data[features].hist(bins=25)
        plt.xlabel(features)
        plt.ylabel("count")
        plt.title(features)
        plt.show()

    
dataVisuals()