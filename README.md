- Our network security dashboard can perform log file scans, report generation, and raising Alert notifications to the user through WhatsApp.
- The web interface is built using Python’s Streamlit library, this was an obvious choice as the dashboard’s purpose was to encapsulate the Signature-based detection tool and ML model both of which were developed using Python.
- Our Web-Interface supports log file upload, the uploaded log files will be evaluated with our hybrid IoT Attack detection Framework, and the results will be stored as a report and a Notification will be sent on WhatsApp to the administrator. The network host from whom the malicious packets are detected will be blacklisted, hence mitigating further attacks.

- Schematic diagram of proposed hybrid framework
![image](https://github.com/prince-7/Hybird-IoT-IDPS-with-ML/assets/53997924/0b4f699c-5289-407e-99c5-97772e931aa9)

- Our web interface has a dashboard showing metrics of performed scans, there is a file uploader, along with detailed reports of previous scans.
![image](https://github.com/prince-7/Hybird-IoT-IDPS-with-ML/assets/53997924/0ca520e7-bdbc-49dd-a647-205555b699e2)

- On uploading a conn.log file to the dashboard, the file is immediately evaluated, and a report is generated, the generated report is also sent to the admin through WhatsApp.
![image](https://github.com/prince-7/Hybird-IoT-IDPS-with-ML/assets/53997924/6da05440-5d46-44fa-8fb4-2f2d41a5df1f)

- Detailed report of previous scans are available on the dashboard.
![image](https://github.com/prince-7/Hybird-IoT-IDPS-with-ML/assets/53997924/d9f85a52-5350-424d-90c2-2d68b6201c2f)
