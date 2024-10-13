class MessageParser {
  constructor(actionProvider) {
    this.actionProvider = actionProvider;
  }

  async parse(message) {
    try{
      //send the user input to Flask server via POST request
    const response = await fetch("http://127.0.0.1:5000/response_text", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ input: message})
    });

    // Parse the JSON response from the Flask server
    const data = await response.json();

    // Check if the server returned an error
    if (data.error) {
      this.actionProvider.handleCustomMessage("Error: " + data.error, "bot");
      return;
    }

    // Pass the GPT response to the ActionProvider to update the chatbot state
    this.actionProvider.handleCustomMessage(data.response, "bot");

    } catch (error) {
    // Handle any network or server errors
    this.actionProvider.handleCustomMessage("Error: Failed to fetch response.", "bot");
    }
  }
}

export default MessageParser;

  
