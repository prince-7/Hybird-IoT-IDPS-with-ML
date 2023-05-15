import model
import data_preprocessing
import pickle
import pandas as pd
import os
import time
import subprocess
import json
import whatsapp


class Framework:
    def __init__(self):
        try:
            with open('model.pkl', 'rb') as f:
                self.model = pickle.load(f)
        except:
            self.model = model.Model()
            self.model.train()
            with open('model.pkl', 'wb') as f:
                pickle.dump(self.model, f)

        with open("/home/kali/Desktop/IoTSecFramework/config.json",'r') as j:
            creds = json.loads(j.read())
        #whatsapp Notification
        self.Whatsapp_Notification = whatsapp.WhatsApp(creds['whatsapp']['whatsapp_sid'], creds['whatsapp']['whatsapp_token'], creds['whatsapp']['whatsapp_from'], creds['whatsapp']['whatsapp_to'])
    
    def predict(self, log_file):
        print('Started Prediction')
        self.data = data_preprocessing.Data_preprocess(log_file).process()
        return self.model.predict(self.data)
    
    def show_reports(self):
        records = os.listdir('/home/kali/Desktop/IoTSecFramework/records')
        scan_records = [[], [], []]
        for record in records:
            curr_rec = record.split('.')[0]
            curr_rec = curr_rec.split()
            print(curr_rec)
            scan_records[0].append(curr_rec[0])
            scan_records[1].append(curr_rec[1])
            scan_records[2].append(f'/home/kali/Desktop/IoTSecFramework/records/{record}')
    
        records = pd.DataFrame({'Date': scan_records[0], 'Time': scan_records[1], 'Report': scan_records[2]})
        records.to_csv('/home/kali/Desktop/IoTSecFramework/report.csv', index=False)
    
    def notify(self, data):
        self.Whatsapp_Notification.send_message(data)
