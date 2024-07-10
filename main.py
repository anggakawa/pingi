import streamlit as st
import requests
import time
import utils


# Read components from a text file
COMPONENTS_TO_CHECK = utils.read_components_from_file('components.txt')


st.title("Pingi, simple status page")


# Add a timestamp to show when the page was last updated
st.write(f"Last updated: {time.strftime('%Y-%m-%d %H:%M:%S')}")

"---"

for component, desc, url in COMPONENTS_TO_CHECK:
    status_code, is_up = utils.check_component(url)

    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        st.button(f"{component}", key=f"{component}_button", disabled=True)

    with col2:
        st.write(f"{desc} ℹ️")

    with col3:
        if is_up:
            st.success(f"Operational (Status: {status_code})")
        else:
            if status_code:
                st.error(f"Down (Status: {status_code})")
            else:
                st.error("Down (Connection Error)")

    "---"

# Add some custom CSS to make it look more like the image
st.markdown("""
    <style>
    .stButton button {
        background-color: #34a853;
        color: white;
        border: none;
        border-radius: 20px;
        padding: 5px 10px;
        font-size: 14px;
    }
    .stButton button:disabled {
        opacity: 1;
    }
    </style>
    """, unsafe_allow_html=True)

while True:
    time.sleep(60)  # Refresh every 60 seconds
    st.rerun()
