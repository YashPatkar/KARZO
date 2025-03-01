import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
  withCredentials: true,  // 🔥 Ensures session cookies are sent
});

export default api;