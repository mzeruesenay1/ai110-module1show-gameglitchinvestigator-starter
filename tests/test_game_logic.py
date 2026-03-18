from logic_utils import check_guess
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from app import check_guess as check_guess_full

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_hint_message_too_high():
    # When guess is above the secret, the hint should tell the player to go LOWER
    outcome, message = check_guess_full(70, 50)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'LOWER' in hint but got: '{message}'"

def test_hint_message_too_low():
    # When guess is below the secret, the hint should tell the player to go HIGHER
    outcome, message = check_guess_full(30, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'HIGHER' in hint but got: '{message}'"
