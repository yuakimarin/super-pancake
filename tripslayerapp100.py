
import pydeck as pdk
import pandas as pd
import json
import datetime
import numpy as np
import time
import streamlit as st

mbp0=[]
mblayer=[]

# Create a placeholder for pydeck map
map = st.empty()

#It was so slow that I read only 100 module..
for idx2 in range(100):
    for idx in range(100):
        jsonname="hoge.json"
        df=pd.read_json(jsonname)
        df["coordinates"] = df["waypoints"].apply(lambda f: [item["coordinates"] for item in f])
        # 1413946470 is  initial epoch time ** in my case. **
        df["timestamps"] = df["waypoints"].apply(lambda f: [item["timestamp"]/1000 -1413946470 for item in f])
        df.drop(["waypoints"], axis=1, inplace=True)

        layer =pdk.Layer(
            "TripsLayer",
            df,
            get_path="coordinates",
            get_timestamps="timestamps",
            get_color=[255, 255, 0],
            opacity=0.8,
            width_min_pixels=4,
            rounded=True,
            trail_length=500,
            current_Time=idx2*10,
        )
        mbp0.append(layer)

    mblayer.append(mbp0)
    mbp0=[]
    
#view_state = pdk.ViewState(latitude=37.7749295, longitude=-100.4194155, zoom=11, bearing=0, pitch=45)
view_state = pdk.ViewState(latitude=22.54554, longitude=114.0683, zoom=11, bearing=0, pitch=45)

# Render
    for index in range(100):
        r = pdk.Deck(layers=[mblayer[index]], initial_view_state=view_state)
        map.pydeck_chart(r)
    
