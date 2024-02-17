from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from io import StringIO
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.title("Code Review App ☕️")
st.header("Please upload your .py file here")

data = st.file_uploader("Upload python file", type=".py")

if data:
    # decoded content of 'data'
    stringio = StringIO(data.getvalue().decode("utf-8"))
    # reading the content of stringio object and storing it in the variable
    fetched_data = stringio.read()
    st.write(fetched_data)
