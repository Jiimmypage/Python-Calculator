from src.calculators.calculator_2 import Calculator2
from src.drivers.numpy_handler import NumpyHandler

def calculator2_factory() -> Calculator2:
    return Calculator2(NumpyHandler())