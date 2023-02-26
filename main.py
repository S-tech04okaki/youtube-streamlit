import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit　超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

'Done!!'

#st.write('Interactice Widgets')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ１の回答')
expander1 = st.expander('問い合わせ2')
expander1.write('問い合わせ２の回答')
expander1 = st.expander('問い合わせ３')
expander1.write('問い合わせ3の回答')

#text=st.text_input('あなたの趣味を教えてください')
#'あなたの趣味',text

#st.write('Display image')

#option=st.selectbox(
#    'あなたが好きな数字を教えてください',
#    list(range(1,11))
#)
#'あなたが好きな数字は',option,'です。'

#if st.checkbox('Show Image'):
#    img=Image.open('IMG-2445.JPG')
#    st.image(img, caption='me', use_column_width=True)