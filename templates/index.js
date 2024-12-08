function sendMessage() {
  const messageInput = document.getElementById('message-input');
  const chatHistory = document.getElementById('chat-history');

  const message = messageInput.value;
  messageInput.value = '';

  // Send the message to the server using fetch API
  fetch('/chat', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    },
    body: `message=${message}`
  })
  .then(response => response.json())
  .then(data => {
    // Append the user's message to the chat history
    const userMessage = document.createElement('div');
    userMessage.textContent = `You: ${message}`;
    chatHistory.appendChild(userMessage);

    // Append the AI's response to the chat history
    const aiResponse = document.createElement('div');
    aiResponse.textContent = `AI: ${data.response}`;
    chatHistory.appendChild(aiResponse);
  })
  .catch(error => {
    console.error('Error:', error);
    // Handle errors, e.g., display an error message to the user
  });
}
