import streamlit as st
import plotly.express as px
import os
import time
import IoTSecFramework
import pandas as pd
import numpy as np

framework = IoTSecFramework.Framework()

st.set_page_config(page_title='IoT Security Framework',
                   page_icon=":bar-chart:",
                   layout="wide")

framework.show_reports()
reports_list = pd.read_csv('/home/kali/Desktop/IoTSecFramework/report.csv')
table_content = reports_list['Report'].to_numpy()

noOfFiles = table_content.size
noOfPackets = 0
deltaPackets = 0
noOfMalPac = 0
deltaMalPac = 0

for report in table_content:
   data = pd.read_csv(report, index_col=0)
   pac_data = data['Number of packets'].to_numpy()
   deltaPackets = np.sum(pac_data).item()
   noOfPackets = noOfPackets + deltaPackets

   mal_pac_data = data.loc[~data['Packet Type'].isin(['Benign'])]['Number of packets'].to_numpy()
   deltaMalPac = np.sum(mal_pac_data).item()
   noOfMalPac = noOfMalPac + deltaMalPac

     
st.title('Dashboard')

dash_col1, dash_col2, dash_col3 = st.columns(3)

dash_col1.metric(label="Number of Files analysed", value=noOfFiles)
dash_col2.metric(label="Number of Packets Analysed", value=noOfPackets, delta=deltaPackets)
dash_col3.metric(label="Number of Malicious packets detected", value=noOfMalPac, delta=deltaMalPac)

# --- SIDEBAR ---
st.sidebar.header("Input File for Analysis")
captured_data = st.sidebar.file_uploader('Upload your log file', type=['log'], accept_multiple_files=False)
if captured_data is not None:
   bytes_data = captured_data.getvalue()
   uploaded_file_path = f'/home/kali/Desktop/IoTSecFramework/uploads/uploaded-{time.strftime("%Y%m%d-%H%M%S")}-{captured_data.name}'
   with open(uploaded_file_path, 'wb') as f:
      f.write(bytes_data)

   while not os.path.exists(f'{uploaded_file_path}'):
      time.sleep(1)
   if os.path.isfile(f'{uploaded_file_path}'):
      st.divider()
      st.subheader(f'Result for Packet Analysis of {captured_data.name} file')

      report_df = framework.predict(f'{uploaded_file_path}')
      st.dataframe(report_df)
      framework.notify(report_df)
      st.success('Alert Notification sent on Whatsapp!', icon="✅")

st.divider()

st.subheader('Reports')

st.dataframe(reports_list, use_container_width=True)

with st.expander("See all Reports"):
	# rows
	for idx, row in zip(range(table_content.size),table_content):
		
		col1, col2 = st.columns(2)
		col1.write(str(row))
		
		placeholder = col2.empty()
		show_more   = placeholder.button("Show Report", key=idx, type="primary")

		# if button pressed
		if show_more:
			# rename button
			placeholder.button("Hide Report", key=str(idx)+"_")
			
			# do stuff
			report = pd.read_csv(row, index_col=0)
			st.dataframe(report)