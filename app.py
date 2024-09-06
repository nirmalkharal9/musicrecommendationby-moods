import streamlit as st
st.title("Hello Nepal")

st.header("This is header Section")

st.markdown("this is created using st markdown")

col1,col2=st.columns(2)
with col1:
    x=st.slider('choose x value',1,10)
with col2:
    st.write("THe value of : blue[***x***]")
