console.log("GPTwrapper script loaded!");

async function sendQuestion() {
    const input = document.querySelector('.input-box');
    const responseArea = document.getElementById('response');
    const question = input.value.trim();

    if (!question) {
        alert('Please enter a question about sports!');
        return;
    }

    // Show loading state
    responseArea.innerHTML = 'Thinking...';

    try {
        // TODO: Replace with your actual API endpoint
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ question: question })
        });

        const data = await response.json();
        responseArea.innerHTML = data.answer || 'Sorry, I couldn\'t process your question.';
    } catch (error) {
        console.error('Error:', error);
        responseArea.innerHTML = 'Sorry, there was an error processing your question.';
    }
}

// Add event listener for Enter key
document.querySelector('.input-box').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendQuestion();
    }
});
