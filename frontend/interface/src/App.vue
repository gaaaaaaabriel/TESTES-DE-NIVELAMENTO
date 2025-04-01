<script setup>
import { ref, watch } from "vue";
import { buscarOperadoras } from "./api";

const query = ref("");
const operadoras = ref([]);

const buscar = async () => {
  if (query.value.trim()) {
    operadoras.value = await buscarOperadoras(query.value);
    console.log(operadoras.value); // visualizar no console F12
  }
};

watch(query, async () => {
  await buscar();
});

const showInfo = ref(false); 
</script>

<template>
  <div>
    <h1>Buscar Operadoras</h1>
    <div class="barra-busca">
      <input v-model="query" placeholder="Digite o nome" />
    </div>

    <div v-if="operadoras.length" class="containre-resultado">
      <ul>
        <!-- nesse lugar, é criado um for, que percorre a lista do json que vem no corpo da requisição -->
        <li v-for="(operadora, index) in operadoras" :key="index" class="operadora-item">
          <div><strong>Razão Social:</strong> {{ operadora.Razao_Social }}</div>
          <div><strong>Nome Fantasia:</strong> {{ operadora.Nome_Fantasia }}</div>
          <div><strong>Telefone:</strong> {{ operadora.Telefone }}</div>
          <div><strong>Cidade:</strong> {{ operadora.Cidade }} - {{ operadora.UF }}</div>
          <div><strong>Email:</strong> {{ operadora.Endereco_eletronico }}</div>
          <hr />
        </li>
      </ul>
    </div>

    <p v-else class="sem-resultados">Nenhuma operadora encontrada.</p>

    <!-- Ícone de informações no canto superior direito -->
    <div class="informacoes-icon" @mouseover="showInfo = true" @mouseleave="showInfo = false">
      ℹ️
    </div>

    <div v-if="showInfo" class="informacao">
      Essa interface foi feita com uma framework chamada VUE, ela tem como foco principal, fazer uma busca, 
      mas não a um banco de dados, ao arquivo .csv que está dentro dos diretórios. 
      A parte do backend foi feita com Python, utilizando pandas, que serve para tratar dados.
    </div>
  </div>
</template>

<style scoped>
body {
  background-color: #dcdcdc; 
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}


h1 {
  text-align: center;
  font-size: 30px;
  font-weight: 600;
  color: #0059b3;
  margin-bottom: 20px;
}


.barra-busca {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-bottom: 30px;
}

input {
  padding: 12px 15px;
  font-size: 16px;
  width: 300px;
  border-radius: 8px;
  border: 1px solid #ccc;
  transition: border 0.3s;
}

input:focus {
  border-color: #3498db;
  outline: none;
}

.containre-resultado {
  background-color: #ffffff;
  padding: 20px;
  margin-top: 30px;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
  background-color: #f8f8f8;
}

.operadora-item {
  background-color: #f4f6f7;
  padding: 15px;
  margin-bottom: 15px;
  border-radius: 6px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s ease;
}

.operadora-item:hover {
  background-color: #ecf0f1;
}

.operadora-item div {
  margin-bottom: 8px;
  color: #2c3e50;
}

strong {
  font-weight: 600;
  color: #2980b9;
}

hr {
  margin: 10px 0;
  border: 0;
  border-top: 1px solid #ddd;
}

.sem-resultados {
  text-align: center;
  font-size: 18px;
  color: #e74c3c;
  font-weight: bold;
}

.informacoes-icon {
  position: absolute;
  top: 20px;
  right: 20px;
  font-size: 30px;
  cursor: pointer;
  z-index: 9999;
}

.informacao {
  position: fixed;
  top: 100px; 
  left: 50%;
  transform: translateX(-50%);
  background-color: rgba(0, 0, 0, 0.404);
  color: #fff;
  padding: 20px;
  border-radius: 6px;
  width: 80%;
  font-size: 14px;
  text-align: left;
  white-space: normal;
  z-index: 10000;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

@media (max-width: 768px) {
  .barra-busca {
    flex-direction: column;
    align-items: center;
  }

  input {
    width: 100%;
    margin-bottom: 15px;
  }

  .containre-resultado {
    padding: 15px;
  }

  .operadora-item {
    padding: 12px;
  }

  .informacoes-icon {
    top: 10px;
    right: 10px;
  }
}
</style>
