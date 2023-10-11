import requests
import pandas as pd
from io import StringIO


def getData():
    url = "https://raw.githubusercontent.com/arunk13/MSDA-Assignments/master/IS607Fall2015/Assignment3/student-mat.csv"
    # response = requests.get(url)
    # data = response.text
    # cleaned_dataset = pd.read_csv(StringIO(data))
    cleaned_dataset = pd.read_table(url, sep=";")
    print(cleaned_dataset.head())
    print(cleaned_dataset.columns)
    cleaned_dataset.to_csv('data.csv')
    return cleaned_dataset
getData()