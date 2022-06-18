
import streamlit
import pandas
import requests
import snowflake.connector



streamlit.title("My Parents New Healthy Diner")
streamlit.header('Breakfest Favorites')
streamlit.text('🥣 Omega 2 Bluebery Oatmeal')
streamlit.text('🍶 Kale and Spinch Roket Smoothie')
streamlit.text('🥚 Hard-Boiled Free-Range Egg')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), [1,16])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
streamlit.header("Fruityvice Fruit Advice")

fruit_choice = streamlit.text_input('What fruit would you like information about? ', 'kiwi')
streamlit.write('The user entered ', fruit_choice)  
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
fruity_normalized = pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruity_normalized)


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from FRUIT_LOAD_LIST;")
my_data_rows = my_cur.fetchall()
streamlit.header("The FRUIT_LOAD_LIST contains:"
streamlit.dataframe(my_data_row)
