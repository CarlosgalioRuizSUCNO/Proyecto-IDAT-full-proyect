import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useTiendaStore = defineStore('tienda', () => {

    const products = ref([]);

    const API_URL = "http://127.0.0.1:8000/products";

    const newProduct = ref({ name: "", price: 0, image: "", description: "" });

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
        if (!newProduct.value.name ||  newProduct.value.price <= 0 || !newProduct.value.image || !newProduct.value.description) return;
        
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
            newProduct.value.image = "";
            newProduct.value.description = "";
        } catch (error) {
            console.error("Error al agregar producto:", error);
        }
    };

    return {
        products, API_URL, newProduct, fetchProducts, addProduct
    }

})
