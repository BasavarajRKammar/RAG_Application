import axios from "axios";

// Create axios instance
const API = axios.create({
  baseURL: "http://localhost:8000", // FastAPI backend
});

export const upload_file = async(file: any) =>{
    const response = API.post('/documents',file)
    return response
}

export const chat = async(msg: any) =>{
    const resonse = API.post('/chat', msg)
    return resonse
}

export const get_Response = async() =>{
    const resonse = API.get('/chat')
    return resonse
}