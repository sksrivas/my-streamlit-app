import streamlit as st
from textblob import TextBlob

# Title of the app
st.title("Welcome to My Streamlit App")

# Add a slider to select a number
number = st.slider("Select a number", 0, 100)

# Display the number
st.write(f"You selected: {number}")

# Add a button and perform an action when clicked
if st.button("Click me!"):
    st.write("Button was clicked!")

# Sample sentiment analysis using TextBlob
text = "Streamlit is awesome! I love building apps with it."
blob = TextBlob(text)
sentiment = blob.sentiment
st.write(f"Sentiment: {sentiment}")
