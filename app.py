import streamlit as st
from job import jobs  # Importer le dictionnaire jobs depuis job.py

# Interface utilisateur Streamlit
st.title("Découvrez votre métier idéal en IT 🚀")
st.write("Répondez à toutes les questions pour découvrir le métier qui correspond le mieux à vos attitudes !")

responses = {}  # Dictionnaire pour stocker les réponses

# Parcourir toutes les catégories et métiers
for category, roles in jobs.items():
    st.subheader(f"Catégorie : {category}")
    for role, attitudes in roles.items():
        st.markdown(f"### Métier : {role}")
        responses[role] = []  # Initialiser les réponses pour ce métier

        # Afficher les questions et collecter les réponses
        for attitude in attitudes:
            response = st.radio(f"{attitude} ({role})", ("Oui", "Non"), key=f"{role}_{attitude}")
            responses[role].append(response)

# Bouton pour afficher les résultats
if st.button("Voir mes résultats"):
    st.write("### Résultats")
    for role, role_responses in responses.items():
        score = role_responses.count("Oui")
        total_questions = len(role_responses)
        percentage = int((score / total_questions) * 100) if total_questions > 0 else 0
        st.write(f"**{role}** : {score} / {total_questions} questions répondues 'Oui' ({percentage}%).")
