def generate_quiz(topic):
    return {
        "topic": topic,
        "questions": [{"q": f"What is {topic}?", "a": "Sample Answer"}]
    }