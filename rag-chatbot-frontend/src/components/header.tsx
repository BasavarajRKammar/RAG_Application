import React from "react";

const Headers = () => {
const headerStyle = {
    backgroundColor: "#1F2937", // Dark gray background
    color: "#F9FAFB",           // Light text color
    padding: "15px 30px",
    textAlign: "center",
    fontSize: "1.8rem",
    fontWeight: "700",
    fontFamily: "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
    boxShadow: "0 4px 6px rgba(0,0,0,0.1)",
    borderRadius: "0 0 10px 10px",
  };

  return <h2 style={headerStyle}>Gen AI RAG Chatbot</h2>;
}

export default Headers