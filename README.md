# Forsit_BackEndTask

Database schema:
Here is the documentation of the database schema, explaining the purpose of each table and its relationships:

1. Product Table:
   Table Name: products
   Purpose: 
	This table is used to store information about products that are available in the inventory for sale. Each record represents a unique product with details such as its name, price, quantity in stock, description, and category.
   Columns:
•	id (Primary Key): An auto-generated unique identifier for each product.
•	name: The name of the product, which must be unique.
•	price: The price of the product.
•	quantity: The quantity of the product available in stock.
•	description: A brief description of the product.
•	category: The category to which the product belongs.

2. Sales Table:
   Table Name: sales
   Purpose: 
	This table is used to record sales transactions. It tracks when a product was sold, the quantity sold, and the revenue generated from the sale.
   Columns:
•	id (Primary Key): An auto-generated unique identifier for each sale record.
•	product_id (Foreign Key): References the `id` of the product that was sold, establishing a relationship with the Product table.
•	sale_date: The date and time when the sale occurred, recorded in UTC.
•	quantity_sold: The quantity of the product sold in this transaction.
•	revenue: The total revenue generated from the sale of the product.

3. Inventory Table:
Table Name:inventory
Purpose:
	 This table is used to maintain a record of the current inventory levels for each product. It helps track the quantity of each product available in stock.
Columns:
•	id (Primary Key): An auto-generated unique identifier for each inventory record.
•	product_id (Foreign Key): References the `id` of the product, linking it to the Product table.
•	quantity: The current quantity of the product in stock.

4. Supplier Table:
Table Name: suppliers
Purpose:
	 This table is used to store information about suppliers who provide products to the inventory. It includes details about the supplier's name, contact information, address, email, and phone number.
Columns:
•	id(Primary Key): An auto-generated unique identifier for each supplier.
•	name: The name of the supplier, which must be unique.
•	contact: Contact information for the supplier.
•	Address: The supplier's address.
•	email: The email address of the supplier.
•	phone: The phone number of the supplier.

5. Customer Table:
Table Name: customers
Purpose:
	 This table is used to store information about customers who make purchases. It includes details about the customer's name, email, phone number, and address.
Columns:
•	id (Primary Key): An auto-generated unique identifier for each customer.
•	name: The name of the customer.
•	email: The email address of the customer, which must be unique.
•	phone: The phone number of the customer.
•	address: The address of the customer.

Relationships:
•	The `Sales` table has a foreign key relationship with the `Product` table to associate each sale with a specific product.
•	The `Inventory` table also has a foreign key relationship with the `Product` table to link inventory records to their respective products.
•	The `Supplier` table contains supplier information that is relevant to the products in the `Product` table, but there is no direct foreign key relationship between them.
•	The `Customer` table is independent and holds customer information that can be associated with sales transactions.

This database schema is designed to support inventory management, sales tracking, and customer and supplier management for an e-commerce application.
