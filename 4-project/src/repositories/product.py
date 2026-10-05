import json

from src.core import JSON_DATA_FILE_PATH


class ProductRepository:
    # 1. get all products
    def get_all(self) -> dict | None:

        if not JSON_DATA_FILE_PATH:
            raise FileNotFoundError("Invalid path or /data/data.json file not found")

        # read file
        with open(JSON_DATA_FILE_PATH, mode="r") as file:
            payload = json.load(file)

        if not payload:
            return None

        # DEBUG: inspect few values
        # print("--- DEBUG Inspect payload ---")
        # print(payload[1:5])
        # print("-"*25)

        return {"total_products": len(payload), "products": payload}

    # 2. get by id
    def get_by_id(self, id: int) -> dict | None:

        if not JSON_DATA_FILE_PATH:
            raise FileNotFoundError("Invalid path or /data/data.json file not found")

        # read file
        with open(JSON_DATA_FILE_PATH, mode="r") as file:
            payload = json.load(file)

        if not payload:
            return None

        return next((p for p in payload if p.get("id") == id), None)

    # 3. search product
    def search(self, q: str, skip: int = 0, limit: int = 10) -> dict | None:

        if not JSON_DATA_FILE_PATH:
            raise FileNotFoundError("Invalid path or /data/data.json file not found")

        # read file
        with open(JSON_DATA_FILE_PATH, mode="r") as file:
            payload = json.load(file)

        if not payload:
            return None

        # lowercase query
        q = q.lower()

        products = []

        for p in payload:
            if (
                q in str(p.get("id"))
                or q in str(p.get("price"))
                or q in p.get("name").lower()
                or q in p.get("description").lower()
                or q in p.get("category").lower()
            ):
                products.append(p)

        # handle if products found are with in default limit
        if len(products) >= 1 and len(products) <= 10:
            return {
                "total_products": len(payload),
                "found_products": len(products),
                "skip": 0,
                "limit": len(products),
                "products": products[0 : 0 + len(products)],
            }
        else:
            return {
                "total_products": len(payload),
                "found_products": len(products),
                "skip": skip,
                "limit": limit,
                "products": products[skip : skip + limit],
            }


# # Debugging
# product = ProductRepository()

# # Get all products
# print("--- DEBUG product repository ---")
# all_products: dict | None = product.get_all()
# if all_products:
#     # print some products
#     print(all_products["products"][1:2])
