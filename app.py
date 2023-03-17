# to run the app : streamlit run app.py
# to have the correct version  : pipreqs --encoding=utf8 --force


import streamlit as st  # pip install streamlit
from owlready2 import *
from requetes import dictionnaire 
import pandas as pd
import re
import random


#---- Importation of the class and functions

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/ 
st.set_page_config(page_title="Ontology Project", page_icon=":clapper:", layout="wide")

# Chemin 

path="ontolgy/ProjectV5.owl"
#path="C:/Users/leodu/OneDrive/Documents/Projects/Projet_ontology/ontolgy/ProjectV3.owl"

onto = get_ontology(path).load()

st.sidebar.write("Load effective")

l="""with onto:
  sync_reasoner_pellet()
  st.sidebar.write("Reasonner active")"""


world = onto.world

def display_sparql_results(c, query_key,title, column_names):
    # Récupérer la requête SPARQL à partir de la clé du dictionnaire
    query = dictionnaire[query_key]
    
    # Exécuter la requête SPARQL
    results = list(world.sparql(query))
    
    # Créer un DataFrame à partir des résultats et des noms de colonnes
    df = pd.DataFrame(results, columns=column_names)
    df=df.astype(str)
    df = df.replace({'ProjectV5\.':''}, regex=True)
    # Afficher le DataFrame dans un expander
    json_file = df.to_json()
    

    with c.expander(title, expanded=False):
        st.write(df)
        st.download_button(
          label="Download data as JSON",
          data=json_file,
          file_name='data'+str(random.random())+'.json',
          mime='text/json',
      )






st.title(":movie_camera: Movies ontology presentation")

st.markdown("#")


title = st.text_input('Movie Title', 'Interstellar')


with open(path, "r") as f:
    
    data = f.read()

    Person = re.findall(r'<ClassAssertion>\s+<Class IRI="#MovieWorkers"/>\s+<NamedIndividual IRI="#([^"]+)"/>', data)

    match = re.search(f'<NamedIndividual IRI="#{title}"/>', data)

    genre = re.findall(rf'<DataProperty IRI="#genre"/>\s+<NamedIndividual IRI="#{title}"/>\s+<Literal>([^<]+)</Literal>', data)

    country = re.findall(rf'<DataProperty IRI="#country"/>\s+<NamedIndividual IRI="#{title}"/>\s+<Literal>([^<]+)</Literal>', data)

    year = re.findall(rf'<DataProperty IRI="#year"/>\s+<NamedIndividual IRI="#{title}"/>\s+<Literal datatypeIRI="http://www.w3.org/2001/XMLSchema#int">([^<]+)</Literal>', data)

    if match:
        st.write(f"{title} is mentioned in the OWL file and it's genre {genre} and in the countries {country} and created in {year[0]}.")
    else:
        st.write(f"{title} is not mentioned in the OWL file.")


with st.expander("List of Persons", expanded=False):
  df=pd.DataFrame(Person, columns=["Person"])
  st.write(df)
  json_file = df.to_json()
  st.download_button(
    label="Download data as JSON",
    data=json_file,
    file_name='data'+str(random.random())+'.json',
    mime='text/json',
  )
st.write("----")

c_1,c_2=st.columns(2)


display_sparql_results(c_1, "List_the_instances_of_the_class_Actor","List of actors", ["Actors"])


display_sparql_results(c_2, "List_the_name_of_all_Thriller_movies","List of the directors of thriller movies", ["Directors","Movies"])

st.write("----")

c_1,c_2=st.columns(2)

display_sparql_results(c_1, "List_the_name_of_Actors_older_than_51_years","List of actors older than 51", ["Actors"])

display_sparql_results(c_2, "List_the_name_of_all_Crime_Thriller_movies","List name of thriller and crime movies", ["Movies","Genres"])

st.write("----")

c_1,c_2=st.columns(2)

display_sparql_results(c_1, "List_of_movies_that_are_played_in_theater_for_a_specific_day","Movies that are played in a theater for a specific day", ["Theatre", "Movie", "Day"])

display_sparql_results(c_2, "A_query_that_contains_at_least_2_Optional_Graph_Patterns","Movies and Actors that are show in a theatre", ["Movie", "Actor" ,"Theatre"])
st.write("----")



# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
