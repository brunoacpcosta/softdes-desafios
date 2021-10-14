import sys
sys.path.append("../src")
from softdes import lambda_handler
import pytest

mock_event = {"ndes": "1", "code": "", "args": [[1], [2], [3]],
"resp": [0, 0, 0], "diag": ["a", "b", "c"] }

func_error = "Nome da função inválido"

def test_correct_post():
    with open("./desafio.py", 'r', encoding="UTF-8") as file:
        answer = file.read()
    mock_event["code"] = answer
    assert len(lambda_handler(mock_event)) == 0

def test_incorrect_function():
    with open("./desafio2.py", 'r', encoding="UTF-8") as file:
        answer = file.read()
    mock_event["code"] = answer
    error = lambda_handler(mock_event)
    assert error[0:len(func_error)] == func_error

def test_incorrect_post():
    with open("./desafio3.py", 'r', encoding="UTF-8") as file:
        answer = file.read()
    mock_event["code"] = answer
    error = lambda_handler(mock_event)
    assert len(error) != 0 and error[0:len(func_error)] != func_error       