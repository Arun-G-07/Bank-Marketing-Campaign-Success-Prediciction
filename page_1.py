import streamlit as st
import base64
import apps
import pandas as pd
import base64


def get_image(image_file):
    with open(image_file, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return encoded

image_bg = get_image("campaign.webp")
def background():
    st.markdown("""
    <style>
               .st-emotion-cache-13ln4jf {
                background-color: rgb(0 0 0 / .7);!important;
                padding-top:50px !important;
                padding-left:40px !important;
                padding-right:40px !important;

                } 
    </style>""", unsafe_allow_html=True)
    st.markdown(
        f"""<style>
        .stApp {{
            background-image: url("data:image/png;base64,{image_bg}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>""", unsafe_allow_html=True
    )

    # st.markdown("<h1 style='text-align:center;'>POTATO LEAF DISEASE PREDICTION</h1>", unsafe_allow_html=True)
    # st.markdown("---")

background()


def main():

    st.sidebar.title("Navigation")
    selected = st.sidebar.selectbox("Select a page", ["Introduction", "Model Prediction","Conclusion"])
    if selected == "Introduction":
        st.header("Hello, Welcome To My Machine Learning Project...!!!")
        st.header("Introduction")
        st.write("""
        The data is related with direct marketing campaigns of a Portuguese banking institution. 
        The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, 
        in order to access if the product (Bank term deposit) would be ('Yes') or not ('No') subscribed.
                 """)
        st.write("-[Bank Marketing Dataset Link](https://archive.ics.uci.edu/dataset/222/bank+marketing)")





    elif selected == "Model Prediction":
        apps.predict()
    else:

        st.title(":orange[Conclusion]")

        st.header("Project Summary Report")
        st.write("""
        The aim of the project is to develop and training a machine learning model by using the data related with the
        direct marketing campaigns of a Portuguese banking institution. By using this model we can identify the key features 
        that are most influencing the bank marketing campaign success and hence predicting the success of the campaign.
           """)


        st.header("Observations")
        st.write("""
        1) Client with job type as blue collar records the high and housemaid are the very less.

        2) Clients who are married are more in record and divorced are less.

        3) Clients whose educational background as secondary has the highest count.

        4) Default feature has value of yes and no which doesn't seems to play important role

        5) Data in month may records the higher and less in december
          
           """)

        st.header("Model Performance")
        st.write("""
           The machine learning model was developed and checked for its performance. The model showed a promising results, 
           as it gives an accuracy of 93%  using Random Forest Classifier. On a futuristic aspect, proper tuning methods can also be implemented to improve the model
           performance. 
           """)
main()