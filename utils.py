def calculate_score(responses):
    return responses.count("Oui")

def generate_job_mapping(score, total_questions):
    percentage = int((score / total_questions) * 100)
    return f"Votre correspondance avec le métier est de {percentage}%."

def get_next_question(current_question_index, questions):
    if current_question_index < len(questions) - 1:
        return current_question_index + 1
    return None

def create_job_visualization(job_suggestions):
    # Placeholder for job mapping visualization logic
    pass
