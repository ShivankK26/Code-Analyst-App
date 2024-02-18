import base64
import time
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from io import StringIO
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

st.title("Code Review App ☕️")
st.header("Please upload your .py file here")


# Function to download text content
def text_downloader(raw_text):
    # Generating timestamps for file download
    timestr = time.strftime("%Y%m%d-%H%M%S")
    # Converting to base64 for file download
    b64 = base64.b64encode(raw_text.encode()).decode()
    # Creating a new filename after download
    new_filename = "reviewed_code_file_{}_.txt".format(timestr)
    st.markdown("Download File ✅")
    # Creating an HTML link and file download
    href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}">Click here!!</a>'
    # Displaying the HTML link
    st.markdown(href, unsafe_allow_html=True)


data = st.file_uploader("Upload python file", type=".py")

if data:
    # decoded content of 'data'
    stringio = StringIO(data.getvalue().decode("utf-8"))
    # reading the content of stringio object and storing it in the variable
    fetched_data = stringio.read()
    st.write(fetched_data)

    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.9)
    systemMessage = SystemMessage(
        content="You are a senior code analyst. Provide detailed suggestions to improve the below given python code."
    )

    humanMessage = HumanMessage(content=fetched_data)

    FinalResponse = chat([systemMessage, humanMessage])

    # Displaying the review comments
    st.markdown(FinalResponse.content)

    # Importing the download function
    text_downloader(FinalResponse.content)
