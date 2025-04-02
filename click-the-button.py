import streamlit as st

import random

reaction_time = 0
number = random.randint(1, 75)
col1, col2, col3, col4, col5 = st.columns(5)
col6, col7, col8, col9, col10 = st.columns(5)
col11, col12, col13, col14, col15 = st.columns(5)
col16, col17, col18, col19, col20 = st.columns(5)
col21, col22, col23, col24, col25 = st.columns(5)
col26, col27, col28, col29, col30 = st.columns(5)
col31, col32, col33, col34, col35 = st.columns(5)
col36, col37, col38, col39, col40 = st.columns(5)
col41, col42, col43, col44, col45 = st.columns(5)
col46, col47, col48, col49, col50 = st.columns(5)
col51, col52, col53, col54, col55 = st.columns(5)
col56, col57, col58, col59, col60 = st.columns(5)
col61, col62, col63, col64, col65 = st.columns(5)
col66, col67, col68, col69, col70 = st.columns(5)
col71, col72, col73, col74, col75 = st.columns(5)
st.title("Click the Button :material/arrow_selector_tool:")
st.write("Your reaction time is " + str(reaction_time) + ".")
if number == 1:
  with col1:
    #start reaction time
    button = st.button(label="Click Me", icon=":material/arrow_selector_tool:")
