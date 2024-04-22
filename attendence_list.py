import streamlit as st
import pandas as pd
import pymongo


def app():



    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["attendance_system"]
    collection = db["students"]

    # Retrieve data from MongoDB
    data_from_mongo = list(collection.find())

    # Convert data to DataFrame
    df = pd.DataFrame(data_from_mongo)

    # Display data in Streamlit
    st.write("Data from MongoDB:")
    st.dataframe(df)
