import streamlit as st
from job import jobs  # Importer le dictionnaire jobs depuis job.py


# Fonctions utilitaires
def calculate_score(responses):
    """Calcule le score en fonction des réponses."""
    return responses.count("Oui")


def generate_job_mapping(score, total_questions):
    """Génère le pourcentage de correspondance pour un métier."""
    percentage = int((score / total_questions) * 100)
    return f"Votre correspondance avec le métier est de {percentage}%."


def get_next_question(current_question_index, questions):
    """Retourne l'index de la prochaine question, ou None s'il n'en reste plus."""
    if current_question_index < len(questions) - 1:
        return current_question_index + 1
    return None


def create_job_visualization(job_suggestions):
    """Placeholder pour la visualisation des suggestions métier."""
    st.write("Visualisation des suggestions métier :")
    for job, percentage in job_suggestions.items():
        st.write(f"- {job}: {percentage}%")


# Interface utilisateur Streamlit
st.title("Découvrez votre métier idéal en IT 🚀")
st.write("Répondez aux questions pour découvrir le métier correspondant à vos attitudes !")

# Collecter les réponses de l'utilisateur
responses = {}
for category, roles in jobs.items():
    st.subheader(f"Catégorie : {category}")
    for role, attitudes in roles.items():
        st.markdown(f"### Métier : {role}")
        role_responses = []

        for i, question in enumerate(attitudes):
            response = st.radio(question, ("Oui", "Non"), key=f"{role}_{i}")
            role_responses.append(response)

        # Calculer le score pour chaque métier
        score = calculate_score(role_responses)
        total_questions = len(role_responses)
        responses[role] = {
            "score": score,
            "total_questions": total_questions,
        }

# Afficher les résultats une fois les réponses soumises
if st.button("Voir mes résultats"):
    st.write("### Résultats")
    job_suggestions = {}
    for role, data in responses.items():
        score = data["score"]
        total_questions = data["total_questions"]
        percentage = int((score / total_questions) * 100)
        job_suggestions[role] = percentage
        st.write(f"**{role}** : {score} / {total_questions} questions répondues 'Oui' ({percentage}%).")

    # Visualisation des suggestions
    create_job_visualization(job_suggestions)
