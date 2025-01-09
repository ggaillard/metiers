import streamlit as st
from job import jobs


# Fonction pour obtenir les questions et rôles
def get_next_question():
    for category, roles in jobs.items():
        for role, questions in roles.items():
            for question in questions:
                yield question, role


# Initialisation de l'état de session
if 'current_question' not in st.session_state:
    st.session_state.current_question = 0
if 'responses' not in st.session_state:
    st.session_state.responses = []


# Fonction principale pour gérer les pages
def main():
    st.title("Quiz : Quel métier est fait pour vous ?")

    # Navigation entre les pages
    page = st.sidebar.selectbox("Choisissez une page :", ["Accueil", "Questionnaire", "Résultats"])

    if page == "Accueil":
        page_accueil()
    elif page == "Questionnaire":
        page_questionnaire()
    elif page == "Résultats":
        page_resultats()


# Page d'accueil
def page_accueil():
    st.header("Bienvenue sur l'application de découverte des métiers !")
    st.write("Répondez à quelques questions simples pour découvrir quel métier pourrait vous correspondre.")
    st.write("Cliquez sur **Questionnaire** dans la barre latérale pour commencer.")


# Page questionnaire
def page_questionnaire():
    st.header("Répondez aux questions suivantes")
    questions = list(get_next_question())

    # Vérification des index pour éviter les dépassements
    if st.session_state.current_question < len(questions):
        question, role = questions[st.session_state.current_question]
        response = st.radio(question, ["Oui", "Non"])

        # Si l'utilisateur appuie sur "Suivant"
        if st.button("Suivant"):
            st.session_state.responses.append((question, response, role))
            st.session_state.current_question += 1

            # Recharge la page si d'autres questions restent
            if st.session_state.current_question < len(questions):
                st.experimental_rerun()
    else:
        st.write("Vous avez terminé le questionnaire. Rendez-vous dans l'onglet **Résultats** pour découvrir votre métier idéal.")


# Page résultats
def page_resultats():
    st.header("Résultats du quiz")

    if not st.session_state.responses:
        st.write("Vous n'avez pas encore répondu aux questions. Allez dans l'onglet **Questionnaire** pour commencer.")
        return

    # Calcul des scores pour chaque métier
    role_scores = {}
    for question, response, role in st.session_state.responses:
        if response == "Oui":
            role_scores[role] = role_scores.get(role, 0) + 1

    # Affichage des résultats
    if role_scores:
        best_role = max(role_scores, key=role_scores.get)
        st.write(f"Votre métier idéal est : **{best_role}**")
        st.write("Détail des scores par métier :")
        for role, score in role_scores.items():
            st.write(f"- **{role}** : {score} points")
    else:
        st.write("Aucun métier ne correspond à vos réponses.")

    # Bouton pour recommencer
    if st.button("Recommencer"):
        st.session_state.current_question = 0
        st.session_state.responses = []
        st.experimental_rerun()


# Exécution de l'application
if __name__ == "__main__":
    main()
