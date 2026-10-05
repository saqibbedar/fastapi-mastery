# Guide

Use [Mockaroo](https://www.mockaroo.com/) and generate `commerce` type data in `json` or `csv` format. You can get help from llm for this, how to generate fake+free data using Mockaroo. 

# Fields

Select following fields to get the application to work properly, as these this product is defined and whole application is built on top of it. So, use exact fields in Mockaroo Api for data generation.

```py
class Product:
    id: int
    name: str
    description: str
    price: float
    category: str
    image_url: str
```