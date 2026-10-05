from pathlib import Path

from streamlit.testing.v1 import AppTest

APP_PATH = str(Path(__file__).resolve().parent.parent / "app.py")


def start_app():
    return AppTest.from_file(APP_PATH).run()


def click_new_game(at):
    new_game = next(b for b in at.button if b.label == "New Game 🔁")
    return new_game.click().run()


def end_game_with(at, status):
    at.session_state.status = status
    at.session_state.attempts = 8
    at.session_state.score = 40
    at.session_state.history = [10, 20, 30]
    return at.run()


def test_new_game_after_loss_starts_playing_again():
    # Bug: status stayed "lost", so the app kept stopping on "Game over"
    at = end_game_with(start_app(), "lost")
    assert at.error[0].value == "Game over. Start a new game to try again."

    click_new_game(at)

    assert at.session_state.status == "playing"
    assert not at.error


def test_new_game_after_win_starts_playing_again():
    # Bug: status stayed "won", so the app kept stopping on "You already won"
    at = end_game_with(start_app(), "won")

    click_new_game(at)

    assert at.session_state.status == "playing"
    assert "You already won" not in [s.value for s in at.success]


def test_new_game_resets_attempts_score_and_history():
    # Bug: score and history carried over from the previous game
    at = end_game_with(start_app(), "playing")

    click_new_game(at)

    assert at.session_state.attempts == 0
    assert at.session_state.score == 0
    assert at.session_state.history == []


def test_new_game_shows_full_attempts():
    # Bug: attempts started at 1, so Normal showed 7 attempts left instead of 8
    at = click_new_game(start_app())
    assert "Attempts left: 8" in at.info[0].value


def test_fresh_game_and_new_game_start_the_same():
    at = start_app()
    assert at.session_state.attempts == 0

    click_new_game(at)
    assert at.session_state.attempts == 0


def test_new_game_secret_uses_difficulty_range():
    # Bug: the new secret was always picked from 1-100, even on Easy (1-20)
    at = start_app()
    at.sidebar.selectbox[0].select("Easy").run()

    for _ in range(30):
        click_new_game(at)
        assert 1 <= at.session_state.secret <= 20


def test_new_game_shows_confirmation_message():
    # Bug: st.rerun() wiped the message before it could be seen
    at = click_new_game(start_app())
    assert "New game started." in [s.value for s in at.success]


def test_new_game_clears_guess_box():
    at = start_app()
    at.text_input[0].input("42").run()

    click_new_game(at)

    assert at.text_input[0].value == ""


def test_can_play_after_new_game():
    # End to end: lose, start over, then win the new game
    at = end_game_with(start_app(), "lost")
    click_new_game(at)

    at.text_input[0].input(str(at.session_state.secret)).run()
    submit = next(b for b in at.button if b.label == "Submit Guess 🚀")
    submit.click().run()

    assert at.session_state.status == "won"
