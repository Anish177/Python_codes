import pandas as pd
import streamlit as st
import requests
import time

st.title('FMMS')

st.subheader('Temp Data')
df = pd.read_csv('temp.csv')
chart = st.line_chart(df, x='Date/Time', y='Temperature')
# while True:
#     value = requests.get('https://api.init.st/data/v1/events/latest?accessKey=ist_6jxPkB-hjd9Iv2qkz5hzoxjhwwD9tUf-&bucketKey=piot_temp_stream031815', timeout=2)
#     value = value.json()['temperature (C)']['value']

#     dic = {'Date/Time': time.asctime(time.localtime())[4:19], 'Temperature': value}
#     df = df.append(dic, ignore_index=True)
#     df.to_csv('temp.csv',index=False)
#     chart.empty()
#     chart = st.line_chart(df, x='Date/Time', y='Temperature')

    
#     time.sleep(2)