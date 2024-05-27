import streamlit as st
from dotenv import load_dotenv #python-dotenv
import os
import pandas as pd

load_dotenv()


def get_query(prompt):
    from openai import OpenAI

    client = OpenAI(
                    api_key= os.getenv("OPENAI_API_KEY"),
                )
    conversation1 = [{"role": "system", "content": f"""You specialize in the field of data science. 
                      You only know about this field.
                      Based on the {genre} give answers based on this feild.
                      -Based on the {genre} given to you, give the description about the topic.
                      -If the user asks you anything apart from this feild just tell them you don't know.
                      -Provide the answers in the json format with the answer stored in the key "Results :" 
                      - Please do not mention any symbol like ```json, ---, /, # etc. Just provide me the json.

                      
                      """},
                    {"role": "user", "content": prompt}]
    response1 = client.chat.completions.create(
            messages=conversation1,
            model="gpt-4",
            #temperature=0,
            max_tokens=400,
            top_p=0.9
        )
    output=response1.choices[0].message.content
    return output


st.title("DEMO")

st.caption("""Data science is the art and science of extracting insights and knowledge from data using 
           various techniques and tools. It involves collecting, cleaning, and analyzing large amounts 
           of data to uncover patterns, trends, and relationships that can be used to make informed 
           decisions and predictions. Data scientists employ a combination of skills from computer science, 
           statistics, and domain expertise to solve complex problems and extract actionable insights from data. 
           Through the application of machine learning, statistical modeling, and data visualization techniques, 
           data scientists help organizations leverage their data assets to gain a competitive edge, optimize processes, 
           and drive innovation.""")


st.subheader("Ask me Data Science !!!")

genre = st.radio(
    "Select the Subtopic you want to explore:",
    [":rainbow[Machine Learning]", "***Deep Learning***", "Reinforcement Learning :robot_face:"],
    index=None,
)

st.write("You selected:", genre)

prompt = st.text_area(f"Enter the topic you want to learn under {genre}:")
if st.button("Explore"):
    with st.spinner('Processing...'):
        output = get_query(prompt)
        st.write(output)