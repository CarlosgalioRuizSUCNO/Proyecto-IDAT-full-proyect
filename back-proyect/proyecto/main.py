from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from fastapi.middleware.cors import CORSMiddleware
 
app = FastAPI()

origins = [
    "http://localhost:5173/",
    "http://127.0.0.1:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],  # Permite cualquier origen
    allow_credentials = True,  # Permite enviar cookies/autenticacion
    allow_methods = ["*"],  # Permite todos los metodos: get, post, put, delete
    allow_headers = ["*"]   # Permite todas las cabeceras
)

class Product(BaseModel):
  id:int
  name:str
  price:float
  image: str
  description:Optional[str] = None
 
products = [
  Product(id=1, name = "TV", price = 1999, image = "https://images.samsung.com/is/image/samsung/assets/pe/tvs/03-2025/2025-tvs-pcd-f03-line-up-01-mo.jpg?$720_N_JPG$", description = "High-end gaminf TV"),
  Product(id=2, name = "smartphone", price = 799, image = "https://rymportatiles.com.pe/cdn/shop/files/Samsung-Galaxy-S24-Ultra-grey.png?v=1706808200&width=1214", description = "latest model smartphone"),
  Product(id=3, name = "tablet", price = 249, image = "https://i5.walmartimages.com/asr/76306201-5160-4a1c-ba20-364a2470592a.69d9219fbea842b22a511fae0ee4d6c7.jpeg?odnHeight=612&odnWidth=612&odnBg=FFFFFF", description = "screen with good resolution"),
  Product(id=4, name = "laptop", price = 799, image = "https://elcomercio.pe/resizer/v2/5G2JX6RN6VEXJBHT6LETGSUA4M.jpg?auth=af2d6488ebff91f93a51210eefff4764ace76542f6eee89cb1c7d7786b9702f2&width=1200&height=800&quality=75&smart=true", description = "good laptop with great resolution"),
]
 
 
@app.get("/products", response_model = List[Product])
# response_model = List[Product] : indica que la respuesta sera una lista de objetos de tipo Porduct.
async def get_products():
    return products
    # Devuelve la lista de productos
 
@app.get("/products/{product_id}", response_model = Product)
async def get_product(product_id:int):
    product = next((p for p in products if p.id == product_id), None)
    if product is None:
        raise HTTPException(status_code = 404, detail = "Product not found")
    return product    
 
@app.post("/products", response_model=Product)
async def create_product(product:Product):
    if any(p.id == product.id for p in products):
    # Verifica si el id del producto que se intenta crear ya existe en la lista products.
      raise HTTPException(status_code=400, detail="Product ID already exists")
    products.append(product)
    # si el ID no existe, agrega el nuevo producto a la lista products
    return product  
 
@app.put("/products/{product_id}", response_model = Product)
async def update_product(product_id: int, product: Product):
    index = next((i for i, p in enumerate(products) if p.id == product_id), None)
    # Busca el indice del productoo en la lista products cuyo id coincida con product_id.
    if index is None:
        raise HTTPException(status_code=400, detail="Product not found")
    products[index] = product  
    # Si se encuentra el producto, lo actializa en la lista con los nuevos datos.
    return product

@app.delete("/products/{product_id}", response_model = Product)
async def delete_product(product_id: int):
    index = next((i for i, p in enumerate(products) if p.id == product_id), None)
    # Busca el indice del productoo en la lista products cuyo id coincida con product_id.
    if index is None:
        raise HTTPException(status_code=400, detail="Product not found")
    delete_product = products.pop(index)
    # Si se encuentra el producto lo elimina de la lista utilizando pop() que tambien devuelve el producto eliminado
    return delete_product