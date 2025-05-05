def ask_question(question: str) -> bool:
    response = input(question + " (yes/no): ").lower().strip()
    return response == "yes"


def diagnose():
    print("\nAnswer the following questions to determine your illness.")
    
    itching_or_swelling = ask_question("Do you experience any itching or swelling?")
    red_watery_eyes = ask_question("Do you have red, watery eyes?")
    temperature_above_37_5 = ask_question("Do you have a temperature above 37.5°C?")
    chills = ask_question("Do you experience chills?")
    runny_or_stuffy_nose = ask_question("Do you have a runny or stuffy nose?")
    sneezing = ask_question("Are you sneezing frequently?")
    body_aches = ask_question("Do you have body aches?")
    tired_or_fatigued = ask_question("Do you feel tired or fatigued?")
    temperature_above_38 = ask_question("Do you have a temperature above 38°C?")
    sore_throat = ask_question("Do you have a sore throat?")
    swollen_tonsils = ask_question("Are your tonsils swollen?")
    nauseous = ask_question("Do you feel nauseous?")
    vomiting = ask_question("Have you been vomiting?")
    diarrhea = ask_question("Do you have diarrhea?")
    severe_abdominal_pain = ask_question("Do you have severe abdominal pain?")
    lost_appetite = ask_question("Have you lost your appetite?")
    
    print("\nDiagnosis:")
    if itching_or_swelling or red_watery_eyes:
        print("- You might have allergies.")
    if temperature_above_37_5 or chills:
        print("- You might have a fever.")
    if runny_or_stuffy_nose or sneezing:
        print("- You might have a cold.")
    if body_aches and tired_or_fatigued and temperature_above_38:
        print("- You might have the flu.")
    if sore_throat and swollen_tonsils:
        print("- You might have strep throat.")
    if nauseous and vomiting and diarrhea:
        print("- You might have food poisoning.")
    if severe_abdominal_pain and lost_appetite:
        print("- You might have appendicitis.")

    print("- If none of the above matched your symptoms, consult a doctor for more accurate diagnosis.")


print("Welcome to the Expert System for Diagnosing Illnesses!")
diagnose()
