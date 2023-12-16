# import streamlit as st
# from pymongo import MongoClient
# import time

# # Connexion à la base de données MongoDB
# client = MongoClient('mongodb://localhost:27017/')  # Mettez votre URI MongoDB ici
# db = client['Walmart_cloud']  # Remplacez 'nom_de_votre_database' par le nom de votre base de données

# # Fonction pour la page utilisateur interne
# def page_utilisateur_interne():
#     st.title("Utilisateur Interne")

#     # Onglets de navigation pour l'utilisateur interne
#     onglet_selectionne = st.sidebar.selectbox("Navigation", ("Mesure de Performance", "Autre Option", "Requête"))

#     if onglet_selectionne == "Mesure de Performance":
#         st.subheader("Mesure de Performance")

#         st.write("Exemple de pipeline à exécuter :")
#         st.code("""
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
#         ]
#         """)

#         num_iterations = st.number_input("Nombre d'itérations pour la mesure de performance", value=1)

#         if st.button("Lancer la mesure de performance"):
#             collection = db['sales']  # Remplacez 'votre_collection' par le nom de votre collection
#             pipeline = [  # Insérez ici le pipeline donné
#                 # Votre pipeline donné ici...
#             ]

#             execution_times = []

#             for i in range(num_iterations):
#                 start_time = time.time()
#                 result = list(collection.aggregate(pipeline))
#                 end_time = time.time()
#                 execution_time = end_time - start_time
#                 execution_times.append(execution_time)

#                 # Afficher le résultat de la première itération (à des fins de vérification)
#                 if i == 0:
#                     st.write("Résultat de la requête (première itération) :", result)

#             st.write(f"Temps d'exécution moyen sur {num_iterations} itérations :", sum(execution_times) / len(execution_times), "secondes")

#         # Ajoutez ici d'autres composants pour d'autres fonctionnalités pour l'utilisateur interne

#     elif onglet_selectionne == "Autre Option":
#         st.subheader("Autre Option")
#         # Ajoutez ici d'autres composants pour d'autres fonctionnalités pour l'utilisateur interne

#     elif onglet_selectionne == "Requête":
#         st.subheader("Requête")
#         # Ajoutez ici les composants pour les requêtes spécifiques à l'utilisateur interne vers MongoDB
#         # Par exemple, des champs de saisie pour les requêtes, des boutons pour lancer les requêtes, etc.

# # Fonction pour la page utilisateur externe
# def page_utilisateur_externe():
#     st.title("Utilisateur Externe")
#     # Ajoutez ici les composants de l'interface pour les utilisateurs externes
#     # ... (vous pouvez ajouter un onglet de requête pour les utilisateurs externes si nécessaire)

# # Interface utilisateur Streamlit
# st.title("Walmart Weather 🌧")

# user_level = st.selectbox("Sélectionnez votre niveau d'utilisateur", ("Interne", "Externe"))

# if user_level == "Interne":
#     page_utilisateur_interne()
# elif user_level == "Externe":
#     page_utilisateur_externe()








##############################################################################




import matplotlib.pyplot as plt
import streamlit as st
from pymongo import MongoClient
import time

# Increase message size limit
# st.set_option('server.maxMessageSize', 500)  # Set the value according to your needs

# Connection to the MongoDB database
client = MongoClient('mongodb://localhost:27017/')
db = client['WalmartWeather']

# Function for the internal user page
def page_internal_user():
    st.title("Utilisateur Interne")

    # Onglets de navigation pour l'utilisateur interne
    onglet_selectionne = st.sidebar.selectbox("Navigation", ("Mesure de Performance", "Autre Option", "Requête"))

    if onglet_selectionne == "Mesure de Performance":
        st.subheader("Mesure de Performance")

        st.write("Exemple de pipeline à exécuter :")
        st.code("""
        # Votre pipeline donné ici...
        """)

        num_iterations = st.number_input("Nombre d'itérations pour la mesure de performance", value=10)

        if st.button("Lancer la mesure de performance"):
            mongo_host = 'localhost'
            mongo_port = 27017
            mongo_database = 'WalmartWeather'
            collection_name = 'sales'

            avg_execution_times = []

            shards_list = list(range(1, 7))
            plt.figure(figsize=(10, 6))

            for num_shards in shards_list:
                client = MongoClient(f'mongodb://{mongo_host}:{mongo_port}/')
                db = client[mongo_database]
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

                st.write(f"Temps d'exécution moyen avec {num_shards} shards :", average_execution_time, "secondes")

                client.close()

            # Plot des temps d'exécution moyens en fonction du nombre de shards
            plt.plot(shards_list, avg_execution_times, marker='o', linestyle='-', color='blue')
            plt.xlabel('Nombre de Shards')
            plt.ylabel('Temps d\'exécution moyen (s)')
            plt.title('Temps d\'exécution moyen en fonction du nombre de Shards')
            st.pyplot(plt)

        # Ajoutez ici d'autres composants pour d'autres fonctionnalités pour l'utilisateur interne

    elif onglet_selectionne == "Autre Option":
        st.subheader("Autre Option")
        # Ajoutez ici d'autres composants pour d'autres fonctionnalités pour l'utilisateur interne

    elif onglet_selectionne == "Requête":
        st.subheader("Requête")
        # Ajoutez ici les composants pour les requêtes spécifiques à l'utilisateur interne
        # Par exemple, des champs de saisie pour les requêtes, des boutons pour lancer les requêtes, etc.

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
