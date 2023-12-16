import streamlit as st
from pymongo import MongoClient
import time

# Increase message size limit
# st.set_option('server.maxMessageSize', 500)  # Set the value according to your needs

# Connection to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['Walmart_cloud']

# Function for the internal user page
def page_internal_user():
    st.title("Internal User")

    selected_tab = st.sidebar.selectbox("Navigation", ("Performance Measurement", "Other Option", "Query"))

    if selected_tab == "Performance Measurement":
        st.subheader("Performance Measurement")


        num_iterations = st.number_input("Number of iterations for performance measurement", value=1)

        if st.button("Start performance measurement"):
            collection = db['sales']
            pipeline = [
                {
                    '$match': {
                        'store_nbr': 1, 
                        'item_nbr': 9
                    }
                },
                {
                    '$group': {
                        '_id': None, 
                        'total_units': {
                            '$sum': '$units'
                        }
                    }
                },
                {
                    '$project': {
                        '_id': 0, 
                        'total_units': 1
                    }
                }
            ]

            execution_times = []

            for i in range(num_iterations):
                start_time = time.time()
                result = list(collection.aggregate(pipeline))
                end_time = time.time()
                execution_time = end_time - start_time
                execution_times.append(execution_time)

                if i == 0:
                    st.write("Query result (first iteration):", result[:10])  # Displaying only the first 10 rows

            st.write(f"Average execution time over {num_iterations} iterations:", sum(execution_times) / len(execution_times), "seconds")

    elif selected_tab == "Other Option":
        st.subheader("Other Option")
        # Add components for other features for the internal user

    elif selected_tab == "Query":
        st.subheader("Query")
        # Add components for specific queries to MongoDB
        # For example, input fields for queries, buttons to execute queries, etc.

# Function for the external user page
def page_external_user():
    st.title("External User")
    # Add components for the interface for external users
    # ... (you can add a query tab for external users if needed)

# Streamlit user interface
st.title("Walmart Weather 🌧")

user_level = st.selectbox("Select your user level", ("Internal", "External"))

if user_level == "Internal":
    page_internal_user()
elif user_level == "External":
    page_external_user()
