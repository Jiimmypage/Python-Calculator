import pytest
from typing import Dict
from src.calculators.calculator_1 import Calculator1

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self._json = body

    def get_json(self) -> Dict:
        return self._json

def test_calculate():
    mock_request = MockRequest(body={"number": 1})
    calculator_1 = Calculator1()

    response = calculator_1.calculate(mock_request)
    print("\n", response)

    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]

    assert response["data"]["result"] == 14.25
    assert response["data"]["Calculator"] == 1

def test_calculate_with_body_error():
    mock_request = MockRequest(body={"something": 1})
    calculator_1 = Calculator1()

    with pytest.raises(ValueError) as excinfo:  
        calculator_1.calculate(mock_request)

    assert str(excinfo.value) == "O campo 'number' é obrigatório."  