
import streamlit
import pandas

streamlit.title("My Parents New healthy Diner")
streamlit.header('Breakfest Favorites')
streamlit.text('🥣 Omega 2 Bluebery Oatmeal')
streamlit.text('🍶 Kale and Spinch Roket Smoothie')
streamlit.text('🥚 Hard-Boiled Free-Range Egg')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])

