import os
import pandas as pd

from myproject.lexical_features import having_ip_address

def prepare_data_from_file(filePath):
    return pd.read_csv(filePath)


def standard_data():
    file = prepare_data_from_file(os.path.join('DataFiles', 'malicious_phish.csv'))

def lexical_features_from_raw_url(url):
    status = []
    status.append(having_ip_address(url))
    status.append()
