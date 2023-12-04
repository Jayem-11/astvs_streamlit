import streamlit as st
import requests
import json
from split import split_video
from files import get_files_with_blob, delete_files

# =========================================================================================

st.write("""

# ASVTS

""")


# =========================================================================================

st.write("""# """)

# =========================================================================================

# =========================================================================================

st.write("""## Upload a Swahili video and get a summary""")

# =========================================================================================

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()

    with open("video.mp4", 'wb') as f:
        f.write(bytes_data)

    st.video("video.mp4")

    split_video("video.mp4")


# Usage
directory = "./"
blob = "chunk*.mp4"  # Change this to the blob you're looking for
files = get_files_with_blob(directory, blob)


# Button
predict_bt = st.button('Summary')

st.write("""# """)

url = 'https://jayem-11-swahili.hf.space/predict'  # replace with your server URL

if predict_bt:

    summary = ""

    for file in files:

        data = {'file': open(file, 'rb')}

        response = requests.post(url, files=data)

        # Decode the byte string to string
        str_response = response.content.decode()

        # Parse the string to JSON
        json_response = json.loads(str_response)

        # Retrieve the summary content
        summary = summary + json_response['summary'][0]['summary_text']

    st.write("""### Summary""")
    st.success(summary)

    # Call the function
    st.balloons()

refresh = st.button('refresh')

if refresh:
    
    delete_files(files)
