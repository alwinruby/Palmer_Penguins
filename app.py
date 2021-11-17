import streamlit as st
from PIL import Image


# Data Viz Pkg
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
import seaborn as sns

# Core Pkgs
import pandas as pd
import numpy as np


DATA_URL = ("datasets/penguins_size.csv")


st.markdown("# Self Exploratory Visualization on palmerpenguins")
st.markdown("Explore the dataset to know more about palmerpenguins")
img=Image.open('images/palmerpenguins.png')
st.image(img,width=100)

st.markdown("**Penguins** are some of the most recognizable and beloved birds in the world and even have their own holiday: **World Penguin Day is celebrated every year on April 25**. Penguins are also amazing birds because of their physical adaptations to survive in unusual climates and to live mostly at sea. Penguins propel themselves through water by flapping their flippers.  Bills tend to be long and thin in species that are primarily fish eaters, and shorter and stouter in those that mainly eat krill.")

st.markdown("The data presented are of 3 different species of penguins - **Adelie, Chinstrap, and Gentoo,** collected from 3 islands in the **Palmer Archipelago, Antarctica.**")

if st.button("Meet the Palmer Penguins"):
    img=Image.open('images/lter_penguins.png')
    st.image(img,width=700, caption="We are Penguins 🐧")
    st.markdown("The data was collected and made available by **[Dr. Kristen Gorman](https://www.uaf.edu/cfos/people/faculty/detail/kristen-gorman.php)** and **[Palmer Station, Antarctica, LTER](https://pal.lternet.edu/)**.")

    images=Image.open('images/meet.png')
    st.image(images,width=600)

    #Ballons
    st.balloons()

st.info(" The dataset contains the different aspect between the species like Body Mass (g), Flipper Length (mm), Culmen Length (mm), Culmen Depth (mm) etc.")
img=Image.open('images/beak.png')
st.image(img,width=700)

st.sidebar.markdown("## Side Panel")
st.sidebar.markdown("Use this panel to explore the dataset and create own viz.")
# df = pd.read_csv(DATA_URL, nrows = nrows)


@st.cache(persist=True, show_spinner=True)
# Load  the Data
def load_data(nrows):
	#Parse date and Time
    df = pd.read_csv(DATA_URL, nrows = nrows)
    lowercase = lambda x:str(x).lower()
    df.rename(lowercase, axis='columns',inplace=True)
    return df


st.markdown("### Click the button below to explore the dataset through my visualization.")
if st.button("Visualization created by Author "):
    img=Image.open('images/palmerpenguins.png')
    st.image(img,width=700, caption="Viz. created by Author. 🐧")

    st.markdown(
    " **Takeaway:** Gento is *most massive & most gigantic* with an average body mass 5.08 Kg & average flipper length 217 mm.")


st.markdown("-----")


# Loading data
# df = load_data(100000)
# original_data = df
st.header("Now, Explore Yourself the Palmer Penguins")
# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading palmerpenguins dataset...')
    # Load 10,000 rows of data into the dataframe.
df = load_data(100000)
    # Notify the reader that the data was successfully loaded.
data_load_state.text('Loading palmerpenguins dataset...Completed!')

images=Image.open('images/meet.png')
st.image(images,width=600)

# Showing the original raw data
if st.checkbox("Show Raw Data", False):
    st.subheader('Raw data')
    st.write(df)

st.title('Quick  Explore')
st.sidebar.subheader(' Quick  Explore')
st.markdown("Tick the box on the side panel to explore the dataset.")
if st.sidebar.checkbox('Basic info'):
    if st.sidebar.checkbox('Dataset Quick Look'):
        st.subheader('Dataset Quick Look:')
        st.write(df.head())
    if st.sidebar.checkbox("Show Columns"):
        st.subheader('Show Columns List')
        all_columns = df.columns.to_list()
        st.write(all_columns)
    # if st.sidebar.checkbox('Column Names'):
    #     st.subheader('Column Names')
    #     st.write(df.columns())
    if st.sidebar.checkbox('Statistical Description'):
        st.subheader('Statistical Data Descripition')
        st.write(df.describe())
    if st.sidebar.checkbox('Missing Values?'):
        st.subheader('Missing values')
        st.write(df.isnull().sum())


# st.title('Quick  Explore')
# st.sidebar.subheader(' Quick  Explore')
# st.markdown("Tick the box on the side panel to explore the dataset.")
# if st.sidebar.checkbox('Basic info'):
#     if st.sidebar.checkbox('Dataset Quick Look'):
#         st.subheader('Dataset Quick Look:')
#         st.write(df.head())
#     if st.sidebar.checkbox("Show Columns"):
#         st.subheader('Show Columns List')
#         all_columns = df.columns.to_list()
#         st.write(all_columns)
#
#     if st.sidebar.checkbox('Statistical Description'):
#         st.subheader('Statistical Data Descripition')
#         st.write(df.describe())
#     if st.sidebar.checkbox('Missing Values?'):
#         st.subheader('Missing values')
#         st.write(df.isnull().sum())
