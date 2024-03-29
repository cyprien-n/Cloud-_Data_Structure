###########################################                Imports                 #########################################################


import streamlit as st
from pymongo import MongoClient
import time
import matplotlib.pyplot as plt
import plotly.express as px
import datetime as dt
import json
import pandas as pd



###########################################     Connection to MongoDB database     #########################################################

mongo_database = 'Walmart'
mongo_cloud_url = 'mongodb+srv://username:Walmart@wlamart.pwzpbh8.mongodb.net/'
client = MongoClient(mongo_cloud_url)
db = client[mongo_database]



###########################################         Defining the queries          #########################################################


EU1 = [
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

EU2 = [
    {
        '$match': {
            'store_nbr': 30
        }
    }, {
        '$lookup': {
            'from': 'weather', 
            'localField': 'station_nbr', 
            'foreignField': 'station_nbr', 
            'as': 'weather_info'
        }
    }, {
        '$unwind': '$weather_info'
    }, {
        '$match': {
            'weather_info.snowfall': {
                '$gt': 2
            }
        }
    }, {
        '$lookup': {
            'from': 'sales', 
            'let': {
                'store_nbr': '$store_nbr', 
                'weather_date': '$weather_info.date'
            }, 
            'pipeline': [
                {
                    '$match': {
                        '$expr': {
                            '$and': [
                                {
                                    '$eq': [
                                        '$store_nbr', '$$store_nbr'
                                    ]
                                }, {
                                    '$eq': [
                                        '$date', '$$weather_date'
                                    ]
                                }
                            ]
                        }
                    }
                }
            ], 
            'as': 'sales_info'
        }
    }, {
        '$unwind': '$sales_info'
    }, {
        '$group': {
            '_id': '$store_nbr', 
            'total_units_sold': {
                '$sum': '$sales_info.units'
            }
        }
    }
]

EU3 = [
                {
                    '$match': {
                        'store_nbr': {
                            '$in': [
                                1
                            ]
                        }, 
                        'date': {
                            '$gte': dt.datetime(2012, 1, 1, 0, 0, 0, tzinfo=dt.timezone.utc), 
                            '$lte': dt.datetime(2012, 1, 31, 0, 0, 0, tzinfo=dt.timezone.utc)
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
                        'store_nbr': 1, 
                        'item_nbr': '$_id.item_nbr', 
                        'total_units': 1, 
                        '_id': 0
                    }
                }, {
                    '$sort': {'item_nbr': 1} 
                   }
            ]

EU4 = [
                {
                    '$match': {
                        'item_nbr': {
                            '$in': [
                                5
                            ]
                        }, 
                        'date': {
                            '$gte': dt.datetime(2012, 1, 1, 0, 0, 0, tzinfo=dt.timezone.utc), 
                            '$lte': dt.datetime(2012, 1, 31, 0, 0, 0, tzinfo=dt.timezone.utc)
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
                        'item_nbr': 1, 
                        'total_units': 1, 
                        '_id': 0
                    }
                }, {
                    '$sort': {'store_nbr': 1} 
                   }
            ]


DA1 = []

DA2 = [
                {
                    '$match': {
                        'store_nbr': 30 # Parameter the query by setting this value
                    }
                }, {
                    '$lookup': {
                        'from': 'weather', 
                        'localField': 'station_nbr', 
                        'foreignField': 'station_nbr', 
                        'as': 'weather_info'
                    }
                }, {
                    '$unwind': '$weather_info'
                }, {
                    '$match': {
                        'weather_info.snowfall': {
                            '$gt': 2
                        }
                    }
                }, {
                    '$lookup': {
                        'from': 'sales', 
                        'let': {
                            'store_nbr': '$store_nbr', 
                            'weather_date': '$weather_info.date'
                        }, 
                        'pipeline': [
                            {
                                '$match': {
                                    '$expr': {
                                        '$and': [
                                            {
                                                '$eq': [
                                                    '$store_nbr', '$$store_nbr'
                                                ]
                                            }, {
                                                '$eq': [
                                                    '$date', '$$weather_date'
                                                ]
                                            }
                                        ]
                                    }
                                }
                            }
                        ], 
                        'as': 'sales_info'
                    }
                }, {
                    '$unwind': '$sales_info'
                }, {
                    '$group': {
                        '_id': '$store_nbr', 
                        'total_units_sold': {
                        '$sum': '$sales_info.units'
                        }
                    }
                },{
                                '$sort': {'total_units': -1} 
                            }
            ]


###########################################     Functions for the actions and views limited to end-users      #########################################################

def page_end_user():
    st.title("End-User")
    # Only access to visualizing query results
    eu_queries()

def eu_queries():
    st.subheader("End-User queries")
    query_choice = st.selectbox("Choose an End-User query ", ("Query 1 (End-User)", "Query 2 (End-User)", "Query 3 (End-User)", "Query 4 (End-User)"),index=None)

    if query_choice == "Query 1 (End-User)":
        st.write("You choose Query 1 (End-User)")
        if st.button("Run Query 1 (End-User)"):
            collection_name = 'sales'
            collection = db[collection_name]           
            pipeline = EU1
            # Displaying the result as a dataframe and the execution time 
            start_time = time.time()
            result = list(collection.aggregate(pipeline))
            end_time = time.time()
            execution_time = end_time - start_time
            df_eu1 = pd.DataFrame(result)
            st.write("This query returns the number of sales of item_nbr 5 across all stores in the month of January.")
            st.write(df_eu1)
            st.write(f"Execution time : {execution_time} seconds")

    elif query_choice == "Query 2 (End-User)":
        st.write("You choose Query 2 (End-User)")
        if st.button("Run Query 2 (End-User)"):
            collection_name = 'sales'
            collection = db[collection_name]           
            pipeline = EU2
            # Displaying the result as a dataframe and the execution time 
            start_time = time.time()
            result = list(collection.aggregate(pipeline))
            end_time = time.time()
            execution_time = end_time - start_time
            df_eu2 = pd.DataFrame(result)
            st.write("This query returns the last weather report of a given store.")
            st.write(df_eu2)
            st.write(f"Execution time : {execution_time} seconds")

    elif query_choice == "Query 3 (End-User)":
        if st.button("Run Query 3 (End-User)"):
            collection_name = 'sales'
            collection = db[collection_name]           
            pipeline = EU3 
            # Displaying the result as a dataframe and the execution time 
            start_time = time.time()
            result = list(collection.aggregate(pipeline))
            end_time = time.time()
            execution_time = end_time - start_time
            df_eu3 = pd.DataFrame(result)
            st.write("This query returns the number of sales of all items from the store 1 in the month of February.")
            st.write(df_eu3[['item_nbr', 'total_units']])
            st.write(f"Execution time : {execution_time} seconds")

    elif query_choice == "Query 4 (End-User)":
        st.write("You choose Query 4 (End-User)")
        if st.button("Run Query 4 (End-User)"):
            collection_name = 'sales'
            collection = db[collection_name]           
            pipeline = EU4
            # Displaying the result as a dataframe and the execution time 
            start_time = time.time()
            result = list(collection.aggregate(pipeline))
            end_time = time.time()
            execution_time = end_time - start_time
            df_eu4 = pd.DataFrame(result)
            st.write("This query returns the number of sales of item_nbr 5 across all stores in the month of January.")
            st.write(df_eu4[['store_nbr', 'total_units']])
            st.write(f"Execution time : {execution_time} seconds")



###########################################     Functions for the actions and views limited to data analysts     #########################################################

def page_data_analyst():
    st.title("Data Analyst User")

    # onglet_selectionne = st.sidebar.selectbox("Navigation", ("Queries", "Performance Measurement"), index=None)

    # if onglet_selectionne == "Performance Measurement":
    #     page_performance_measurement()

    # elif onglet_selectionne == "Queries":
    da_queries()


def da_queries():
    st.subheader("Data Analyst Queries")
    # A menu where the DA can select the query they want:
    query_choice = st.selectbox("Choose a Data Analyst Query", ("Query 1 (DA)", "Query 2 (DA)", "Query 1 (End-User)", "Query 2 (End-User)", "Query 3 (End-User)", "Query 4 (End-User)"), index=None)

    if query_choice == "Query 1 (DA)":
        st.write("You choose Query 1 (DA)")
        #Displaying the query:
        st.write(DA1)
        collection_name = 'stores'
        collection = db[collection_name] 
        # Parameter Streamlit so that the DA can parameter the query in a menu (here they can choose the value of store_nbr they want for the query):
        unique_store_nbr_values = collection.distinct('store_nbr')
        selected_store_nbr = st.selectbox("Choose the store_nbr", unique_store_nbr_values, index=0)
        #Once the DA has set the parameter they want for the query, the query runs : 
        if st.button("Run Query 1 (DA)"):   
            pipeline = DA1
            # Displaying the result as a dataframe 
            result = list(collection.aggregate(pipeline))
            df_da1 = pd.DataFrame(result)
            st.write("This query returns the number of items sold out of all the items from the store 1 during snow days.")
            st.write(df_da1)

    elif query_choice == "Query 2 (DA)":
        st.write("You choose Query 2 (DA):")
        #Displaying the query:
        st.write(DA2)
        collection_name = 'stores'
        collection = db[collection_name] 
        # Parameter Streamlit so that the DA can parameter the query in a menu (here they can choose the value of store_nbr they want for the query):
        unique_store_nbr_values = collection.distinct('store_nbr')
        selected_store_nbr = st.selectbox("Choose the store_nbr", unique_store_nbr_values, index=None)
        #Once the DA has set the parameter they want for the query, the query runs : 
        if st.button("Run Query 2 (DA)"):   
            pipeline = [
                {
                    '$match': {
                        'store_nbr': selected_store_nbr # Parameter the query by setting this value
                    }
                }, {
                    '$lookup': {
                        'from': 'weather', 
                        'localField': 'station_nbr', 
                        'foreignField': 'station_nbr', 
                        'as': 'weather_info'
                    }
                }, {
                    '$unwind': '$weather_info'
                }, {
                    '$match': {
                        'weather_info.snowfall': {
                            '$gt': 2
                        }
                    }
                }, {
                    '$lookup': {
                        'from': 'sales', 
                        'let': {
                            'store_nbr': '$store_nbr', 
                            'weather_date': '$weather_info.date'
                        }, 
                        'pipeline': [
                            {
                                '$match': {
                                    '$expr': {
                                        '$and': [
                                            {
                                                '$eq': [
                                                    '$store_nbr', '$$store_nbr'
                                                ]
                                            }, {
                                                '$eq': [
                                                    '$date', '$$weather_date'
                                                ]
                                            }
                                        ]
                                    }
                                }
                            }
                        ], 
                        'as': 'sales_info'
                    }
                }, {
                    '$unwind': '$sales_info'
                }, {
                    '$group': {
                        '_id': '$store_nbr', 
                        'total_units_sold': {
                        '$sum': '$sales_info.units'
                        }
                    }
                },{
                                '$sort': {'total_units': -1} 
                            }
            ]
            # Displaying the result as a dataframe and the execution time 
            start_time = time.time()
            result = list(collection.aggregate(pipeline))
            end_time = time.time()
            execution_time = end_time - start_time
            df_da2 = pd.DataFrame(result)
            st.write("This query returns the number of items sold out of all the items from the store 1 during snow days.")
            st.write(df_da2)
            st.write(f"Execution time : {execution_time} seconds")

    elif query_choice == "Query 1 (End-User)":
        st.write("You choose Query 1 (End-User)")
        if st.button("Run Query 1 (End-User)"):
            collection_name = 'sales'
            collection = db[collection_name]           
            pipeline = EU1
            # Displaying the result as a dataframe and the execution time 
            start_time = time.time()
            result = list(collection.aggregate(pipeline))
            end_time = time.time()
            execution_time = end_time - start_time
            df_eu1 = pd.DataFrame(result)
            st.write("This query returns the number of sales of item_nbr 5 across all stores in the month of January.")
            st.write(df_eu1[ 'total_units'])
            st.write(df_eu1)
            st.write(f"Execution time : {execution_time} seconds")
       
    elif query_choice == "Query 2 (End-User)":
        st.write("You choose Query 2 (End-User)")
        if st.button("Run Query 2 (End-User)"):
            collection_name = 'sales'
            collection = db[collection_name]           
            pipeline = EU2
            # Displaying the result as a dataframe and the execution time 
            start_time = time.time()
            result = list(collection.aggregate(pipeline))
            end_time = time.time()
            execution_time = end_time - start_time
            df_eu2 = pd.DataFrame(result)
            st.write("This query returns the number of sales of all items from the store 1 in the month of February.")
            st.write(df_eu2[['item_nbr', 'total_units']])
            st.write(f"Execution time : {execution_time} seconds")

    elif query_choice == "Query 3 (End-User)":
        st.write("You choose Query 3 (End-User)")
        if st.button("Run Query 3 (End-User)"):
            collection_name = 'sales'
            collection = db[collection_name]           
            pipeline = EU3
            # Displaying the result as a dataframe and the execution time 
            start_time = time.time()
            result = list(collection.aggregate(pipeline))
            end_time = time.time()
            execution_time = end_time - start_time
            df_eu3 = pd.DataFrame(result)
            st.write("This query returns the number of sales of all items from the store 1 in the month of February.")
            st.write(df_eu3[['item_nbr', 'total_units']])
            st.write(f"Execution time : {execution_time} seconds")

    elif query_choice == "Query 4 (End-User)":
            # Displaying the result as a dataframe and the execution time 
        st.write("You choose Query 4 (End-User)")
        if st.button("Run Query 4 (End-User)"):
            collection_name = 'sales'
            collection = db[collection_name]           
            pipeline = EU4
            # Displaying the result as a dataframe and the execution time 
            start_time = time.time()
            result = list(collection.aggregate(pipeline))
            end_time = time.time()
            execution_time = end_time - start_time
            df_eu4 = pd.DataFrame(result)
            st.write("This query returns the number of sales of item_nbr 5 across all stores in the month of January.")
            st.write(df_eu4[['store_nbr', 'total_units']])
            st.write(f"Execution time : {execution_time} seconds")

        

###########################################     Function for performance measurements      #########################################################
# def page_performance_measurement():
#     st.subheader("Performance Measurement")
#     # Ajoutez ici la logique pour la Peformance Measurement pour l'utilisateur interne

#     st.write("Select the query you want to evaluate:")
#     query_choice = st.selectbox("Choose a Data Analyst Query", ("Query 1 (DA)", "Query 2 (DA)", "Query 1 (End-User)", "Query 2 (End-User)", "Query 3 (End-User)", "Query 4 (End-User)"), index=None)

#     if query_choice == "Query 1 (DA)":
#         # Ajoutez ici la logique pour la Query 1 pour l'utilisateur interne
#         st.write("You choose Query 1 (DA)")
#     elif query_choice == "Query 2 (DA)":
#         # Ajoutez ici la logique pour la Query 2 pour l'utilisateur interne
#         st.write("You choose Query 2 (DA)")
#     elif query_choice == "Query 1 (End-User)":
#         # Ajoutez ici la logique pour la Query 1 pour l'utilisateur End-User
#         collection_name = 'sales'
#         pipeline = [
#             {
#                 '$match': {
#                     'store_nbr': 1, 
#                     'item_nbr': 9
#                 }
#             },
#             {
#                 '$group': {
#                     '_id': None, 
#                     'total_units': {
#                         '$sum': '$units'
#                     }
#                 }
#             },
#             {
#                 '$project': {
#                     '_id': 0, 
#                     'total_units': 1
#                 }
#             }
#                 ]
        
#         st.write("You choose Query 1 (End-User)")
#         st.code("""pipeline = [
#             {
#                 '$match': {
#                     'store_nbr': 1, 
#                     'item_nbr': 9
#                 }
#             },
#             {
#                 '$group': {
#                     '_id': None, 
#                     'total_units': {
#                         '$sum': '$units'
#                     }
#                 }
#             },
#             {
#                 '$project': {
#                     '_id': 0, 
#                     'total_units': 1
#                 }
#             }
#             ]""")

#     num_iterations = st.number_input("Number of iterations for Peformance Measurement", value=10)

#     if st.button("Start Peformance Measurement"):
        

#         avg_execution_times = []
# ################################### CHANGER RANGE(1,7) ###################################################
#         shards_list = list(range(1, 7))
#         plt.figure(figsize=(10, 6))

#         for num_shards in shards_list:
#             collection = db[collection_name]

#             execution_times = []

#             for i in range(num_iterations):
#                 start_time = time.time()
#                 result = list(collection.aggregate(pipeline))
#                 end_time = time.time()
#                 execution_time = end_time - start_time
#                 execution_times.append(execution_time)

#             execution_times = sorted(execution_times)[1:-1]
#             average_execution_time = sum(execution_times) / len(execution_times)
#             avg_execution_times.append(average_execution_time)

#             st.write(f"Average execution time with {num_shards} shards :", average_execution_time, "seconds")

#             # client.close()
#         # Create a Plotly Express scatter plot
#         fig = px.scatter(x=shards_list, y=avg_execution_times, labels={'x': 'Shards', 'y': 'Average Execution Time'},
#                         title='My Plot', template='plotly_dark')

#         # Set background color of the plot area
#         fig.update_layout(plot_bgcolor='rgba(0,0,0,0)')  # Full transparency

#         # Display the plot in Streamlit
#         st.plotly_chart(fig)
#         # fig, ax = plt.subplots()
#         # fig.patch.set_facecolor(st.get_option("theme.primaryColor"))

#         # # Plot the data
#         # ax.plot(shards_list, avg_execution_times, marker='o', linestyle='-', color='lightblue')
#         # ax.set_facecolor(("#FFFFFF"))  # Full transparency
#         # ax.yaxis.grid(False)
#         # # ax.xaxis
#         # # Set plot labels and title
#         # ax.set_xlabel('Shards')
#         # ax.set_ylabel('Average Execution Time')
#         # ax.set_title('Average execution time depending of the number of Shards')
#         # st.pyplot(fig)

#         # Plot des temps d'exécution moyens en fonction du nombre de shards
#         # plt.plot(shards_list, avg_execution_times, marker='o', linestyle='-', color='blue')
#         # fig.patch.set_facecolor(st.get_option("theme.primaryColor"))
#         # plt.xlabel('Number of Shards')
#         # plt.ylabel('Mean execution time (s)')
#         # plt.title('Mean execution time depending of the number of Shards')
#         # st.pyplot(plt)

###########################################     Function for actions and views limited to administrators      #########################################################

def data_stat_admin():
    stat  = db.command("dbstats")
    datasize = stat['dataSize'] / 1024
    objects = stat['objects']
    collections = stat['collections']
    st.write("Database Distribution Statistics  : ")
    st.write('\n')
    st.write('Objects:', str(objects))
    st.write('Collections:', str(collections))
    st.write('Size:', str(datasize) + ' Mb')

    st.write('Sales collection stats : ')
    stats = db.command("collStats", "sales")
    subset_stats = {
    'Namespace': stats['ns'],
    'Size': stats['size'],
    'Storage Size': stats['storageSize'],
    'Number of Documents': stats['count'],
    'Average Document Size': stats['avgObjSize'],
    }
    st.write(subset_stats)
    st.write('\n')

    st.write('Stores collection stats : ')
    stats = db.command("collStats", "stores")
    subset_stats = {
    'Namespace': stats['ns'],
    'Size': stats['size'],
    'Storage Size': stats['storageSize'],
    'Number of Documents': stats['count'],
    'Average Document Size': stats['avgObjSize'],
    }
    st.write(subset_stats)
    st.write('\n')

    st.write('Weather collection stats : ')
    stats = db.command("collStats", "weather")
    subset_stats = {
    'Namespace': stats['ns'],
    'Size': stats['size'],
    'Storage Size': stats['storageSize'],
    'Number of Documents': stats['count'],
    'Average Document Size': stats['avgObjSize'],
    }
    st.write(subset_stats)
    
def cluster_state():
    cluster_state = client.admin.command("serverStatus")
    st.write('Cluster state : ', cluster_state)


def data_repartition():
    st.write("Un-charded database")

def indexes():
    st.write("SALES COLLECTION INDEXES : ")
    stats = db.command("collStats", "sales")
    st.write(f"Total Index Size : {stats['totalIndexSize']}")
    st.write(f"Number of Indexes: {stats['nindexes']}")
    indexes = db['sales'].list_indexes()
    st.write('Index names : ')
    for index in indexes:
        st.write(f" - Index Name: {index['name']}")

    st.write("STORES COLLECTION INDEXES : ")
    stats = db.command("collStats", "stores")
    st.write(f"Total Index Size : {stats['totalIndexSize']}")
    st.write(f"Number of Indexes: {stats['nindexes']}")
    indexes = db['stores'].list_indexes()
    for index in indexes:
        st.write(f" - Index Name: {index['name']}")

    st.write("WEATHER COLLECTION INDEXES : ")
    stats = db.command("collStats", "weather")
    st.write(f"Total Index Size : {stats['totalIndexSize']}")
    st.write(f"Number of Indexes: {stats['nindexes']}")
    indexes = db['weather'].list_indexes()
    for index in indexes:
        st.write(f" - Index Name: {index['name']}")

def page_admin():
    st.title("Administrator")
    onglet_selectionne = st.sidebar.selectbox("Navigation", ("Data Distribution Statistics", "Cluster State", "Data Repartition", "Indexes"), index=None)

    if onglet_selectionne == "Data Distribution Statistics":
        data_stat_admin()

    if onglet_selectionne == "Cluster State":
        cluster_state()
    if onglet_selectionne == "Data Repartition":
        data_repartition()
    if onglet_selectionne == "Indexes":
        indexes()


#######################################       User Interface  Streamlit       ##########################################
st.title("Walmart Weather 🌧")  
# st.set_page_config(page_title="Walmart Weather 🌧", layout="wide", bg_color="lightblue")
user_level = st.selectbox("Select your user level ", ("End-User", "Data Analyst", "Administrator"), index=None)

# if st.button("Show Content"):
if user_level == "Data Analyst":
    page_data_analyst()
elif user_level == "End-User":
    page_end_user()
elif user_level == "Administrator":
    page_admin()
