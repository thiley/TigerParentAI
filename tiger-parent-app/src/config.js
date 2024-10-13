import { createChatBotMessage } from 'react-chatbot-kit';

const config = { 
  botName: "TigerParentAI",
  initialMessages: [createChatBotMessage("What you want la? Why you no studying?")],
  customStyles: {
    botMessageBox: {
      backgroundColor: "#000000",
    },
    chatButton: {
      backgroundColor: "#000000",
    },
  },
}

export default config