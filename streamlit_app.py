import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError
streamlit.title("My Mom's New Healthy Diner")
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)
# New Section for API


def get_fruityvice_data(this_fruit_choice):
  fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
  fruityvice_Normalized=pandas.json_normalize(fruityvice_response.json())
  return fruityvice_Normalized



streamlit.header('Fruityvice Fruit Advice')
try:
  fruit_choice=streamlit.text_input("What information would you like about?")
  if not fruit_choice:     #streamlit.write('User entered',fruit_choice)
    streamlit.error("Please select a fruit to get information")
  else:
      #fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
      #fruityvice_Normalized=pandas.json_normalize(fruityvice_response.json())
      back_from_function=get_fruityvice_data(fruit_choice)
      streamlit.dataframe(back_from_function)
      #streamlit.dataframe(fruityvice_Normalized)
except URLError as e:
  streamlit.error()
      
      
#import requests

#streamlit.text(fruityvice_response)
#streamlit.text(fruityvice_response.json())
#fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
#fruityvice_Normalized=pandas.json_normalize(fruityvice_response.json())
#streamlit.dataframe(fruityvice_Normalized)
streamlit.stop()

#import snowflake.connector
my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur=my_cnx.cursor()
#my_cur.execute("select current_user(), current_account(), current_region()")
#my_data_row=my_cur.fetchone()
#streamlit.text("Hello from snowflake:")
#streamlit.text(my_data_row)

my_cur.execute("select * from fruit_load_list")
my_data_row=my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_row)



streamlit.header('Fruityvice Fruit Advice')
add_my_fruit=streamlit.text_input("What fruit would you like to add",'jackfruit')
streamlit.write('Thanks for adding',add_my_fruit)

my_cur.execute("insert into fruit_load_list values('from streamlit')")






