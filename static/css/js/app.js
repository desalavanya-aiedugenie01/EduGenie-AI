async function sendRequest(url, inputId, resultId) {
    const input = document.getElementById(inputId);
    const result = document.getElementById(resultId);

    const text = input.value.trim();

    if (!text) {
        result.innerHTML = `
            <div class="error">
                Please enter something first.
            </div>
        `;
        return;
    }

    result.innerHTML = `
        <div class="loading">
            Generating answer...
        </div>
    `;

    try {
        const response = await fetch(url, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                text: text
            })
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Something went wrong.");
        }

        result.innerHTML = `
            <div class="result-box">
                ${formatText(data.result)}
            </div>
        `;

    } catch (error) {
        result.innerHTML = `
            <div class="error">
                ${error.message}
            </div>
        `;
    }
}


function formatText(text) {
    if (!text) {
        return "No answer received.";
    }

    return text
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/\n/g, "<br>");
}


function askQuestion() {
    sendRequest(
        "/qa",
        "question",
        "questionResult"
    );
}


function explainConcept() {
    sendRequest(
        "/explain",
        "concept",
        "explanationResult"
    );
}


function generateQuiz() {
    sendRequest(
        "/quiz",
        "quizTopic",
        "quizResult"
    );
}


function summarizeText() {
    sendRequest(
        "/summarize",
        "summaryText",
        "summaryResult"
    );
}


function getLearningPath() {
    sendRequest(
        "/learn/recommendations",
        "learningTopic",
        "learningResult"
    );
}