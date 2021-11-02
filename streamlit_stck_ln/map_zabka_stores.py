import pandas as pd
import requests
import streamlit as st


def get_shops_coordinates() -> list:
    json_url: str = "https://www.zabka.pl/ajax/shop-clusters.json"
    web_response = requests.get(url=json_url)
    web_json = web_response.json()
    return web_json


json_coordinates: list = get_shops_coordinates()

data = pd.DataFrame({
    'shop id': [shop_id['id'] for shop_id in json_coordinates],
    'lat': [shop_id['lat'] for shop_id in json_coordinates],
    'lon': [shop_id['lng'] for shop_id in json_coordinates],
})

st.title("Zabka shops in Poland")
st.map(data=data, )
st.subheader(f"Found: {len(json_coordinates)} shops")
