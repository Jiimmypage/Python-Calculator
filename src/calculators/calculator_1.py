from typing import List, Dict, Any
from flask.wrappers import Request

class Calculator1:
    def calculate(self, request: Request) -> Dict[str, Any]:
        body = request.get_json()
        if body is None:
            raise ValueError("JSON inválido ou não enviado!")
        
        numbers = self._validate_body(body)
        results = []
        
        for number in numbers:
            split_number = number / 3
            first_result = self._first_process(split_number)  
            second_result = self._second_process(split_number)
            total_result = first_result + second_result + split_number
            results.append(round(total_result, 2))
        
        return self._format_response(results)

    def _validate_body(self, body: Dict[str, Any]) -> List[float]:
        if "numbers" not in body:
            raise ValueError("O campo 'numbers' é obrigatório.")
            
        if not isinstance(body["numbers"], list):
            raise ValueError("O campo 'numbers' deve ser uma lista.")
        
        try:
            return [float(num) for num in body["numbers"]]
        except (ValueError, TypeError):
            raise ValueError("Todos os valores em 'numbers' devem ser números válidos.")

    def _first_process(self, value: float) -> float:
        return ((value / 4) + 7) ** 2 * 0.257
    
    def _second_process(self, value: float) -> float:
        return ((value ** 2.121) / 5) + 1

    def _format_response(self, results: List[float]) -> Dict[str, Any]:
        return {
            "data": {
                "Calculator": 1,
                "results": results,
                "average": round(sum(results)/len(results), 2) if results else 0
            }
        }