
import streamlit
import pandas
import requests



streamlit.title("My Parents New healthy Diner")
streamlit.header('Breakfest Favorites')
streamlit.text('🥣 Omega 2 Bluebery Oatmeal')
streamlit.text('🍶 Kale and Spinch Roket Smoothie')
streamlit.text('🥚 Hard-Boiled Free-Range Egg')

fuit_choice = streamlit.text_input("What fruit would you like information about? ", kiwi)
streamlit.write('The user entered ', fuit_choice)  
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fuit_choice)
fruity_normalized = pandas.json_normalize(fruityvice_response.json())
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), [1,16])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
streamlit.header("Fruityvice Fruit Advice")
fuit_choice = stremlit.text_input("What fruit would you like information about? ", kiwi)
streamlit.write('The user entered ', fuit_choice)  
streamlit.dataframe(fruity_normalized)
