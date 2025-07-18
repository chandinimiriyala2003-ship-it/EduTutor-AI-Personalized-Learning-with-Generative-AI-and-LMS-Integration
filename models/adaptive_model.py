def adapt_quiz_difficulty(score):
    if score > 80:
        return "Advanced"
    elif score > 50:
        return "Intermediate"
    return "Beginner"