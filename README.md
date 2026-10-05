# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
-- the game tries to guide the user with guessing a random number picked by the game.
- [ ] Detail which bugs you found.
-- I found that the game failed to notice whether the input was actually higher or lower than the number the game picked, giving wrong hints to the user.
- [ ] Explain what fixes you applied.
-- users are receiving correct hints, so the game is now more fair. The user can actually starts a new game with fresh attempts, after either losing, winning, or simply starting a new game. 

## 📸 Demo Walkthrough

1. User enters a guess of 38
2. Game returns "Too Low"
3. User enters a guess of 70, and the game shows "Too High"
4. Users have a few attempts left before the game ends
5. If the user guess the number before the last attempt, the user wins and game ends
6. If not, the user has to start a new game

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================
```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
