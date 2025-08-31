<script setup>

import { ref } from "vue";
import { RouterLink, RouterView } from "vue-router";

const products = ref([]);
const newProduct = ref({ name: "", price: 0 });
 
const editing = ref(false);
const editData = ref({});
 
const API_URL = "http://127.0.0.1:8000/products";
 
const fetchProducts = async () => {
  try {
    const res = await fetch(API_URL);
    products.value = await res.json();
 
    // console.log(res);
  } catch (error) {
    console.error("Error al obtener productos:", error);
  }
};
fetchProducts();
 
const addProduct = async () => {
  if (!newProduct.value.name || newProduct.value.price <= 0) return;
 
  try {
    const res = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ ...newProduct.value, id: Date.now() }),
    });
 
    const created = await res.json();
    products.value.push(created);
 
    newProduct.value.name = "";
    newProduct.value.price = 0;
  } catch (error) {
    console.error("Error al agregar producto:", error);
  }
};
 
const deleteProduct = async (id) => {
  try {
    await fetch(`${API_URL}/${id}`, { method: "DELETE" });
    products.value = products.value.filter((p) => p.id !== id);
  } catch (error) {
    console.error("Error al eliminar producto:", error);
  }
};
 
const editProduct = (product) => {
  editing.value = true;
  // console.log(product);
  editData.value = { ...product };
  // console.log(editData.value);
};
 
const cancelEdit = () => {
  editing.value = false;
  editData.value = {};
};
 
const updateProduct = async () => {
  try {
    const res = await fetch(`${API_URL}/${editData.value.id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(editData.value),
    });
    const updated = await res.json();
    const index = products.value.findIndex((p) => p.id === updated.id);
    // console.log(index);
    products.value[index] = updated;
    cancelEdit();
  } catch (error) {
    console.error("Error al actualizar producto:", error);
  }
};
</script>
 
<template>
  <nav class=" mt-5 navbar navbar-expand-lg navbar-dark bg-dark">
    <div class="container-fluid">
      <a class="navbar-brand" href="./">CG-Web</a>
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