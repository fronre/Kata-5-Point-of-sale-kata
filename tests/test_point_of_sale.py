from src.point_of_sale import point_of_sale

def test_point_of_sale_input_empty_return_error():
    assert point_of_sale("") == "Error: barcode is empty"

def test_point_of_sale_barcode_12345_should_return_price():
    assert point_of_sale("12345") == "$7.25"
