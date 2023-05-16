from calculation import calc
from user_interface import get_data as gd
import logger

def control_data():
    logger.log_all('Записываем переменные. Вызываем функцию вычисления.')
    first_value, second_value, operator = gd()
    result = calc(first_value, second_value, operator)
    logger.log_all(f"Ответ = {str(result)}")
    return result