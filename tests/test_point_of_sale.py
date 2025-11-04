import pytest
from src.point_of_sale import point_of_sale

@pytest.mark.parametrize("barcode, expected", [
    ("12345", "$7.25"),
    ("23456", "$12.50"),
    ("99999", "Error: barcode not found"),
    ("", "Error: empty barcode"),
])
def test_point_of_sale_various_cases(barcode, expected):
    assert point_of_sale(barcode) == expected
