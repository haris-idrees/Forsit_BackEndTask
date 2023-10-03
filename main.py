from fastapi import FastAPI, HTTPException, Depends,status
from pydantic import BaseModel
from typing import Annotated
import Models
from Database import engine,SessionLocal
from sqlalchemy.orm import Session
from datetime import datetime

#
app = FastAPI()
Models.Base.metadata.create_all(bind=engine)


class ProductBase(BaseModel):
    name: str
    price: float
    quantity: int
    description: str
    category: str


class SupplierBase(BaseModel):
    name: str
    contact: str
    Address: str


class CustomerBase(BaseModel):
    name: str
    email: str
    phone: str
    address: str


class SalesBase(BaseModel):
    product_id: int
    sale_date: str
    quantity_sold: int
    revenue: float


class InventoryBase(BaseModel):
    product_id: int
    quantity: int


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


# --------------------------Customer End points--------------------------------------

@app.post("/cutomers/", status_code=status.HTTP_201_CREATED)
async def insert_customer(customer:CustomerBase, db:db_dependency):
    db_cust = Models.Customer(**customer.dict())
    db.add(db_cust)
    db.commit()


@app.get("/customer/{cust_id}", status_code=status.HTTP_200_OK)
async def read_customer(cust_id: int, db: db_dependency):
    customer = db.query(Models.Customer).filter(Models.Customer.id == cust_id).first()
    if customer is None:
        raise HTTPException(status_code=404, detail="User not found")
    return customer


@app.get("/customers/", status_code=status.HTTP_200_OK)
async def read_all_customers(db: db_dependency):
    customer = db.query(Models.Customer).all()
    if customer is None:
        raise HTTPException(status_code=404, detail="Customers not found")
    return customer

@app.delete("customers/{cust_id}", status_code=status.HTTP_200_OK)
async  def remove_customer(cust_id: int, db: db_dependency):
    db_customer = db.query(Models.Customer).filter(Models.Customer.id == cust_id).first()
    if db_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    db.delete(db_customer)


@app.put("/customers/{cust_id}", status_code=status.HTTP_200_OK)
async def update_customer(cust_id: int, updated_cust: CustomerBase, db: db_dependency):
    db_cust = db.query(Models.Customer).filter(Models.Customer.id == cust_id).first()
    if db_cust is None:
        raise HTTPException(status_code=404, detail="Customer not found")

    # Update the post attributes
    db_cust.name = updated_cust.name
    db_cust.email = updated_cust.email
    db_cust.phone = updated_cust.phone
    db_cust.address = updated_cust.address

    db.commit()
    db.refresh(db_cust)
    return db_cust

# __________________________Product End Points__________________________________________


@app.post("/products/", status_code=status.HTTP_201_CREATED)
async def insert_product(product:ProductBase, db: db_dependency):
    db_product = Models.Product(**product.dict())
    db.add(db_product)
    db.commit()


@app.get("/products/", status_code=status.HTTP_200_OK)
async def read_all_products(db: db_dependency):
    product = db.query(Models.Product).all()
    if product is None:
        raise HTTPException(status_code=404, detail="Products not found")
    return product


@app.get("/products/{prod_id}", status_code=status.HTTP_200_OK)
async def read_product(product_id: int, db: db_dependency):
    product = db.query(Models.Product).filter(Models.Product.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@app.delete("products/{prod_id}", status_code=status.HTTP_200_OK)
async  def remove_product(prod_id: int, db: db_dependency):
    db_product = db.query(Models.Product).filter(Models.Product.id == prod_id).first()
    if db_product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(db_product)


@app.put("/products/{prod_id}", status_code=status.HTTP_200_OK)
async def update_product(prod_id: int, updated_prod: ProductBase, db: db_dependency):
    db_prod = db.query(Models.Product).filter(Models.Product.id == prod_id).first()
    if db_prod is None:
        raise HTTPException(status_code=404, detail="Product not found")

    # Update the post attributes
    db_prod.name = updated_prod.name
    db_prod.price = updated_prod.price
    db_prod.quantity = updated_prod.quantity
    db_prod.description = updated_prod.description
    db_prod.category = updated_prod.category

    db.commit()
    db.refresh(db_prod)
    return db_prod


# __________________________Supplier End Points__________________________________________


@app.post("/suppliers/", status_code=status.HTTP_201_CREATED)
async def insert_supplier(supplier:SupplierBase, db: db_dependency):
    db_supplier = Models.Supplier(**supplier.dict())
    db.add(db_supplier)
    db.commit()


@app.get("/suppliers/", status_code=status.HTTP_200_OK)
async def read_all_suppliers(db: db_dependency):
    db_supplier = db.query(Models.Supplier).all()
    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Suppliers not found")
    return db_supplier


@app.get("/suppliers/{supp_id}", status_code=status.HTTP_200_OK)
async def read_supplier(supp_id: int, db: db_dependency):
    db_supplier = db.query(Models.Supplier).filter(Models.Supplier.id == supp_id).first()
    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return db_supplier


@app.delete("suppliers/{supp_id}", status_code=status.HTTP_200_OK)
async  def remove_supplier(supp_id: int, db: db_dependency):
    db_supplier = db.query(Models.Supplier).filter(Models.Supplier.id == supp_id).first()
    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    db.delete(db_supplier)


@app.put("/suppliers/{supp_id}", status_code=status.HTTP_200_OK)
async def update_supplier(supp_id: int, updated_supp: SupplierBase, db: db_dependency):
    db_supplier = db.query(Models.Supplier).filter(Models.Supplier.id == supp_id).first()
    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")

    # Update the supplier attributes
    db_supplier.name = updated_supp.name
    db_supplier.contact = updated_supp.contact
    db_supplier.Address = updated_supp.Address

    db.commit()
    db.refresh(db_supplier)
    return db_supplier


# _________________________Sale End Points___________________________

@app.post("/sales/", status_code=status.HTTP_201_CREATED)
async def create_sales_record(sales: SalesBase, db: db_dependency):
    # Create a new sales record in the database
    sale_date = datetime.utcnow()
    db_sale = Models.Sales(sale_date=sale_date, **sales.dict())
    db.add(db_sale)
    db.commit()
    db.refresh(db_sale)
    return db_sale


@app.get("/sales/", status_code=status.HTTP_200_OK)
async def read_all_sales(db: db_dependency):
    sales = db.query(Models.Sales).all()
    if not sales:
        raise HTTPException(status_code=404, detail="Sales data not found")
    return sales


@app.put("/inventory/update/", status_code=status.HTTP_200_OK)
async def update_inventory(inventory_update: InventoryBase, db: db_dependency):
    # Find the product in the inventory
    product_id = inventory_update.product_id
    db_inventory = db.query(Models.Inventory).filter(Models.Inventory.product_id == product_id).first()
    if db_inventory is None:
        raise HTTPException(status_code=404, detail="Product not found in inventory")

    # Update the inventory quantity
    db_inventory.quantity += inventory_update.quantity_change
    db.commit()
    db.refresh(db_inventory)
    return db_inventory


@app.get("/")
def read_something():
    return {"msg":"Hello world"}