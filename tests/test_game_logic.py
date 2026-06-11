import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import check_guess, get_range_for_difficulty


# Bug 1: Normal and Hard difficulty ranges were swapped.
# Normal should go 1–50 and Hard should go 1–100, but the original code had them reversed.

def test_normal_range():
    # Normal difficulty should have a max of 50, not 100
    low, high = get_range_for_difficulty("Normal")
    assert (low, high) == (1, 50)

def test_hard_range():
    # Hard difficulty should have a max of 100, not 50
    low, high = get_range_for_difficulty("Hard")
    assert (low, high) == (1, 100)


# Bug 2: The hint messages in check_guess were inverted.
# When your guess is too high, the hint should tell you to go LOWER — not HIGHER.
# When your guess is too low, the hint should tell you to go HIGHER — not LOWER.

def test_too_high_gives_lower_hint():
    # Guessing 60 when secret is 50 means we went too high — hint should say go LOWER
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message

def test_too_low_gives_higher_hint():
    # Guessing 40 when secret is 50 means we went too low — hint should say go HIGHER
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_correct_guess_is_win():
    # Guessing exactly the secret number should return a Win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
