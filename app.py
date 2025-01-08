import streamlit as st
from job import jobs  # Importer le dictionnaire jobs depuis job.py


# Interface utilisateur Streamlit
st.title("Découvrez votre métier idéal en IT 🚀")
st.write("Répondez aux questions pour découvrir le métier correspondant à vos attitudes !")

selected_job = st.selectbox("Choisissez une catégorie :", list(jobs.keys()))

if selected_job:
    selected_role = st.selectbox("Choisissez un métier :", list(jobs[selected_job].keys()))

if selected_role:
    st.subheader(f"Questions pour : {selected_role}")
    attitudes = jobs[selected_job][selected_role]
    responses = []

    for attitude in attitudes:
        response = st.radio(attitude, ("Oui", "Non"))
        responses.append(response)

    if st.button("Voir mon résultat"):
        score = responses.count("Oui")
        st.write(f"Vous avez répondu 'Oui' à {score} / {len(attitudes)} questions.")
        st.write(f"Votre correspondance avec le métier de **{selected_role}** est de {int((score / len(attitudes)) * 100)}%.")
