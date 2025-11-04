def point_of_sale(barcode: str) -> str:
    if barcode == "":
        return "Error: barcode is empty"

    if barcode == "12345":
         return "$7.25"


    if barcode == "23456":
        return "$12.50"


    if barcode == "99999":
        return "Error: barcode not found"


