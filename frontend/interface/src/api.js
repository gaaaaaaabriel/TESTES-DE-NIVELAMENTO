import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000", // Endereço da sua API
});

export const buscarOperadoras = async (query) => {
  try {
    const response = await api.get(`/buscar_operadoras?query=${query}`);
    return response.data; 
  } catch (error) {
    console.error("Erro ao buscar operadoras", error);
    return []; //retorna vazio, para não estourar erro na cara do usuario
  }
};
