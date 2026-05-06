import pytest
# Simulation simple de logique de parsing pour le test
def parse_logic(text):
    if "avance" in text: return True
    if "stop" in text: return True
    return False

def test_commands():
    assert parse_logic("avance 1.0") == True
    assert parse_logic("stop") == True
    assert parse_logic("inconnu") == False
