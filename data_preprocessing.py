import pandas as pd
import numpy as np

class Data_preprocess:
    def __init__(self, filepath):
        self.df = pd.read_table(filepath_or_buffer=filepath, skiprows=10, nrows=100000)
        self.df.columns= [
            'ts',
            'uid',
            'id.orig_h',
            'id.orig_p',
            'id.resp_h',
            'id.resp_p',
            'proto',
            'service',
            'duration',
            'orig_bytes',
            'resp_bytes',
            'conn_state',
            'local_orig',
            'local_resp',
            'missed_bytes',
            'history',
            'orig_pkts',
            'orig_ip_bytes',
            'resp_pkts',
            'resp_ip_bytes',
            'label'
            ]
        self.df.drop(self.df.tail(1).index,inplace=True)
        self.df.loc[(self.df.label == '-   Malicious   PartOfAHorizontalPortScan'), 'label'] = 'PartOfAHorizontalPortScan'
        self.df.loc[(self.df.label == '(empty)   Malicious   PartOfAHorizontalPortScan'), 'label'] = 'PartOfAHorizontalPortScan'
        self.df.loc[(self.df.label == '-   Malicious   Okiru'), 'label'] = 'Okiru'
        self.df.loc[(self.df.label == '(empty)   Malicious   Okiru'), 'label'] = 'Okiru'
        self.df.loc[(self.df.label == '-   Benign   -'), 'label'] = 'Benign'
        self.df.loc[(self.df.label == '-   benign   -'), 'label'] = 'Benign'
        self.df.loc[(self.df.label == '(empty)   Benign   -'), 'label'] = 'Benign'
        self.df.loc[(self.df.label == '-   Malicious   DDoS'), 'label'] = 'DDoS'
        self.df.loc[(self.df.label == '-   Malicious   C&C'), 'label'] = 'C&C'
        self.df.loc[(self.df.label == '(empty)   Malicious   C&C'), 'label'] = 'C&C'
        self.df.loc[(self.df.label == '-   Malicious   Attack'), 'label'] = 'Attack'
        self.df.loc[(self.df.label == '(empty)   Malicious   Attack'), 'label'] = 'Attack'
        self.df.loc[(self.df.label == '-   Malicious   C&C-HeartBeat'), 'label'] = 'C&C-HeartBeat'
        self.df.loc[(self.df.label == '(empty)   Malicious   C&C-HeartBeat'), 'label'] = 'C&C-HeartBeat'
        self.df.loc[(self.df.label == '-   Malicious   C&C-FileDownload'), 'label'] = 'C&C-FileDownload'
        self.df.loc[(self.df.label == '-   Malicious   C&C-Torii'), 'label'] = 'C&C-Torii'
        self.df.loc[(self.df.label == '-   Malicious   C&C-HeartBeat-FileDownload'), 'label'] = 'C&C-HeartBeat-FileDownload'
        self.df.loc[(self.df.label == '-   Malicious   FileDownload'), 'label'] = 'FileDownload'
        self.df.loc[(self.df.label == '-   Malicious   C&C-Mirai'), 'label'] = 'C&C-Mirai'
        self.df.loc[(self.df.label == '-   Malicious   Okiru-Attack'), 'label'] = 'Okiru-Attack'

    def process(self):
        self.df = self.df.drop(columns=['ts','uid','id.orig_h','id.resp_h', 'local_orig','local_resp','history'])
        self.df = pd.get_dummies(self.df, columns=['proto'])
        self.df = pd.get_dummies(self.df, columns=['conn_state'])
        self.df = pd.get_dummies(self.df, columns=['service'])
        self.df['duration'] = self.df['duration'].str.replace('-','0')
        self.df['orig_bytes'] = self.df['orig_bytes'].str.replace('-','0')
        self.df['resp_bytes'] = self.df['resp_bytes'].str.replace('-','0')
        self.df.fillna(-1,inplace=True)
        return self.df