import React, { useEffect, useRef, useState } from "react";
import { chat, get_Response } from "../services/api";
// import '../App.css'
const ChatWindow = ({ messages, setMessages }) => {
  const [response, setResponse] = useState([])
  const chatEndRef = useRef<HTMLDivElement | null>(null);
    const [input, setInput] = useState("");
     useEffect(() => {
        chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
      }, [response]);
    async function get_documents() {
    const formData = new FormData()
    formData.append('msg', input)
    const response = await chat(formData);
    console.log(response.data);
}
 async function postMsg() {
    const formData = new FormData()
    formData.append('msg', input)
    const response = await chat({'msg': input});
    console.log(response)
    const fianl_response = await get_Response()
    setResponse(fianl_response?.data.history)
}
    return (
    <div className="chat-window" style={{ height: "400px", overflowY: "auto" }}>
  
  <h2>Chat History</h2>

  <div className="chat-messages">
    {response?.map((msg, index) => (
      <div
        key={index}
        style={{
          textAlign: msg.role === "human" ? "right" : "left",
          margin: "10px 0"
        }}
      >
        <div
          style={{
            display: "inline-block",
            padding: "10px",
            borderRadius: "10px",
            backgroundColor: msg.role === "human" ? "#DCF8C6" : "#F1F0F0",
            maxWidth: "70%"
          }}
        >
          <b>{msg.role === "human" ? "You" : "AI"}:</b>
          <p>{msg.content}</p>
        </div>
      </div>
    ))}
    <div ref={chatEndRef}></div>
  </div>

  <div className="chat-input">
    <input
      type="text"
      value={input}
      onChange={(e) => setInput(e.target.value)}
      placeholder="Ask your question..."
    />

    <button onClick={postMsg} className="px-4 py-2 bg-blue-500 text-white rounded-full hover:bg-blue-600">Send</button>
  </div>
      <div ref={chatEndRef}></div>
</div>
  );
}
export default ChatWindow;