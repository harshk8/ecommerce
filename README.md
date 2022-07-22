# ecommerce
Its a test app for creating product having multiple category and category itself having their sub-category in same table.

We have created CRUD Operation for Category and Product, all details mentioned below:


### CRUD Operation for Category:
1. Create Category:
POST: /api/categorys/
Body: {
        "name": "Sweet Food",
        "parent": 2
    }
Response: {
        "id": 3,
        "name": "Sweet Food",
        "parent": 2
    }
status_code: 201_CREATED


2. Get All Category:
GET: /api/categorys
Response: [
    {
        "id": 1,
        "name": "Food",
        "parent": null
    },
    {
        "id": 2,
        "name": "Fruits",
        "parent": 1
    },
    ...
    ]
status_code: 200_OK


3. Get Category by Id:
POST: /api/categorys/1/
Response: {
        "id": 1,
        "name": "Food",
        "parent": null
    }
status_code: 200_OK


4. Update Category:
PUT: /api/categorys/1/
Body: {
    "name": "Foods",
    "parent": null
}
Response: {
        "id": 1,
        "name": "Foods",
        "parent": null
    }
status_code: 200_OK

5. Delete Category:
DELETE: /api/categorys/1/
Response: {}
status_code: 204 No Content


### CRUD Operation for Product:
1. Create Product:
POST: /api/products/
Body: {
    "name": "TV 65 Inches",
    "price": 50000,
    "category": 9
}
Response: {
    "id":99,
    "name": "TV 65 Inches",
    "price": 50000,
    "category": [9,10]
}
status_code: 201_CREATED


2. Get All Product:
GET: /api/products
Response: [
    {
        "id": 99,
        "name": "TV 32 Inches",
        "price": 10000,
        "category": [9]
    },
    {
        "id": 100,
        "name": "TV 65 Inches",
        "price": 50000,
        "category": [9]
    },...
    ]
status_code: 200_OK


3. Get Product by Id:
POST: /api/product/99/
Response: {
        "id": 99,
        "name": "TV 32 Inches",
        "price": 10000,
        "category": [9]
    }
status_code: 200_OK


4. Update Product:
PUT: /api/product/99/
Body:     {
    "name": "TV 32 Inches - Android TV",
    "price": 10000,
    "category": [9]
}
Response: {
        "id": 99,
        "name": "TV 32 Inches - Android TV",
        "price": 10000,
        "category": [9]
    }
status_code: 200_OK


5. Delete Product:
DELETE: /api/product/99/
Response: {}
status_code: 204_NO_CONTENT