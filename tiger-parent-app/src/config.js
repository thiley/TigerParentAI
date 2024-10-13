import { createChatBotMessage } from 'react-chatbot-kit';

const config = { 
  botName: "TigerParentAI",
  initialMessages: [createChatBotMessage("What you want la? Why you no studying?")],
  customStyles: {
    botMessageBox: {
      backgroundColor: "#376B7E",
    },
    chatButton: {
      backgroundColor: "#376B7E",
    },
  },
}

export default config