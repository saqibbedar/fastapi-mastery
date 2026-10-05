import json

from src.core import DATA_DIR


# json based
class ProductRepository:
    # 1. get all products, read data from data/data.json file and return json data
    def get_all(self) -> list | None:

        payload = None

        # if valid path read the json data from /root/data/data.json
        if DATA_DIR:
            # read json data
            with open(DATA_DIR, mode="r") as file:
                payload = json.load(file)
            return payload
        else:
            return None

    # 2. get a product by an id
    def get_by_id(self, id: int) -> dict | None:

        payload = None

        if DATA_DIR:
            # read json data
            with open(DATA_DIR, mode="r") as file:
                payload = json.load(file)

            print(f"id type: {type(id)}")

            # find product by id
            for item in payload:
                if item["id"] == id:
                    return item
        else:
            return None

    # 3. search product
    def get_by_query(self, q: str) -> list | None:

        # lowercase query
        q = q.lower()

        payload = None

        if DATA_DIR:
            # read json data
            with open(DATA_DIR, mode="r") as file:
                payload = json.load(file)

            # accumulate founded products
            products = []

            # search a product
            for item in payload:
                # convert numbers to string
                id = str(item["id"])
                price = str(item["price"])

                # filter products
                if (
                    q in id
                    or q in price
                    or q in item["name"].lower()
                    or q in item["description"].lower()
                    or q in item["category"].lower()
                ):
                    products.append(item)

            return products

        else:
            return None

    # 4. product with pagination
    def get_by_pagination(self, q: str, skip: int = 0, limit: int = 10) -> dict | None:

        # lowercase query
        q = q.lower()

        payload = None

        if DATA_DIR:
            # read json data
            with open(DATA_DIR, mode="r") as file:
                payload = json.load(file)

            # accumulate products
            products = []

            for item in payload:
                # convert numbers to string
                id = str(item["id"])
                price = str(item["price"])

                # filter products
                if (
                    q in id
                    or q in price
                    or q in item["name"].lower()
                    or q in item["description"].lower()
                    or q in item["category"].lower()
                ):
                    products.append(item)

            return {
                "total_matches": len(products),
                "skip": skip,
                "limit": limit,
                "results": products[skip : skip + limit] if len(products) > 10 else products,
            }

        else:
            return None
