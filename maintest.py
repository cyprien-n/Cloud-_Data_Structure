import streamlit as st
from pymongo import MongoClient
import time
import matplotlib.pyplot as plt

# Connexion à la base de données MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['WalmartWeather']

# Fonction pour les requêtes spécifiques pour l'utilisateur interne
def internal_queries():
    st.subheader("Requêtes Internes")
    query_choice = st.selectbox("Choisissez une requête interne", ("Requête 1 (Interne)", "Requête 2 (Interne)", "Requête 1 (Externe)", "Requête 2 (Externe)", "Requête 3 (Externe)", "Requête 4 (Externe)"))

    if query_choice == "Requête 1 (Interne)":
        # Ajoutez ici la logique pour la requête 1 pour l'utilisateur interne
        st.write("Vous avez choisi la Requête 1 (Interne)")
    elif query_choice == "Requête 2 (Interne)":
        # Ajoutez ici la logique pour la requête 2 pour l'utilisateur interne
        st.write("Vous avez choisi la Requête 2 (Interne)")
    elif query_choice == "Requête 1 (Externe)":
        # Ajoutez ici la logique pour la requête 1 pour l'utilisateur externe
        st.write("Vous avez choisi la Requête 1 (Externe)")
        if st.button("Afficher la Requête 1 (Externe)"):
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
    elif query_choice == "Requête 2 (Externe)":
        # Ajoutez ici la logique pour la requête 2 pour l'utilisateur externe
        st.write("Vous avez choisi la Requête 2 (Externe)")
    elif query_choice == "Requête 3 (Externe)":
        # Ajoutez ici la logique pour la requête 3 pour l'utilisateur externe
        st.write("Vous avez choisi la Requête 3 (Externe)")
    elif query_choice == "Requête 4 (Externe)":
        # Ajoutez ici la logique pour la requête 4 pour l'utilisateur externe
        st.write("Vous avez choisi la Requête 4 (Externe)")

# Fonction pour les requêtes spécifiques pour l'utilisateur externe
def external_queries():
    st.subheader("Requêtes Externes")
    query_choice = st.selectbox("Choisissez une requête externe", ("Requête 1 (Externe)", "Requête 2 (Externe)", "Requête 3 (Externe)", "Requête 4 (Externe)"))

    if query_choice == "Requête 1 (Externe)":
        # Ajoutez ici la logique pour la Requête 1 pour l'utilisateur externe
        st.write("Vous avez choisi la Requête 1 (Externe)")
        if st.button("Afficher la Requête 1 (Externe)"):
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
    elif query_choice == "Requête 2 (Externe)":
        # Ajoutez ici la logique pour la Requête 2 pour l'utilisateur externe
        st.write("Vous avez choisi la Requête 2 (Externe)")
    elif query_choice == "Requête 3 (Externe)":
        # Ajoutez ici la logique pour la Requête 3 pour l'utilisateur externe
        st.write("Vous avez choisi la Requête 3 (Externe)")
    elif query_choice == "Requête 4 (Externe)":
        # Ajoutez ici la logique pour la Requête 4 pour l'utilisateur externe
        st.write("Vous avez choisi la Requête 4 (Externe)")

# Fonction pour la page utilisateur interne
def page_internal_user():
    st.title("Utilisateur Interne")

    onglet_selectionne = st.sidebar.selectbox("Navigation", ("Requête", "Mesure de Performance", "Autre option"))

    if onglet_selectionne == "Mesure de Performance":
        st.subheader("Mesure de Performance")
        # Ajoutez ici la logique pour la mesure de performance pour l'utilisateur interne
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
    elif onglet_selectionne == "Autre Option":
        st.subheader("Autre Option")
        # Ajoutez ici d'autres composants pour d'autres fonctionnalités pour l'utilisateur interne

    elif onglet_selectionne == "Requête":
        internal_queries()

# Fonction pour la page utilisateur externe
def page_external_user():
    st.title("Utilisateur Externe")

    onglet_selectionne = st.sidebar.selectbox("Navigation", ("Requête", "Autre option"))

    if onglet_selectionne == "Autre Option":
        st.subheader("Autre Option")
        # Ajoutez ici d'autres composants pour d'autres fonctionnalités pour l'utilisateur externe

    elif onglet_selectionne == "Requête":
        external_queries()

# Interface utilisateur Streamlit
st.title("Walmart Weather 🌧")  

user_level = st.selectbox("Sélectionnez votre niveau d'utilisateur", ("Interne", "Externe"))

if user_level == "Interne":
    page_internal_user()
elif user_level == "Externe":
    page_external_user()
