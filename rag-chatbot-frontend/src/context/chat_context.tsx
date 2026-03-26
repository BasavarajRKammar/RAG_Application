import React, { useEffect, useRef, useState } from "react";
import Headers from "../components/header";
import FileUploads from "../components/fileupload";
import ChatWindow from "../components/chatwindow";

const Chatcontext = ()=>{
     const [loading, setLoading] = useState(false);
    const [messages, setMessages] = useState([]);

    return (
    <>
      <Headers />
       {loading && (
        <div>
        <div className="loader-container">
          <div className="loader"></div>
        </div>
         <span>Processing..</span>
         </div>
      )}
      <FileUploads setLoading={setLoading}/>
      <ChatWindow messages={messages} setMessages={setMessages} />
    </>
  );
}

export default Chatcontext