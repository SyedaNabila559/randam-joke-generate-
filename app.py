import streamlit as st
import requests

def get_random_joke():
    # Fetch a random joke from the API
    url = 'https://official-joke-api.appspot.com/random_joke'
    response = requests.get(url)
    if response.status_code == 200:
        joke_data = response.json()
        return joke_data['setup'], joke_data['punchline']
    else:
        return None, None

# Streamlit interface
st.title('Random Joke Generator 🤣')

# Button to get a random joke
if st.button('Tell me a joke 😂'):
    setup, punchline = get_random_joke()
    if setup and punchline:
        st.subheader('Here\'s a joke for you! 😄')
        st.write(f"**{setup}**")
        st.write(f"**{punchline}** 😆")
    else:
        st.write("Sorry, I couldn't fetch a joke at the moment. 😕")
