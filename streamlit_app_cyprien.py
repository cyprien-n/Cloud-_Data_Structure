# import streamlit as st
# from pymongo import MongoClient
# import time

# # Increase message size limit
# # st.set_option('server.maxMessageSize', 500)  # Set the value according to your needs

# # Connection to the MongoDB database
# client = MongoClient('mongodb://localhost:27017/')
# db = client['Walmart_cloud']

# # Function for the internal user page
# def page_internal_user():
#     st.title("Internal User")

#     selected_tab = st.sidebar.selectbox("Navigation", ("Performance Measurement", "Other Option", "Query"))

#     if selected_tab == "Performance Measurement":
#         st.subheader("Performance Measurement")


#         num_iterations = st.number_input("Number of iterations for performance measurement", value=1)

#         if st.button("Start performance measurement"):
#             collection = db['sales']
#             pipeline = [
#                 {
#                     '$match': {
#                         'store_nbr': 1, 
#                         'item_nbr': 9
#                     }
#                 },
#                 {
#                     '$group': {
#                         '_id': None, 
#                         'total_units': {
#                             '$sum': '$units'
#                         }
#                     }
#                 },
#                 {
#                     '$project': {
#                         '_id': 0, 
#                         'total_units': 1
#                     }
#                 }
#             ]

#             execution_times = []

#             for i in range(num_iterations):
#                 start_time = time.time()
#                 result = list(collection.aggregate(pipeline))
#                 end_time = time.time()
#                 execution_time = end_time - start_time
#                 execution_times.append(execution_time)

#                 if i == 0:
#                     st.write("Query result (first iteration):", result[:10])  # Displaying only the first 10 rows

#             st.write(f"Average execution time over {num_iterations} iterations:", sum(execution_times) / len(execution_times), "seconds")

#     elif selected_tab == "Other Option":
#         st.subheader("Other Option")
#         # Add components for other features for the internal user

#     elif selected_tab == "Query":
#         st.subheader("Query")
#         # Add components for specific queries to MongoDB
#         # For example, input fields for queries, buttons to execute queries, etc.

# # Function for the external user page
# def page_external_user():
#     st.title("External User")
#     # Add components for the interface for external users
#     # ... (you can add a query tab for external users if needed)

# # Streamlit user interface
# st.title("Walmart Weather 🌧")

# user_level = st.selectbox("Select your user level", ("Internal", "External"))

# if user_level == "Internal":
#     page_internal_user()
# elif user_level == "External":
#     page_external_user()




##########################################################################################################




import streamlit as st
from pymongo import MongoClient
import time
import matplotlib.pyplot as plt

# Connexion à la base de données MongoDB
mongo_host = 'localhost'
mongo_port = 27017
mongo_database = 'Walmart_cloud'
client = MongoClient(f'mongodb://{mongo_host}:{mongo_port}/')
db = client[mongo_database]

# Fonction pour les Querys spécifiques pour l'utilisateur interne
def internal_queries():
    st.subheader("Data Analyst Queries")
    query_choice = st.selectbox("Choose a Data Analyst Query", ("Query 1 (DA)", "Query 2 (DA)", "Query 1 (End-User)", "Query 2 (End-User)", "Query 3 (End-User)", "Query 4 (End-User)"))

    if query_choice == "Query 1 (DA)":
        # Ajoutez ici la logique pour la Query 1 pour l'utilisateur interne
        st.write("You choose Query 1 (DA)")
    elif query_choice == "Query 2 (DA)":
        # Ajoutez ici la logique pour la Query 2 pour l'utilisateur interne
        st.write("You choose Query 2 (DA)")
    elif query_choice == "Query 1 (End-User)":
        # Ajoutez ici la logique pour la Query 1 pour l'utilisateur End-User
        st.write("You choose Query 1 (End-User)")
        if st.button("Run Query 1 (End-User)"):
            mongo_host = 'localhost'
            mongo_port = 27017
            mongo_database = 'Walmart_cloud'
            collection_name = 'sales'
            client = MongoClient(f'mongodb://{mongo_host}:{mongo_port}/')
            db = client[mongo_database]
            collection = db[collection_name]           
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
            result = list(collection.aggregate(pipeline))
            st.write(result)
    elif query_choice == "Query 2 (End-User)":
        # Ajoutez ici la logique pour la Query 2 pour l'utilisateur End-User
        st.write("You choose Query 2 (End-User)")
    elif query_choice == "Query 3 (End-User)":
        # Ajoutez ici la logique pour la Query 3 pour l'utilisateur End-User
        st.write("You choose Query 3 (End-User)")
    elif query_choice == "Query 4 (End-User)":
        # Ajoutez ici la logique pour la Query 4 pour l'utilisateur End-User
        st.write("You choose Query 4 (End-User)")

# Fonction pour les Querys spécifiques pour l'utilisateur End-User
def external_queries():
    st.subheader("Querys End-Users")
    query_choice = st.selectbox("Choose an End-User query ", ("Query 1 (End-User)", "Query 2 (End-User)", "Query 3 (End-User)", "Query 4 (End-User)"))

    if query_choice == "Query 1 (End-User)":
        # Ajoutez ici la logique pour la Query 1 pour l'utilisateur End-User
        st.write("You choose Query 1 (End-User)")
        if st.button("Run Query 1 (End-User)"):
            collection_name = 'sales'
            collection = db[collection_name]           
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
            result = list(collection.aggregate(pipeline))
            st.write(result)
    elif query_choice == "Query 2 (End-User)":
        # Ajoutez ici la logique pour la Query 2 pour l'utilisateur End-User
        st.write("You choose Query 2 (End-User)")
    elif query_choice == "Query 3 (End-User)":
        # Ajoutez ici la logique pour la Query 3 pour l'utilisateur End-User
        st.write("You choose Query 3 (End-User)")
    elif query_choice == "Query 4 (End-User)":
        # Ajoutez ici la logique pour la Query 4 pour l'utilisateur End-User
        st.write("You choose Query 4 (End-User)")

# Fonction pour la page utilisateur interne
def page_internal_user():
    st.title("Data Analyst User")

    onglet_selectionne = st.sidebar.selectbox("Navigation", ("Queries", "Performance Measurement"))

    if onglet_selectionne == "Performance Measurement":
        st.subheader("Performance Measurement")
        # Ajoutez ici la logique pour la Peformance Measurement pour l'utilisateur interne

        st.write("Exemple de pipeline à exécuter :")
        st.code("""
        # Votre pipeline donné ici...
        """)

        num_iterations = st.number_input("Number of iterations for Peformance Measurement", value=10)

        if st.button("Start Peformance Measurement"):
            collection_name = 'sales'

            avg_execution_times = []

            shards_list = list(range(1, 7))
            plt.figure(figsize=(10, 6))

            for num_shards in shards_list:
                collection = db[collection_name]

                execution_times = []

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

                for i in range(num_iterations):
                    start_time = time.time()
                    result = list(collection.aggregate(pipeline))
                    end_time = time.time()
                    execution_time = end_time - start_time
                    execution_times.append(execution_time)

                execution_times = sorted(execution_times)[1:-1]
                average_execution_time = sum(execution_times) / len(execution_times)
                avg_execution_times.append(average_execution_time)

                st.write(f"Average execution time with {num_shards} shards :", average_execution_time, "seconds")

                # client.close()

            fig, ax = plt.subplots()
            fig.patch.set_facecolor(st.get_option("theme.primaryColor"))

            # Plot the data
            ax.plot(shards_list, avg_execution_times, marker='o', linestyle='-', color='blue')
            ax.set_facecolor('rgba(0,0,0,0)')
            ax.yaxis.grid(False)
            ax.xaxis
            # Set plot labels and title
            ax.set_xlabel('Shards')
            ax.set_ylabel('Average Execution Time')
            ax.set_title('Average execution time depending of the number of Shards')
            st.pyplot(fig)

            # Plot des temps d'exécution moyens en fonction du nombre de shards
            # plt.plot(shards_list, avg_execution_times, marker='o', linestyle='-', color='blue')
            # fig.patch.set_facecolor(st.get_option("theme.primaryColor"))
            # plt.xlabel('Number of Shards')
            # plt.ylabel('Mean execution time (s)')
            # plt.title('Mean execution time depending of the number of Shards')
            # st.pyplot(plt)

    elif onglet_selectionne == "Queries":
        internal_queries()

# Fonction pour la page utilisateur End-User
def page_external_user():
    st.title("End-User")

    # onglet_selectionne = st.sidebar.selectbox("Navigation", "Queries")

    # if onglet_selectionne == "Autre Option":
    #     st.subheader("Autre Option")
    #     # Ajoutez ici d'autres composants pour d'autres fonctionnalités pour l'utilisateur End-User

    # if onglet_selectionne == "Queries":
    #     external_queries()
    external_queries()

# Interface utilisateur Streamlit
st.title("Walmart Weather 🌧")  

user_level = st.selectbox("Select your user level ", ("Data Analyst", "End-User", "Administrator"))

if user_level == "Data Analyst":
    page_internal_user()
elif user_level == "End-User":
    page_external_user()
