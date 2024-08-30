import numpy as np
import altair as alt
import pandas as pd
import streamlit as st


st.header('Система риск-менеджмента в ЭТП ГПБ')




with st.form("my_form"):
   bp = st.text_input('Описание бизнес-процесса')
   proc_importance = st.number_input('Критичность процесса',min_value=1,max_value=4,step=1,placeholder='Введите значение от 1 до 4',value=None)
   submitted = st.form_submit_button("Отправить")
   if submitted:
     st.write(bp)
     st.write(proc_importance)








