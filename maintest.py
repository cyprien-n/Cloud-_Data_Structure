import streamlit as st
from pymongo import MongoClient
import time
import matplotlib.pyplot as plt
import plotly.express as px
import datetime as dt


# Connexion à la base de données MongoDB
mongo_host = 'localhost'
mongo_port = 27017
mongo_database = 'WalmartWeather'
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
            mongo_database = 'WalmartWeather'
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
        if st.button("Run Query 3 (End-User)"):
            mongo_host = 'localhost'
            mongo_port = 27017
            mongo_database = 'WalmartWeather'
            client = MongoClient(f'mongodb://{mongo_host}:{mongo_port}/')
            db = client[mongo_database]
            collection_name = 'sales'
            collection = db[collection_name]           
            pipeline = [
                {
                    '$match': {
                        'store_nbr': {
                            '$in': [
                                1,2,3
                            ]
                        }, 
                        'date': {
                            '$gte': dt.datetime(2012, 12, 1, 0, 0, 0, tzinfo=dt.timezone.utc), 
                            '$lte': dt.datetime(2012, 12, 31, 0, 0, 0, tzinfo=dt.timezone.utc)
                        }
                    }
                }, {
                    '$group': {
                        '_id': {
                            'store_nbr': '$store_nbr', 
                            'item_nbr': '$item_nbr'
                        }, 
                        'total_units': {
                            '$sum': '$units'
                        }
                    }
                }, {
                    '$project': {
                        'store_nbr': '$_id.store_nbr', 
                        'item_nbr': '$_id.item_nbr', 
                        'total_units': 1, 
                        '_id': 0
                    }
                }
            ]
            result = list(collection.aggregate(pipeline))
            st.write(result)
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
        if st.button("Run Query 3 (End-User)"):
            collection_name = 'sales'
            collection = db[collection_name]           
            pipeline = [
                {
                    '$match': {
                        'store_nbr': {
                            '$in': [
                                1,2,3
                            ]
                        }, 
                        'date': {
                            '$gte': dt.datetime(2012, 12, 1, 0, 0, 0, tzinfo=dt.timezone.utc), 
                            '$lte': dt.datetime(2012, 12, 31, 0, 0, 0, tzinfo=dt.timezone.utc)
                        }
                    }
                }, {
                    '$group': {
                        '_id': {
                            'store_nbr': '$store_nbr', 
                            'item_nbr': '$item_nbr'
                        }, 
                        'total_units': {
                            '$sum': '$units'
                        }
                    }
                }, {
                    '$project': {
                        'store_nbr': '$_id.store_nbr', 
                        'item_nbr': '$_id.item_nbr', 
                        'total_units': 1, 
                        '_id': 0
                    }
                }
            ]
            result = list(collection.aggregate(pipeline))
            st.write(result)
        st.write("You choose Query 3 (End-User)")
    elif query_choice == "Query 4 (End-User)":
        # Ajoutez ici la logique pour la Query 4 pour l'utilisateur End-User
        st.write("You choose Query 4 (End-User)")


# Fonction pour la page de mesure de performance
def page_performance_measurement():
    st.subheader("Performance Measurement")
    # Ajoutez ici la logique pour la Peformance Measurement pour l'utilisateur interne

    st.write("Select the query you want to evaluate:")
    query_choice = st.selectbox("Choose a Data Analyst Query", ("Query 1 (DA)", "Query 2 (DA)", "Query 1 (End-User)", "Query 2 (End-User)", "Query 3 (End-User)", "Query 4 (End-User)"))

    if query_choice == "Query 1 (DA)":
        # Ajoutez ici la logique pour la Query 1 pour l'utilisateur interne
        st.write("You choose Query 1 (DA)")
    elif query_choice == "Query 2 (DA)":
        # Ajoutez ici la logique pour la Query 2 pour l'utilisateur interne
        st.write("You choose Query 2 (DA)")
    elif query_choice == "Query 1 (End-User)":
        # Ajoutez ici la logique pour la Query 1 pour l'utilisateur End-User
        collection_name = 'sales'
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
        
        st.write("You choose Query 1 (End-User)")
        st.code("""pipeline = [
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
            ]""")

    num_iterations = st.number_input("Number of iterations for Peformance Measurement", value=10)

    if st.button("Start Peformance Measurement"):
        

        avg_execution_times = []
################################### CHANGER RANGE(1,7) ###################################################
        shards_list = list(range(1, 7))
        plt.figure(figsize=(10, 6))

        for num_shards in shards_list:
            collection = db[collection_name]

            execution_times = []

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
        # Create a Plotly Express scatter plot
        fig = px.scatter(x=shards_list, y=avg_execution_times, labels={'x': 'Shards', 'y': 'Average Execution Time'},
                        title='My Plot', template='plotly_dark')

        # Set background color of the plot area
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)')  # Full transparency

        # Display the plot in Streamlit
        st.plotly_chart(fig)
        # fig, ax = plt.subplots()
        # fig.patch.set_facecolor(st.get_option("theme.primaryColor"))

        # # Plot the data
        # ax.plot(shards_list, avg_execution_times, marker='o', linestyle='-', color='lightblue')
        # ax.set_facecolor(("#FFFFFF"))  # Full transparency
        # ax.yaxis.grid(False)
        # # ax.xaxis
        # # Set plot labels and title
        # ax.set_xlabel('Shards')
        # ax.set_ylabel('Average Execution Time')
        # ax.set_title('Average execution time depending of the number of Shards')
        # st.pyplot(fig)

        # Plot des temps d'exécution moyens en fonction du nombre de shards
        # plt.plot(shards_list, avg_execution_times, marker='o', linestyle='-', color='blue')
        # fig.patch.set_facecolor(st.get_option("theme.primaryColor"))
        # plt.xlabel('Number of Shards')
        # plt.ylabel('Mean execution time (s)')
        # plt.title('Mean execution time depending of the number of Shards')
        # st.pyplot(plt)

# Fonction pour la page data statistiques administrateur
def data_stat_admin():
    call= db.command("dbstats")
    datasize = call['dataSize'] / 1024
    objects = call['objects']
    collections = call['collections']
    st.write("Database Distribution Statistics  : ")
    st.write('\n')
    st.write('Objects:', str(objects))
    st.write('Collections:', str(collections))
    st.write('Size:', str(datasize) + ' Mb')
    st.write('\n')
    

# Fonction pour la page utilisateur interne
def page_internal_user():
    st.title("Data Analyst User")

    onglet_selectionne = st.sidebar.selectbox("Navigation", ("Queries", "Performance Measurement"))

    if onglet_selectionne == "Performance Measurement":
        page_performance_measurement()

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

# Fonction pour la page Administrateur
def page_admin():
    st.title("Administrator")
    onglet_selectionne = st.sidebar.selectbox("Navigation", ("Data Distribution Statistics", "Cluster State", "Data Repartition", "Indexes"))

    if onglet_selectionne == "Data Distribution Statistics":
        data_stat_admin()
# Interface utilisateur Streamlit
st.title("Walmart Weather 🌧")  
# st.set_page_config(page_title="Walmart Weather 🌧", layout="wide", bg_color="lightblue")
user_level = st.selectbox("Select your user level ", ("Data Analyst", "End-User", "Administrator"))

if user_level == "Data Analyst":
    page_internal_user()
elif user_level == "End-User":
    page_external_user()
elif user_level == "Administrator":
    page_admin()
