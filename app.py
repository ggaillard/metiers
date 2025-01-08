import streamlit as st

# Dictionnaire des métiers et attitudes
jobs = {
    "Support et administration IT": {
        "Technicien(ne) support informatique": [
            "Aimer résoudre des problèmes techniques",
            "Être patient(e) et pédagogue",
            "Avoir une bonne capacité d'écoute",
            "Savoir diagnostiquer rapidement les pannes",
            "Aimer travailler en contact direct avec les utilisateurs",
            "Être méthodique dans la résolution des problèmes",
            "Avoir une bonne maîtrise des outils bureautiques",
            "Être réactif(ve) face aux urgences",
            "Savoir gérer le stress des utilisateurs",
            "Aimer apprendre de nouvelles technologies"
        ],
        "Technicien(ne) systèmes et réseaux": [
            "Aimer configurer des équipements réseau",
            "Savoir diagnostiquer les dysfonctionnements systèmes",
            "Être rigoureux(se) dans la gestion des infrastructures",
            "Avoir un esprit logique et méthodique",
            "Aimer travailler en équipe",
            "Savoir documenter les procédures techniques",
            "Être curieux(se) des nouvelles technologies",
            "Être à l'aise avec le travail sur le terrain",
            "Savoir gérer les priorités des interventions",
            "Aimer optimiser les performances des systèmes"
        ],
        "Administrateur(trice) systèmes et réseaux": [
            "Être responsable et autonome",
            "Aimer assurer la disponibilité des systèmes",
            "Avoir une bonne maîtrise des environnements serveurs",
            "Savoir sécuriser les infrastructures informatiques",
            "Être réactif(ve) face aux incidents critiques",
            "Savoir travailler en équipe sur des projets complexes",
            "Être méthodique dans la gestion des mises à jour",
            "Aimer documenter les processus et configurations",
            "Être curieux(se) des nouvelles tendances en IT",
            "Avoir un esprit analytique pour résoudre les problèmes"
        ]
    },
    "Développement et programmation": {
        "Développeur(se) d'applications": [
            "Aimer créer des logiciels innovants",
            "Être rigoureux(se) dans l'écriture du code",
            "Savoir analyser les besoins des utilisateurs",
            "Être curieux(se) des nouvelles technologies",
            "Aimer résoudre des problèmes complexes",
            "Savoir travailler en équipe avec d'autres développeurs",
            "Avoir un esprit créatif pour proposer des solutions",
            "Être patient(e) face aux défis techniques",
            "Savoir tester et corriger les bugs efficacement",
            "Être organisé(e) dans la gestion des projets"
        ],
        "Développeur(se) web": [
            "Aimer créer des interfaces utilisateur attrayantes",
            "Avoir une bonne maîtrise des langages front-end",
            "Être curieux(se) des tendances web",
            "Aimer travailler sur des projets interactifs",
            "Être rigoureux(se) dans le respect des standards web",
            "Savoir optimiser les performances des sites",
            "Avoir un bon sens esthétique",
            "Savoir travailler en équipe avec des designers",
            "Être patient(e) dans la résolution des problèmes",
            "Aimer apprendre de nouveaux outils"
        ],
        "Développeur(se) mobile": [
            "Aimer concevoir des applications mobiles",
            "Avoir une bonne maîtrise des langages natifs (iOS, Android)",
            "Être curieux(se) des tendances mobiles",
            "Aimer résoudre des défis liés à l'optimisation",
            "Être rigoureux(se) dans le développement multiplateforme",
            "Savoir travailler avec des API",
            "Être créatif(ve) pour répondre aux attentes des utilisateurs",
            "Aimer tester les applications sur différents appareils",
            "Savoir résoudre rapidement les bugs",
            "Aimer apprendre de nouvelles technologies mobiles"
        ],
        "Intégrateur(trice) web": [
            "Aimer assembler des éléments graphiques et techniques",
            "Savoir respecter les maquettes fournies",
            "Être rigoureux(se) dans l'intégration du code",
            "Avoir une bonne maîtrise des langages front-end",
            "Aimer travailler en collaboration avec des designers",
            "Être curieux(se) des nouvelles pratiques web",
            "Savoir optimiser le rendu sur différents navigateurs",
            "Aimer résoudre des problèmes de compatibilité",
            "Être patient(e) dans la résolution des erreurs",
            "Savoir gérer les deadlines de projets"
        ],
        "Ingénieur(e) en machine learning": [
            "Aimer concevoir des algorithmes complexes",
            "Être à l’aise avec les mathématiques",
            "Avoir une curiosité pour l’apprentissage automatique",
            "Savoir résoudre des problèmes liés aux données",
            "Être rigoureux(se) dans l’implémentation des modèles",
            "Aimer travailler avec des équipes de data scientists",
            "Savoir tester les modèles pour assurer leur efficacité",
            "Être curieux(se) des dernières innovations en IA",
            "Avoir une capacité d’analyse avancée",
            "Savoir présenter des résultats complexes de façon simple"
        ],
        "Data analyst": [
            "Aimer analyser des données",
            "Être rigoureux(se) dans les calculs",
            "Savoir poser les bonnes questions",
            "Aimer communiquer des insights",
            "Savoir utiliser des outils BI",
            "Être curieux(se) des chiffres",
            "Aimer collaborer avec les métiers",
            "Être logique et méthodique",
            "Savoir repérer des tendances",
            "Être attentif(ve) aux détails"
        ]
    },
    "Cybersécurité": {
        "Consultant(e) en sécurité informatique": [
            "Aimer conseiller sur la cybersécurité",
            "Être méthodique dans les audits",
            "Savoir détecter les vulnérabilités",
            "Être à l’aise avec les normes ISO",
            "Savoir documenter les processus",
            "Aimer résoudre des problèmes complexes",
            "Être curieux(se) des nouvelles menaces",
            "Savoir former des équipes",
            "Être à l’écoute des besoins clients",
            "Être rigoureux(se) sur les détails"
        ]
    }
}

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
