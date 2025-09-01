<script>

import { ref } from "vue";
import { RouterLink, RouterView } from "vue-router";

import axios from "axios";

export default {
  name: "Inicio",
  data() {
    return {
      productos: []
    };
  },
  async mounted() {
    try {
      // Obtén todos los productos desde tu API
      const response = await axios.get("http://localhost:8000/products");
      // const response = await axios.get("https://backend-proyect-ln71.onrender.com/products")
      this.productos = response.data;
    } catch (error) {
      console.error("Error al obtener productos:", error);
    }
  }
};

</script>

<template>
  <header class="bg-dark text-light text-center py-5">
    <div class="container">
      <h1 class="display-4 fw-bold">Bienvenido a CG_Web</h1>
      <p class="lead">Encuentra los mejores productos al mejor precio</p>
      <RouterLink class="btn btn-primary btn-lg mt-3" to="/productos">Comprar ahora</RouterLink>
    </div>
  </header>

  <!-- PRODUCTOS DESTACADOS -->
  <section id="productos" class="container py-5">
    <h2 class="text-center mb-4">Productos Destacados</h2>
    <div class="row g-4">
      <!-- Producto 1 -->
      <div v-for="p in productos.slice(0,3)" :key="p.id" class="col-md-4">
        <div class="card shadow-sm h-100">
          <img style="height: 315px;" :src= "p.image" class="card-img-top" :alt="p.name">
          <!-- <img style="height: 315px;" :src= "p.imagen" class="card-img-top" :alt="p.nombre"> -->
          <div class="card-body">
            <h5 class="card-title">{{ p.name }} </h5>
            <p class="card-text text-muted">$/ {{ p.price}}</p>
            <button @click="addProduct" class="btn btn-primary">
              Agregar Producto
            </button>
          </div>
        </div>
      </div>
    </div>
    <RouterLink class="d-flex justify-content-center btn btn-primary btn-lg mt-3" to="/productos">Ver mas</RouterLink>
  </section>

  <RouterView />
</template>
