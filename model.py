import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from datetime import datetime
import os

class Model:
    def __init__(self):
        dataset_path='./iot23_new_combined.csv'
        self.df = pd.read_csv(dataset_path)
        del self.df['Unnamed: 0']
        self.features_name = ['id.orig_p', 'id.resp_p', 'duration', 'orig_bytes', 'resp_bytes', 'missed_bytes', 'orig_pkts', 'orig_ip_bytes', 'resp_pkts', 'resp_ip_bytes', 'proto_icmp', 'proto_tcp', 'proto_udp', 'conn_state_OTH', 'conn_state_REJ', 'conn_state_RSTO', 'conn_state_RSTOS0', 'conn_state_RSTR', 'conn_state_RSTRH', 'conn_state_S0', 'conn_state_S1', 'conn_state_S2', 'conn_state_S3', 'conn_state_SF', 'conn_state_SH', 'conn_state_SHR', 'service_-', 'service_dhcp', 'service_dns', 'service_http', 'service_irc', 'service_ssh', 'service_ssl']
        # Initialize the Random Forest classifier
        self.model = RandomForestClassifier(n_estimators=100,  random_state=42)
    
    def train(self):
        X = self.df[self.features_name]
        y = self.df['label']

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the model
        self.model.fit(X_train, y_train)

        # Make predictions on the testing set
        y_pred = self.model.predict(X_test)

        # Calculate the accuracy of the model
        accuracy = accuracy_score(y_test, y_pred)
        print("Random Forest Classifier Accuracy: {:.2f}%".format(accuracy*100))
        print(classification_report(y_test, y_pred))
    
    def predict(self, test_df):
        for feat in self.features_name:
            if feat not in test_df:
                test_df[feat] = 0
        
        test_X = test_df[self.features_name]
        test_pred_y = self.model.predict(test_X)

        unique_elements, counts_elements = np.unique(test_pred_y, return_counts=True)
        print("Frequency of unique values of the said array:")
        print(np.asarray((unique_elements, counts_elements)))

        # datetime object containing current date and time
        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
        report = pd.DataFrame({'Packet Type': unique_elements, 'Number of packets': counts_elements})
        report.to_csv(f'/home/kali/Desktop/IoTSecFramework/records/{dt_string}.csv')
        return report


