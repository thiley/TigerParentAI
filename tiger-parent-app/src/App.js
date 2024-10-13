import React from "react";
import Chatbot from "react-chatbot-kit";
import "react-chatbot-kit/build/main.css"
import "./App.css"; 
import ActionProvider from "./ActionProvider";
import MessageParser from "./MessageParser";
import config from "./config";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <div className="chatbot-container">
          <Chatbot
            config={config}
            actionProvider={ActionProvider}
            messageParser={MessageParser}
          />
        </div>
      </header>
    </div>
  );
}

export default App;
