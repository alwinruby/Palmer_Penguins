import streamlit as st
from PIL import Image

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
import seaborn as sns
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
st.markdown(
    "The data was collected and made available by **[Dr. Kristen Gorman](https://www.uaf.edu/cfos/people/faculty/detail/kristen-gorman.php)** and **[Palmer Station, Antarctica, LTER](https://pal.lternet.edu/)**.")
images=Image.open('images/meet.png')
st.image(images,width=600)

#Ballons
st.balloons()

st.info(" The dataset contains the different aspect between the species like Body Mass (g), Flipper Length (mm), Culmen Length (mm), Culmen Depth (mm) etc.")
img=Image.open('images/beak.png')
st.image(img,width=700)
