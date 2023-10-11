from os.path import exists
from download_data import getData
import pandas as pd
def datasetIngestion():
    file_exists = exists('data.csv')
    if not file_exists:
        df = getData()
        return df
    df = pd.read_csv('data.csv')
    return df

datasetIngestion()