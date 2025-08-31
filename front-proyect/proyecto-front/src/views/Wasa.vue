<script setup >

import { ref } from "vue";
 
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
  <div class="container">
    <h1>Crud Productos</h1>
 
    <!-- Formulario para agregar productos -->
    <div class="mb-3">
      <input
        v-model="newProduct.name"
        placeholder="Nombre"
        class="form-control mb-2"
      />
      <input
        v-model.number="newProduct.price"
        type="number"
        placeholder="Precio"
        class="form-control mb-2"
      />
      <button @click="addProduct" class="btn btn-primary">
        Agregar Producto
      </button>
    </div>
 
    <!-- Lista de productos -->
    <ul class="list-group mt-4">
      <li
        class="list-group-item d-flex justify-content-between align-items-center"
        v-for="product in products"
        :key="product.id"
      >
        <span>{{ product.name }} - {{ product.price }} $</span>
        <div>
          <button
            @click="editProduct(product)"
            class="btn btn-sm btn-warning me-2"
          >
            Editar
          </button>
          <button
            @click="deleteProduct(product.id)"
            class="btn btn-sm btn-danger"
          >
            Eliminar
          </button>
        </div>
      </li>
    </ul>
 
    <!--formulario de edicion -->
    <div v-if="editing" class="mt-4">
      <h3>Editar Producto</h3>
      <input v-model="editData.name" class="form-control mb-2" />
      <input
        v-model.number="editData.price"
        type="number"
        class="form-control mb-2"
      />
      <button @click="updateProduct" class="btn btn-success me-2">
        Actualizar
      </button>
      <button @click="cancelEdit" class="btn btn-secondary">Cancelar</button>
    </div>
  </div>
</template>