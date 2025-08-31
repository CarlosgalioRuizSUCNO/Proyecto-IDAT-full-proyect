<script setup ></script>
<template>
    <div class="container py-5">
    <div class="row">
      <!-- Formulario -->
      <div class="col-lg-7">
        <div class="card shadow-sm p-4">
          <h3 class="mb-4">Envíanos un mensaje</h3>
          <form>
            <div class="mb-3">
              <label for="nombre" class="form-label">Nombre</label>
              <input type="text" id="nombre" class="form-control" placeholder="Tu nombre">
            </div>
            <div class="mb-3">
              <label for="email" class="form-label">Correo</label>
              <input type="email" id="email" class="form-control" placeholder="tu@email.com">
            </div>
            <div class="mb-3">
              <label for="mensaje" class="form-label">Mensaje</label>
              <textarea id="mensaje" class="form-control" rows="5" placeholder="Escribe tu mensaje"></textarea>
            </div>
            <button type="submit" class="btn btn-primary">Enviar</button>
          </form>
        </div>
      </div>

      <!-- Info de contacto -->
      <div class="col-lg-5 mt-4 mt-lg-0">
        <div class="card shadow-sm p-4 bg-dark text-light">
          <h4>Información de contacto</h4>
          <p class="mb-2"><i class="bi bi-geo-alt-fill"></i> Av. MAnco Inca 315</p>
          <p class="mb-2"><i class="bi bi-telephone-fill"></i> +51 939 017 545</p>
          <p class="mb-2"><i class="bi bi-envelope-fill"></i> cv63218346galio@gmail.com</p>
          <hr class="border-light">
          <h5>Síguenos</h5>
          <a href="#" class="text-light me-3"><i class="bi bi-facebook"></i> Facebook</a>
          <a href="#" class="text-light me-3"><i class="bi bi-twitter"></i> Twitter</a>
          <a href="#" class="text-light"><i class="bi bi-instagram"></i> Instagram</a>
        </div>
      </div>
    </div>
  </div>
</template>