class ActionProvider {
  constructor(createChatBotMessage, setStateFunc) {
    this.createChatBotMessage = createChatBotMessage;
    this.setState = setStateFunc;
  }

  greet() {
    const greetingMessage = this.createChatBotMessage("Hi, friend.");
    this.updateChatbotState(greetingMessage);
  }

  updateChatbotState(message) {
    this.setState(prevState => ({
      ...prevState,
      messages: [...prevState.messages, message],
    }));
  }

  // Override the default message rendering to use custom components
  handleCustomMessage(message, sender) {
    return (
      <div className={`chatbot-message ${sender}-message`}>
        <div className={`${sender}-profile`}>
          {sender === "bot" ? "B" : "U"}
        </div>
        <div>{message}</div>
      </div>
    );
  }
}

export default ActionProvider