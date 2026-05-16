import axios from "axios";
import env from "env";

const API = axios.create({
  baseURL: import.meta.env.VITE_API_URL,
});

export default API;