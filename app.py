import streamlit as st
from job import jobs

# Configuration de la navigation entre les pages
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Aller à", ["Accueil", "Questionnaire", "Résultats"])

    if page == "Accueil":
        page_home()
    elif page == "Questionnaire":
        page_questionnaire()
    elif page == "Résultats":
        page_results()

# Page d'accueil
def page_home():
    st.title("Bienvenue dans le Questionnaire de Métier")
    st.write("""
        Ce questionnaire vous aide à découvrir le métier qui correspond le mieux à vos intérêts.
        Cliquez sur **Questionnaire** dans le menu de navigation pour commencer.
    """)

# Page du questionnaire
def page_questionnaire():
    # Initialisation de l'état de session
    if "current_question" not in st.session_state:
        st.session_state.current_question = 0
    if "responses" not in st.session_state:
        st.session_state.responses = []

    # Génération de toutes les questions
    def get_all_questions():
        for category, roles in jobs.items():
            for role, questions in roles.items():
                for question in questions:
                    yield question, role

    questions = list(get_all_questions())

    # Affichage de la question actuelle
    if st.session_state.current_question < len(questions):
        question, role = questions[st.session_state.current_question]
        st.subheader(f"Question {st.session_state.current_question + 1}/{len(questions)}")
        response = st.radio(f"{question} ({role})", ("Oui", "Non"))

        if st.button("Suivant"):
            # Sauvegarder la réponse
            st.session_state.responses.append((question, response, role))
            st.session_state.current_question += 1
            st.experimental_rerun()
    else:
        st.write("Vous avez répondu à toutes les questions.")
        if st.button("Voir les résultats"):
            st.experimental_rerun()

# Page des résultats
def page_results():
    if "responses" not in st.session_state or not st.session_state.responses:
        st.write("Vous n'avez pas encore répondu au questionnaire. Rendez-vous sur la page **Questionnaire** pour commencer.")
        return

    # Calcul des scores pour chaque rôle
    role_scores = {}
    for _, response, role in st.session_state.responses:
        if response == "Oui":
            role_scores[role] = role_scores.get(role, 0) + 1

    # Affichage des résultats
    if role_scores:
        best_role = max(role_scores, key=role_scores.get)
        total_questions = sum([len(questions) for roles in jobs.values() for questions in roles.values()])
        score = role_scores[best_role]
        st.success(f"Votre métier idéal est : **{best_role}**")
        st.write(generate_job_mapping(score, total_questions))

        # Visualisation des scores
        st.subheader("Suggestions de métiers")
        st.bar_chart(role_scores)
    else:
        st.warning("Aucun métier ne correspond à vos réponses. Essayez de répondre à nouveau.")

    # Bouton pour recommencer
    if st.button("Recommencer"):
        st.session_state.current_question = 0
        st.session_state.responses = []
        st.experimental_rerun()

# Fonction pour calculer le score de correspondance
def generate_job_mapping(score, total_questions):
    percentage = int((score / total_questions) * 100)
    return f"Votre correspondance avec le métier est de {percentage}%."

# Exécution de l'application
if __name__ == "__main__":
    main()
