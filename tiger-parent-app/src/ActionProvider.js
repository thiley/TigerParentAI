class ActionProvider {
  constructor(createChatBotMessage, setStateFunc) {
    this.createChatBotMessage = createChatBotMessage;
    this.setState = setStateFunc;
  }


  handleCustomMessage(message, sender) {
    const customMessage = this.createChatBotMessage(message);
    this.updateChatbotState(customMessage);
  }

  updateChatbotState(message) {
    this.setState(prevState => ({
      ...prevState,
      messages: [...prevState.messages, message],
    }));
  }  
}

export default ActionProvider