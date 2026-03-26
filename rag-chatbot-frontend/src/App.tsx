import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Chatcontext from "./context/chat_context";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Chatcontext />} />
      </Routes>
    </Router>
  );
}

export default App;