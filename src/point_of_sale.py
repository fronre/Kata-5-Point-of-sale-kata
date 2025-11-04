prices = {
    "12345": 7.25,
    "23456": 12.50,
}

total_sale = 0

def point_of_sale(barcode: str) -> str:
    global total_sale
    barcode = barcode.strip()

    if len(barcode) == 0:
        return "Error: empty barcode"

    if barcode == "total":
        return f"${total_sale:.2f}"

    if barcode in prices:
        total_sale += prices[barcode]
        return f"${prices[barcode]:.2f}"

    return "Error: barcode not found"
