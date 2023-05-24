import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox and subheader
st.title("Weather Forecast for the Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")
option = st.selectbox("Select data to view",
                      ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # This if is required to avoid an error as long as place is not filled
    # Get the temperture/sky data
    filtered_data = get_data(place, days)

    if option == "Temperature":
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        # Create a temperature plot
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if option == "Sky":
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png", "Rain": "images/rain.png",
                  "Snow": "images/snow.png"}
        # Weather is a list and contains a dictionary, the [0] is required to point to that and
        # with "main" we filter the description under "main in that dictionary
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        # List comprehension to find the image paths for the conditions
        image_paths = [images[condition] for condition in sky_conditions]
        print(sky_conditions)
        st.image(image_paths, width=115)