import logging
from datetime import datetime

# Configuração básica
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

class Calculator:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
    
    def divide(self, a, b):
        self.logger.info(f"Dividindo {a} por {b}")
        
        if b == 0:
            self.logger.error("Tentativa de divisão por zero")
            raise ValueError("Divisão por zero")
        
        result = a / b
        self.logger.info(f"Resultado: {result}")
        return result
    
    def calculate_average(self, numbers):
        self.logger.debug(f"Calculando média de {len(numbers)} números")
        
        if not numbers:
            self.logger.warning("Lista vazia fornecida para cálculo de média")
            return 0
        
        avg = sum(numbers) / len(numbers)
        self.logger.info(f"Média calculada: {avg}")
        return avg

# Uso
calc = Calculator()
try:
    result = calc.divide(10, 2)
    avg = calc.calculate_average([1, 2, 3, 4, 5])
except ValueError as e:
    logger.error(f"Erro no cálculo: {e}")