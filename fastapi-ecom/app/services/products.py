import json

from pathlib import Path

from typing import List,Dict
BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR.parent / "data" / "products.json"

def load_products() ->List[Dict]:
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE,'r',encoding='utf-8') as file:
        return json.load(file)
    

def get_all_products() ->List[Dict]:
    return load_products()

def save_product(products:List[Dict])->None:
    with open(DATA_FILE,"w",encoding="utf-8") as f:
        json.dump(products,f,indent=2,ensure_ascii=False)
def add_product(product:Dict)->Dict:
    products=get_all_products()
    products.append(product)
    save_product(products)
    return product

# def remove_product(id:int)->str:
#     products=get_all_products()
#     for idx,product in enumerate(products):
#         if product["id"]==int(id):
#             deleted=products.pop(idx)
#             save_product(products)
#             return {"message":"product deleted success","data":deleted}

def remove_product(id:int)->Dict:
    products=get_all_products()

    for idx,product in enumerate(products):
        if product["id"] == int(id):
            deleted = products.pop(idx)
            save_product(products)

            return {
                "message":"product deleted success",
                "data":deleted
            }

    raise ValueError("product not found")
        
def update_product(id:int,update_data:Dict):
    products=get_all_products()
    for idx,product in enumerate(products):
        if int(product["id"]) != int(id):
            continue
        for key,value in update_data.items():
            if value is None:
                continue
            if isinstance(value,dict) and isinstance(product.get(key),dict):
                product[key].update(value)
            else:
                product[key]=value
        products[idx] =product
        save_product(products)
        return product
    raise ValueError("product not found")