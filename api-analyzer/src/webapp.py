import streamlit as st
import logging
from bedrock_client import bedrock_client 


st.title("Swagger Analyzer")
st.header("Generates a report analyzing the input swagger")


#st.markdown(html_string, unsafe_allow_html=True)



logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', encoding='utf-8', level=logging.INFO)
#model_id="amazon.titan-text-express-v1"
model_id="anthropic.claude-instant-v1"

client = bedrock_client(model_id)


def generate_response(input_text):
  response = client.analyze(input_text)    
  logging.info("response: %s",response)
  st.info(response)
  #st.markdown(response, unsafe_allow_html=True)
with st.form('my_form'):
  text = st.text_area('Enter swagger file to analyze:')
  submitted = st.form_submit_button('Submit')
  if submitted :
    generate_response(text)