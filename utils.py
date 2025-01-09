def calculate_score(responses):
    """
    Calcule le score total basé sur les réponses.
    """
    return responses.count("Oui")

def generate_job_mapping(score, total_questions):
    """
    Génère une phrase décrivant la correspondance avec un métier basé sur le score.
    """
    if total_questions == 0:
        return "Aucune question n'a été posée pour calculer une correspondance."
    percentage = int((score / total_questions) * 100)
    return f"Votre correspondance avec le métier est de {percentage}%."

def get_next_question(current_question_index, questions):
    """
    Retourne l'indice de la prochaine question ou None si toutes les questions ont été posées.
    """
    if current_question_index < len(questions) - 1:
        return current_question_index + 1
    return None

def create_job_visualization(job_suggestions):
    """
    Placeholder pour la logique de visualisation des suggestions de métier.
    Ici, on pourrait utiliser des bibliothèques comme matplotlib ou plotly pour afficher des graphiques.
    """
    # Exemple d'utilisation avec Streamlit pour afficher un graphique
    import streamlit as st
    if job_suggestions:
        st.bar_chart(job_suggestions)
    else:
        st.write("Aucune suggestion de métier à visualiser.")

