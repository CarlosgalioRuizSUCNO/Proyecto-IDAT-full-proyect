<script setup>

import { ref } from "vue";
import { RouterLink, RouterView } from "vue-router";
import { useTiendaStore } from "./stores/tienda";
import { storeToRefs } from "pinia";


const useTienda = useTiendaStore();

const {products, newProduct} = storeToRefs(useTienda);

// const products = ref([]);
// const newProduct = ref({ name: "", price: 0 });
 
const editing = ref(false);
const editData = ref({});
 
const API_URL = "http://127.0.0.1:8000/products";
// const API_URL = "https://backend-proyect-ln71.onrender.com/products";
 
// const fetchProducts = async () => {
//   try {
//     const res = await fetch(API_URL);
//     products.value = await res.json();
 
//     // console.log(res);
//   } catch (error) {
//     console.error("Error al obtener productos:", error);
//   }
// };
// fetchProducts();
</script>
 
<template>
  <nav class=" mt-5 navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid"> 
      <RouterLink class="navbar-brand" to="/">CG-Web</RouterLink>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#menuNav" aria-controls="menuNav" aria-expanded="false" aria-label="Menú">
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="menuNav">
        <ul class="navbar-nav ms-auto">
          <li class="nav-item">
            <RouterLink class="nav-link active" to="/">Inicio</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/productos">Productos</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/creador">Creador</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink class="nav-link" to="/contacto">Contacto</RouterLink>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <RouterView />
</template>