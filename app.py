# to run the app : streamlit run app.py
# to have the correct version  : pipreqs --encoding=utf8 --force


import streamlit as st  # pip install streamlit
from owlready2 import *

#---- Importation of the class and functions


# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/ 
st.set_page_config(page_title="Ontology Project", page_icon=":clapper:", layout="wide")

# ---- READ CSV ----

path=r"ontolgy/ProjectV3.owl"

onto = get_ontology(path).load()

sync_reasoner()
st.write("load effective")

query="""PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX mv: <http://www.semanticweb.org/esilv/ontologies/2023/2/untitled-ontology-20#>

SELECT ?actor
WHERE {
	?actor rdf:type mv:Actor
}
"""


results = list(default_world.sparql(query))

st.write(len(results))
for result in results:
  st.write(result)


# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
