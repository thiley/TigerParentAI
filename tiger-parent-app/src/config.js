import { createChatBotMessage } from 'react-chatbot-kit';
import AngryParentAvatar from './angryManAvatar';

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
  customComponents: {
    header: () => <div>TigerParentAI</div>, // This replaces the default header
    botAvatar: (props) => <AngryParentAvatar {...props} />, //custom bot avatar
  },
  
}

export default config