# to run the app : streamlit run app.py
# to have the correct version  : pipreqs --encoding=utf8 --force


import streamlit as st  # pip install streamlit
from owlready2 import *
from requetes import dictionnaire

#owlready2.JAVA_EXE = "C:\\path\\to\\java.exe"

#---- Importation of the class and functions


# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/ 
st.set_page_config(page_title="Ontology Project", page_icon=":clapper:", layout="wide")

# Chemin 

path="ontolgy/ProjectV3.owl"

onto = get_ontology(path).load()

#sync_reasoner_pellet(onto)
sync_reasoner()

world = onto.world

st.write("load effective")

for key in dictionnaire.keys():
  if len(dictionnaire[key])>70:
    st.write("----")
    st.write(key)
    results = list(world.sparql(dictionnaire[key]))
    res=[ str(result[0])[10:] for result in results]
    for r in res:
      st.write(str(r))




# ---- HIDE STREAMLIT STYLE ----
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
