import streamlit as st
import streamlit_authenticator as stauth
import streamlit_option_menu as som
from pathlib import Path

# On intègre un CSS personnalisé
css_path = Path(__file__).parent / "streamlit.css"
if css_path.exists():
    with open(css_path, encoding="utf-8") as f:
        css_content = f.read()
    st.markdown(f"<style>{css_content}</style>", unsafe_allow_html=True)
else:
    st.warning(f"CSS file not found at: {css_path}")

# Notre home page (recherche films) 
def page1():
    # Je créé trois colonnes pour centrer le contenu
    lay_gauche, lay_centre, lay_droit = st.columns([1, 20, 1])

    # titre
    with lay_centre:
        # box stylisée pour le titre et les filtres
        st.markdown('<div class="main-box">', unsafe_allow_html=True)
        st.markdown('<h1 class="main-title">Recherche de films A&E</h1>', unsafe_allow_html=True)

        # Filtres container (inside the styled box)
        with st.container():
            st.subheader("Filtres")

            # colonnes des filtres principaux
            but_gauche, but_centre, but_droit = st.columns(3)
            with but_gauche:
                st.text_input("Mot-clef", key="filter_keyword")
                st.selectbox("Note", options=["Any", ">= 5", ">= 7", ">= 9"], key="filter_note")
            with but_centre:
                st.text_input("Acteur", key="filter_actor")
                st.selectbox("Popularité", options=["Any", "Low", "Medium", "High"], key="filter_popularity")
            with but_droit:
                st.text_input("Réalisateur", key="filter_director")
                st.number_input("Année", min_value=1900, max_value=2100, value=2020, step=1, key="filter_year")

            st.write("Genre")
            # Genres comme toggle button dans des petites colonnes
            but_a, but_b, but_c, but_d, but_e = st.columns(5)
            with but_a:
                st.checkbox("A", key="genre_a")
                st.checkbox("F", key="genre_f")
            with but_b:
                st.checkbox("B", key="genre_b")
                st.checkbox("G", key="genre_g")
            with but_c:
                st.checkbox("C", key="genre_c")
                st.checkbox("H", key="genre_h")
            with but_d:
                st.checkbox("D", key="genre_d")
                st.checkbox("I", key="genre_i")
            with but_e:
                st.checkbox("E", key="genre_e")
                st.checkbox("J", key="genre_j")

        # Close the main box
        st.markdown('</div>', unsafe_allow_html=True)
def page2():
    st.write("Un petit test pour du multipage app")
    st.image("https://media.makeameme.org/created/impressive-2y23ct.jpg", width=600)

def page3():
    st.write("Un autre petit test pour du multipage app")
    st.image("https://i.pinimg.com/564x/56/b9/a9/56b9a962f481a4212bce3f82b151433d.jpg", width=600)

pages = [
        st.Page(page1, icon="📽️", title="Recherche A&E"),
        st.Page(page2, icon="🎭", title="Le ciné en délire"),
        st.Page(page3, icon="🤡", title="A&E tracker by WCS"),
    ]
    # Setup de la navigation
st.set_page_config(layout="wide")
current_page = st.navigation(pages=pages, position="hidden")

    # Setup du menu
num_cols_menu = max(len(pages) + 1, 8)
columns_menu = st.columns(num_cols_menu, vertical_alignment="bottom")
columns_menu[0].write("**Menu**")
for col, page in zip(columns_menu[1:-1], pages):
    col.page_link(page, icon=page.icon)
current_page.run()
