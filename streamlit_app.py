
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError



streamlit.title("My Parents New Healthy Diner")
streamlit.header('Breakfest Favorites')
streamlit.text('🥣 Omega 2 Bluebery Oatmeal')
streamlit.text('🍶 Kale and Spinch Roket Smoothie')
streamlit.text('🥚 Hard-Boiled Free-Range Egg')

def get_fruity_vice_data(this_fruite_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+ fruit_choice)
    fruity_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruity_normalized

def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("select * from fruit_load_list")
         return my_cur.fetchall()

def insert_row_into_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('"+new_fruit+"');")
        return "Thanks for adding " + new_fruit
    
    
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), [1,16])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
streamlit.header("Fruityvice Fruit Advice")
try:
    fruit_choice = streamlit.text_input('What fruit would you like information about? ', 'kiwi')
    if not fruit_choice:
      streamlit.error("Please select a fruit to get information")
    else:
      streamlit.write('The user entered ', fruit_choice) 
      back_from_function = get_fruity_vice_data(fruit_choice)
      streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.stop()

add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add Fruit to the List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_into_snowflake(add_my_fruit)
    streamlit.text(back_from_function)

    
if streamlit.button('Get Fruit Load List'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows =  get_fruit_load_list()
    streamlit.header("The FRUIT_LOAD_LIST contains:")
    streamlit.dataframe(my_data_rows)
