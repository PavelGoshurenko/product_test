Siple Rest application for working with a database of products.

## Options

### Get list of all products:
GET /products/
Content-Type: application/json

### Get list of modified products:
GET /products/?modified=true
Content-Type: application/json

### Get list of non-modified products:
GET /products/?modified=false
Content-Type: application/json

### Get detailed information on a particular product.
GET /products/<product UUID>
Content-Type: application/json

### Product creation:
POST /products/create
Content-Type: application/json
  ```
{
    'name': 'Product name',
    'description': 'Product description',
    'logo': 'path_to_logo/logo.jpg'
}
  ```

### To update product:
  PUT  /products/update/<product UUID>
  Content-Type: application/json
    ```
{
    'name': 'Product name',
    'description': 'Product description',
    'logo': 'path_to_logo/logo.jpg'
}
  ```

### To delete product:
  GET /products/delete/<product UUID>
  Content-Type: application/json