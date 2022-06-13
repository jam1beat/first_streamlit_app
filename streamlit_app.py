
import streamlit
import pandas

streamlit.title("My Parents New healthy Diner")
streamlit.header('Breakfest Menue')
streamlit.text('🥣 Omega 2 Bluebery Oatmeal')
streamlit.text('🍶 Kale and Spinch Roket Smoothie')
streamlit.text('🥚 Hard-Boiled Free-Range Egg')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.multiselect("Pick some fruite", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
