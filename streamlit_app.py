
import streamlit
import pandas
import requests



streamlit.title("My Parents New healthy Diner")
streamlit.header('Breakfest Favorites')
streamlit.text('🥣 Omega 2 Bluebery Oatmeal')
streamlit.text('🍶 Kale and Spinch Roket Smoothie')
streamlit.text('🥚 Hard-Boiled Free-Range Egg')

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ "kiwi")
fruity_normalizeed = pandas.json_normalize(frutiyvice_response.json())
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), [1,16])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
streamlit.header("Fruityvice Fruit Advice")
streamlit.dataframe(fruity_normalizeed)
