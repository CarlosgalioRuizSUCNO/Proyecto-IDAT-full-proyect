<script>

import axios from "axios";

export default {
  name: "Productos",
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
    <section id="productos" class="container py-5">
        <h2 class="text-center mb-4">Productos Destacados</h2>
        <div class="row g-4">
            <!-- Producto 1 -->
            <div v-for="p in productos" :key="p.id" class="col-md-4">
                <div class="card shadow-sm h-100">
                    <img style="height: 315px;" :src= "p.image" class="card-img-top" :alt="p.name">
                    <div class="card-body">
                        <h5 class="card-title">{{ p.name }} </h5>
                        <p style="margin-bottom: 0;" class="card-text text-muted">$/ {{ p.price}}</p>
                        <p class="card-text text-muted">Descripción: {{ p.description}}</p>
                        <button @click="addProduct" class="btn btn-primary">
                        Agregar Producto
                        </button>
                    </div>
                </div>
            </div>
        </div>
    </section>
</template>