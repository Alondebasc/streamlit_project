import streamlit as st
from PIL import Image, ImageOps, ImageDraw
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import pandas as pd
import seaborn as sns
import folium
from streamlit_folium import folium_static
from geopy.geocoders import Nominatim
import plotly.express as px


# Chargement de l'image de profil
profile_image = Image.open("Alonpdp.jpg")

# Créer un masque circulaire pour l'image avec une meilleure qualité
mask_size = (min(profile_image.size),) * 2  # Utiliser une taille carrée basée sur la dimension minimale
mask = Image.new('L', mask_size, 0)
draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0) + mask_size, fill=255)

# Redimensionner l'image de profil pour correspondre au masque
profile_image = ImageOps.fit(profile_image, mask_size, centering=(0.5, 0.5))
profile_image.putalpha(mask)

# Configuration de la page Streamlit
st.set_page_config(page_title="Alon Debasc - Ingénieur Data", page_icon="🚀", layout="wide")

# Style global
st.markdown(
    """
    <style>
    body {color: #CCCCCC; background-color: #1e1e1e;}
    .sidebar .sidebar-content {background-color: #333333;}
    h1, h2, h3, h4 {color: #FFD700;}
    .stMetricLabel {font-size: 1.5em;}
    </style>
    """,
    unsafe_allow_html=True
)

# Barre latérale de navigation avec profil personnel
st.sidebar.image(profile_image, width=150)
st.sidebar.title("Alon Debasc 👨‍💻")
st.sidebar.write("Ingénieur Data & Intelligence Artificielle")
st.sidebar.markdown("---")

st.sidebar.write(
    """
    - 📞 *Téléphone*: +33 (0)6 79 04 39 61
    - 📧 *Email*: [alon.debasc@efrei.net](mailto:alon.debasc@efrei.net)
    - 🔗 [LinkedIn](https://www.linkedin.com/in/alon-debasc-17737b223/?originalSubdomain=fr)
    - 🔗 [GitHub](https://github.com/alon-debasc)
    """
)

# Navigation avec onglets
choice = st.sidebar.radio("Navigation", ["Portfolio", "CV", "Analyse Dataset"])
st.sidebar.markdown("---")

# Palette de couleurs personnalisée
primary_color = "#FFD700"  # Jaune doré
secondary_color = "#81D8D0"  # Bleu clair

# Fonction pour styliser les titres
def style_title(title):
    st.markdown(f"<h2 style='color: {primary_color};'>{title}</h2>", unsafe_allow_html=True)

def style_subtitle(subtitle):
    st.markdown(f"<h3 style='color: {secondary_color};'>{subtitle}</h3>", unsafe_allow_html=True)

def style_project(title, technologies, description, learnings, skills):
    st.markdown(f"<h4 style='color: {secondary_color};'>{title}</h4>", unsafe_allow_html=True)
    st.markdown(f"<p><strong>Technologies :</strong> {technologies}</p>", unsafe_allow_html=True)
    st.markdown(f"<p><strong>Description :</strong> {description}</p>", unsafe_allow_html=True)
    st.markdown(f"<p><strong>Ce que j'ai appris :</strong> {learnings}</p>", unsafe_allow_html=True)
    st.markdown(f"<p><strong>Compétences débloquées :</strong> {skills}</p>", unsafe_allow_html=True)
    st.markdown("<hr style='border:1px solid #444;'>", unsafe_allow_html=True)

# Page Portfolio
if choice == "Portfolio":
    st.image(profile_image, width=150, use_column_width='auto')
    style_title("Alon Debasc")
    style_subtitle("Ingénieur Data & Intelligence Artificielle")

    # Présentation du portfolio avec des styles plus attrayants
    style_title("Bienvenue dans mon Portfolio")
    st.write("Ce portfolio regroupe les projets et réalisations qui reflètent mon expertise en ingénierie des données et en intelligence artificielle.")
    st.write("Je cherche à démontrer mes compétences à travers des projets significatifs qui mettent en avant ma capacité à résoudre des problèmes concrets, ma créativité et mon expertise technique.")
    st.markdown("<hr style='border:2px solid #333;'>", unsafe_allow_html=True)

    # Exemple de réalisations avec des sections plus dynamiques
    style_title("Mes Réalisations")

    style_project(
        "SWAPAWS - Marketplace d'achat revente",
        "React, MySQL, Python",
        "Développement d'une plateforme permettant aux utilisateurs d'acheter, vendre ou échanger des produits, avec un système de matching automatisé.",
        "Gestion d'une équipe technique, amélioration des compétences en développement web, et compréhension approfondie des systèmes de matching.",
        "Leadership, gestion de projet, développement front-end et back-end, compréhension des besoins utilisateurs."
    )

    style_project(
        "SOWESKIP - Application de file d'attente virtuelle",
        "React, MySQL, Python, QR Code API",
        "Conception d'un système permettant aux utilisateurs de rejoindre une file d'attente en scannant un QR code, évitant ainsi l'attente physique.",
        "Expérience utilisateur, optimisation des processus, et création d'applications interconnectées.",
        "Développement orienté utilisateur, intégration d'API, optimisation d'applications."
    )

    style_project(
        "Projet Mastercamp Data Science",
        "Python, FastText, Pandas, Scikit-learn",
        "Traitement et classification de brevets en utilisant le modèle FastText pour une classification automatique précise.",
        "Manipulation de grandes bases de données, apprentissage automatique supervisé et non supervisé, utilisation d'algorithmes NLP avancés.",
        "Traitement de texte, classification de données, gestion de projets de data science en équipe."
    )

# Page CV
elif choice == "CV":
    style_title("Curriculum Vitae")
    st.image(profile_image, width=150, use_column_width='auto')
    style_subtitle("Alon Debasc - Ingénieur Data & Intelligence Artificielle")

    col1, col2 = st.columns(2)
    with col1:
        st.write("### 📞 Contact")
        st.markdown(f"<p><strong>Téléphone :</strong> +33 (0)6 79 04 39 61</p>", unsafe_allow_html=True)
        st.markdown(f"<p><strong>Email :</strong> <a href='mailto:alon.debasc@efrei.net' style='color:{primary_color};'>alon.debasc@efrei.net</a></p>", unsafe_allow_html=True)
        st.markdown(f"<p><strong>LinkedIn :</strong> <a href='https://www.linkedin.com/in/alon-debasc-17737b223/?originalSubdomain=fr' style='color:{primary_color};'>linkedin.com/in/alon-debasc</a></p>", unsafe_allow_html=True)
    
    with col2:
        style_subtitle("Formation")
        st.write("EFREI Paris - Panthéon Assas (2021 - 2026)")
        st.write("Cycle ingénieur Data Engineering, 4ème année Majeure Big Data et Intelligence Artificielle.")
        st.write("Concordia University (Septembre - Décembre 2023 🇨🇦)")
        st.write("Semestre d’échange à Montréal.")
    
    st.markdown("---")

    style_subtitle("Expériences Professionnelles")
    st.write("- Business Manager - INTM Belgium (Stage Juillet - Août 2024)\n  Prospection commerciale et recrutement à Bruxelles, avec communication en anglais.")
    st.write("- Business Developer - LOGTEAM (CDD Janvier - Juin 2023)\n  Développement de portefeuille client, prospection à froid, recherche et prise de rendez-vous.")
    st.write("- Consultant Recrutement - LOGTEAM (CDD Juin - Juillet 2023)\n  Recrutement, scraping, gestion des candidats et coordination d'événements.")
    st.markdown("---")

    style_subtitle("Compétences")
    skills = {
        "Langages de programmation": 7,
        "Développement web": 7,
        "Bases de données": 7,
        "Gestion de projet": 9,
        "Gestion d'équipe": 9,
        "Prospection commerciale": 8,
        "Communication": 9
    }
    labels = list(skills.keys())
    values = list(skills.values())

    # Créer un graphique radar pour les compétences
    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values + [values[0]],
        theta=labels + [labels[0]],
        fill='toself',
        name='Compétences',
        line_color=primary_color
    ))
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10],
                showticklabels=True,
                tickfont=dict(color='#333333')  # Changer la couleur des étiquettes pour les rendre visibles
            )
        ),
        showlegend=False
    )
    st.plotly_chart(fig)

    # Ajouter les langues parlées
    style_subtitle("Langues Parlées")
    st.write("- Français 🇫🇷 : Langue maternelle")
    st.write("- Anglais 🇬🇧 : Courant")
    st.write("- Espagnol 🇪🇸 : Notions")

    # Graphique des compétences linguistiques
    style_subtitle("Niveau de Compétence Linguistique")
    languages = ["Français", "Anglais", "Espagnol"]
    levels = [10, 8, 5]

    fig, ax = plt.subplots(figsize=(8, 4))
    ax.barh(languages, levels, color=secondary_color)
    ax.set_xlabel("Niveau de Compétence (sur 10)")
    ax.set_title("Compétences Linguistiques")
    st.pyplot(fig)
    st.markdown("---")

    # Ajouter les hobbies
    style_subtitle("Hobbies")
    st.write("- ⚽ Football (Foot salle)")
    st.write("- 🎭 Cinéma : Science-fiction, Comédie")
    st.write("- 👟 Mode : Sneakers, Streetwear")
    st.write("- ✈ Voyages : Canada, États-Unis, Caraïbes")
    st.write("- 🥋 Krav Maga : Ceinture verte")
    st.markdown("---")

# Page Analyse Dataset
if choice == "Analyse Dataset":
    style_title("Analyse du Dataset : Index Égalité Professionnelle F/H")

    # Contexte du dataset et choix de l'analyse
    with st.container():
        style_subtitle("Contexte et Choix du Dataset")
        col1, col2 = st.columns(2)
        with col1:
            st.write("L'index Égalité Professionnelle entre les femmes et les hommes est une initiative visant à mesurer l'engagement des entreprises pour réduire les inégalités professionnelles. Ce dataset regroupe des données provenant d'entreprises de plus de 50 salariés en France. J'ai choisi ce dataset car il permet de mettre en lumière des enjeux sociétaux cruciaux, notamment l'égalité des genres, et d'identifier les entreprises qui se distinguent dans ce domaine.")
            st.write("L'objectif est de fournir une vision claire des tendances actuelles et des progrès réalisés en matière d'égalité salariale et professionnelle, ainsi que de voir comment les entreprises peuvent améliorer leurs politiques.")
        with col2:
            st.metric(label="Nombre total de lignes", value="151,763")
            st.metric(label="Nombre de variables", value="17")

    st.markdown("---")

    # Charger le fichier Excel fourni
    try:
        df = pd.read_excel("index-egalite-fh.xlsx")
    except FileNotFoundError:
        st.error("Le fichier 'index-egalite-fh.xlsx' est introuvable. Assurez-vous qu'il est bien placé dans le répertoire du script.")
        st.stop()
    except Exception as e:
        st.error(f"Erreur lors du chargement du fichier : {e}")
        st.stop()

    # Aperçu du Dataset
    st.write("### Aperçu du Dataset")
    st.dataframe(df.head())

    # Description du Dataset
    style_subtitle("Variables Clés du Dataset")
    st.write("""
        - *Année* : L'année à laquelle l'index a été mesuré.
        - *Structure* : Type de structure (Entreprise, Groupe, etc.).
        - *Tranche d'effectifs* : Catégorisation par taille de l'entreprise (50-250, 251-999, 1000 et plus).
        - *Région et Département* : Localisation géographique des entreprises.
        - *Code NAF* : Activité économique de l'entreprise.
        - *Note Ecart rémunération, Note Index* : Différents indicateurs d'égalité professionnelle.
    """)

    st.markdown("---")

    # Conversion des colonnes nécessaires en numériques pour éviter les erreurs
    try:
        df['Note Index'] = pd.to_numeric(df['Note Index'], errors='coerce')
        df['Note Ecart rémunération'] = pd.to_numeric(df['Note Ecart rémunération'], errors='coerce')
    except KeyError as e:
        st.error(f"La colonne suivante est manquante dans le dataset : {e}")
        st.stop()

    # --- Ajout des filtres interactifs ---
    st.sidebar.header("Options de Filtrage")
    
    # Filtres pour les différentes colonnes
    selected_regions = st.sidebar.multiselect("Sélectionner une Région :", options=df['Région'].unique(), default=df['Région'].unique())
    selected_tranches_effectifs = st.sidebar.multiselect("Sélectionner une Tranche d'Effectifs :", options=df['Tranche d\'effectifs'].unique(), default=df['Tranche d\'effectifs'].unique())
    selected_years = st.sidebar.slider("Sélectionner l'Année :", int(df['Année'].min()), int(df['Année'].max()), (int(df['Année'].min()), int(df['Année'].max())))

    # Filtrer le dataframe selon les choix
    filtered_df = df[
        (df['Région'].isin(selected_regions)) & 
        (df['Tranche d\'effectifs'].isin(selected_tranches_effectifs)) & 
        (df['Année'] >= selected_years[0]) & 
        (df['Année'] <= selected_years[1])
    ]

      # --- Ajout de la Carte de Position avec Taux d'Égalité par Région ---
    style_subtitle("Répartition Géographique du Taux d'Égalité Professionnelle par Région")
    geolocator = Nominatim(user_agent="geoapiExercises")

    # Initialiser la carte
    m = folium.Map(location=[46.603354, 1.888334], zoom_start=5)

    # Ajouter des points sur la carte pour les régions sélectionnées avec taux d'égalité
    if 'Région' in filtered_df.columns and 'Note Index' in filtered_df.columns:
        region_data = filtered_df.groupby('Région')['Note Index'].mean().dropna()
        for region, note_index in region_data.items():
            try:
                location = geolocator.geocode(region + ", France")
                if location:
                    folium.CircleMarker(
                        location=[location.latitude, location.longitude],
                        radius=note_index / 10,  # Taille du cercle proportionnelle au taux d'égalité
                        popup=f"Région: {region}<br>Note Index: {note_index:.2f}",
                        color='blue',
                        fill=True,
                        fill_color='blue'
                    ).add_to(m)
            except:
                pass

    folium_static(m)

    st.markdown("---")


    # --- Visualisations avec Plotly pour un rendu plus esthétique et interactif ---

    # Répartition des Notes de l'Index par Région
    style_subtitle("Répartition des Notes de l'Index par Région")
    st.write("Cette visualisation permet de voir si certaines régions se démarquent par rapport à l'égalité professionnelle. Cela pourrait indiquer un effet des politiques régionales ou des initiatives spécifiques.")
    if 'Région' in filtered_df.columns and 'Note Index' in filtered_df.columns:
        fig = px.bar(
            filtered_df.groupby('Région')['Note Index'].mean().reset_index(),
            x='Note Index',
            y='Région',
            orientation='h',
            title="Moyenne des Notes de l'Index par Région",
            labels={"Note Index": "Note Moyenne de l'Index", "Région": "Région"},
            template="plotly_white",
            color_discrete_sequence=[secondary_color]
        )
        fig.update_layout(title_font_size=20, title_font_family="Arial", title_x=0.5)
        st.plotly_chart(fig)

    # Comparaison des Notes de l'Index par Tranche d'effectifs
    style_subtitle("Comparaison des Notes de l'Index par Tranche d'effectifs")
    st.write("Cette visualisation montre l'impact de la taille de l'entreprise sur les performances en matière d'égalité professionnelle.")
    if 'Tranche d\'effectifs' in filtered_df.columns and 'Note Index' in filtered_df.columns:
        fig = px.box(
            filtered_df,
            x='Tranche d\'effectifs',
            y='Note Index',
            title="Répartition des Notes de l'Index par Tranche d'effectifs",
            labels={"Tranche d\'effectifs": "Tranche d'effectifs", "Note Index": "Note de l'Index"},
            template="plotly_white",
            color_discrete_sequence=[secondary_color]
        )
        fig.update_layout(title_font_size=20, title_font_family="Arial", title_x=0.5)
        st.plotly_chart(fig)

    # Corrélation entre les Notes d'Écart de rémunération et l'Index global
    style_subtitle("Corrélation entre l'Écart de rémunération et la Note de l'Index")
    st.write("Cette corrélation met en évidence l'importance de la rémunération équitable.")
    if 'Note Ecart rémunération' in filtered_df.columns and 'Note Index' in filtered_df.columns:
        fig = px.scatter(
            filtered_df,
            x='Note Ecart rémunération',
            y='Note Index',
            title="Corrélation entre la Note d'Écart de Rémunération et la Note de l'Index",
            labels={"Note Ecart rémunération": "Note Écart de Rémunération", "Note Index": "Note de l'Index"},
            template="plotly_white",
            color_discrete_sequence=[secondary_color]
        )
        fig.update_layout(title_font_size=20, title_font_family="Arial", title_x=0.5)
        st.plotly_chart(fig)

    # Évolution des Notes de l'Index dans le Temps (par Année)
    style_subtitle("Évolution des Notes de l'Index dans le Temps")
    st.write("Cette analyse montre l'évolution des scores d'égalité professionnelle au fil des années. Une tendance à la hausse montre que les efforts des entreprises et les politiques publiques ont porté leurs fruits.")
    if 'Année' in df.columns and 'Note Index' in df.columns:
        fig = px.line(
            df.groupby('Année')['Note Index'].mean().reset_index(),
            x='Année',
            y='Note Index',
            title="Évolution des Notes de l'Index au Fil des Années",
            labels={"Année": "Année", "Note Index": "Note Moyenne de l'Index"},
            template="plotly_white",
            color_discrete_sequence=[secondary_color]
        )
        fig.update_layout(title_font_size=20, title_font_family="Arial", title_x=0.5)
        st.plotly_chart(fig)

    # Conclusion
    style_subtitle("Conclusion")
    st.write("Cette analyse met en évidence les disparités de l'égalité professionnelle dans les différentes régions de France et les différences entre les tranches d'effectifs. Les entreprises qui réduisent les écarts de rémunération obtiennent de meilleures notes, soulignant l'importance d'une politique salariale équitable. Les efforts collectifs et les politiques publiques ont porté leurs fruits, mais des améliorations sont encore possibles, en particulier pour les entreprises de taille moyenne qui rencontrent des difficultés. L'avenir de l'égalité professionnelle semble prometteur, mais nécessite des engagements continus.")
