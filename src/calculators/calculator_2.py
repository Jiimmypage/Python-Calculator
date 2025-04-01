import numpy as np
from typing import Dict, Any, List
from flask.wrappers import Request
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class Calculator2:
    def __init__(self, driver_handler: DriverHandlerInterface):
        self.__driver_handler = driver_handler

    def calculate(self, request: Request) -> Dict[str, Any]:

        body = request.get_json()
        self.__validate_request(body)
        
        numbers = self.__convert_to_float_list(body["numbers"])
        
        return self.__build_response(numbers)

    def __validate_request(self, body: Dict[str, Any]) -> None:
        if not body:
            raise ValueError("Request body não pode ser vazio")
        if "numbers" not in body:
            raise ValueError("Campo 'numbers' é obrigatório")
        if not isinstance(body["numbers"], list):
            raise ValueError("'numbers' deve ser uma lista")

    def __convert_to_float_list(self, numbers: List[Any]) -> List[float]:
        try:
            return [float(num) for num in numbers]
        except (ValueError, TypeError) as e:
            raise ValueError(f"Valores inválidos em 'numbers': {str(e)}")

    def __build_response(self, numbers: List[float]) -> Dict[str, Any]:
        return {
            "data": {
                "Calculator": 2,
                "standard_deviation": round(self.__driver_handler.standard_deviation(numbers), 4),
                "variance": round(self.__driver_handler.variance(numbers), 4),
                "mean": round(np.mean(numbers), 4),
                "min": round(float(np.min(numbers)), 4),
                "max": round(float(np.max(numbers)), 4)
            }
        }