import streamlit
import pandas
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
streamlit.header('Fruityvice Fruit Advice')
fruit_choice=streamlit.text_input("What information would you like about?",'kiwi')
streamlit.write('User entered',fruit_choice)

import requests
fruityvice_response=requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
#streamlit.text(fruityvice_response)
#streamlit.text(fruityvice_response.json())

fruityvice_Normalized=pandas.json_normalize(fruityvice_response.json())
streamlit.dataframe(fruityvice_Normalized)


import snowflake.connector
my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur=my_cnx.cursor()
my_cur.execute("select current_user(), current_account(), current_region()")
my_data_row=my_cur.fetchone()
streamlit.text("Hello from snowflake:")
streamlit.text(my_data_row)
#
