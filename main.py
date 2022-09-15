import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100) :
    latest_iteration.text(f'Iteration{i + 1}')
    bar.progress(i + 1)
    time.sleep(0.01)

'Done!'

st.write('DataFrame : udemy19分まで終わったよ')
st.write('streamlit run main.py    ←実行する')

df = pd.DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)

st.dataframe(df.style.highlight_max(axis=0), width=200, height=200)
st.table(df)

"""
# マークダウン　章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

st.line_chart(df)
st.bar_chart(df)

left_column, right_column = st.columns(2)

df2 = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

left_column.map(df2)
if left_column.button('右カラムに文字を表示') :
    right_column.write('Hey！')

expand = st.expander('問い合わせ')
expand.write('問い合わせ内容を書く')

option = st.selectbox(
    '好きな数字を選択',
    list(range(1, 11))
)

'推し数字：', option

text = st.sidebar.text_input('推しは？')
condition = st.sidebar.slider('ご機嫌いかが？',0 , 100, 50)
'推し:',text
'ご機嫌:', condition


st.write('Display Image')

if st.checkbox('Show Image') :

    img = Image.open('InterMezzo.jpg')
    st.image(img, caption='MEZZO"！！！', use_column_width=True)

