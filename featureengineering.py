import pandas as pd
from sklearn.preprocessing import LabelEncoder,MinMaxScaler
from datapreprocessing import dataPrepocessing

def dataEngineering():
    df = dataPrepocessing()

    Y_ = df.loc[:,['G1','G2','G3']]
    Yavg = Y_.mean(axis=1)
    X_ = df.drop(['G1','G2','G3'], axis=1)
    #print(X_.head())
    
    # extracting categorical columns
    cat_df = X_.select_dtypes(include = ['object'])
    num_df = X_.select_dtypes(include=["number"])

    lb = LabelEncoder()
    cat_df = cat_df.apply(LabelEncoder().fit_transform)

    scaler = MinMaxScaler()

    scaler.fit(num_df)
    scaled = scaler.fit_transform(num_df)
    scaled_df = pd.DataFrame(scaled, columns=num_df.columns)

    X = pd.concat([cat_df,scaled_df,Yavg], axis = 1)
    X.to_csv("data_mod.csv", index = False)
    #print(X.head())
    return X


dataEngineering()