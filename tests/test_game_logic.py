from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"

def test_too_high_tells_player_to_go_lower():
    # Bug: a guess above the secret used to say "Go HIGHER!"
    _, message = check_guess(60, 50)
    assert "LOWER" in message

def test_too_low_tells_player_to_go_higher():
    # Bug: a guess below the secret used to say "Go LOWER"
    _, message = check_guess(40, 50)
    assert "HIGHER" in message

def test_compares_numerically_not_alphabetically():
    # Bug: the secret was turned into a string on even attempts, so "9" > "50"
    # alphabetically and 9 was reported as "Too High"
    outcome, message = check_guess(9, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message

def test_three_digit_guess_above_two_digit_secret():
    # "100" < "20" alphabetically, but 100 > 20 numerically
    outcome, _ = check_guess(100, 20)
    assert outcome == "Too High"
