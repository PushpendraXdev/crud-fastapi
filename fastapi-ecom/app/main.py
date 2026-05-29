from fastapi import FastAPI,HTTPException,Query
from services.products import update_product,remove_product,get_all_products,add_product
from schema.product_schema import Product,ProductUpdate
app=FastAPI()


# uvicorn main:app --reload

@app.get("/")

def root():
    return {"hello"}

@app.get("/products")

def list_products(

    name: str =Query(
     default=None,
     min_length=1,
     max_length=50,
     description="Search by prooduct name "),

    sort_by_price:bool=Query(
     default=False,
     description="Sort products by price"),
     
     offset:int=Query(default=1,
                 description="offset limit"
         
     ),

    order:str=Query(
     default="asc",
     description="sort by asc or desc when sort_by_price is true"),

     limit:int=Query(
     default=5,
     ge=1,
     le=50,
     description="number of product"),
):
    products=get_all_products()
    if name:
        needle=name.strip().lower()
        products=[p for p in products if needle in p.get("name","").lower().strip()]

        if not products:
            raise HTTPException(status_code=404,detail=f"not found for={name}")
        if sort_by_price:
            reverse=order=="desc"
            products=sorted(products,key=lambda p:p.get("price",0),reverse=reverse)
    total = len(products)
    products=products[offset:offset+limit]
    return {
        "total":total,
        "items":products
    }

@app.get("/products/{id}")

def get_product_byid(id:int):
    products=get_all_products()
    for product in products:
        if product["id"]==id:
            return product
    raise HTTPException(status_code=404,detail="product not found.")

@app.post("/products",status_code=201)

def create_products(product:Product):
    product_dict=product.model_dump(mode="json")
    product_dict["id"]=10
    try:
        add_product(product_dict)
    except:
        raise HTTPException(status_code=400)
    return product.model_dump(mode="json")

@app.delete("/products/{product_id}")

def delete_product(product_id:int):
    try:
        data=remove_product(product_id)
        return data
    except:
        raise HTTPException(status_code=400)


@app.patch("/products/{product_id}")

def update_product_route(product_id:int,payload:ProductUpdate):
    try:
        updated_product=update_product(product_id,payload.model_dump(mode="json",exclude_unset=True))
        return updated_product
    except Exception as e:
        raise HTTPException(status_code=404,detail=str(e))