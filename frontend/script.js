function syncCourses() {
    const topic = prompt("Enter topic for quiz:");

    fetch("http://127.0.0.1:5000/generate_quiz", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ topic: topic })
    })
    .then(response => response.json())
    .then(data => {
        alert("Quiz generated:\n" + JSON.stringify(data.questions, null, 2));
    })
    .catch(error => {
        console.error("Error:", error);
        alert("Failed to generate quiz.");
    });
}
