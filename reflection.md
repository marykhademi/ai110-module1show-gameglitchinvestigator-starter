# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it? The game did not look broken in the first few try but it started to act irrational. Because I entered 99, and it still told me to go higher. That's when I realized the game logic is broken.
- List at least two concrete bugs you noticed at the start
  1. the hints were not correct since it was telling me to go higher even though the secret number was lower than my input.
  2. I could not start a new game even though I was out of attempts and lost the game.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
| ----- | ----------------- | --------------- | ---------------------- |
| guess 40 when the secret is lower than 40 | Hint says go lower | Hint says go higher (the hint messages were flipped) | no error, the hint was just  wrong |
| when the game is over, then we want to start a new game | we want to see a new game with full attempts, score 0, and an empty history | however, the page still says "Game over. Start a new game to try again." | none. `st.stop()` ends the run in the backend, not frontend |
| secret is 50. our guess 9, then guess 9 again | we see the same too low outcome again | the first guess was too high and the second was too low. when doing even attempts the secret became a string, so `"9" > "50"` was compared in an alphabetical order | no error. the `TypeError` was caught and the code kept comparing strings |
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  Answer: the AI suggested to clear the old guesses when a new entry would be tried or the old guess is submitted, but the in the old version, the old guesses never disappeared, which I noticed when trying to see if the number of attempts change if I try submitting the same guess over and over, and it sure did.
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
  -- There was none.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? By running the tests and testing the game again.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
  I tried entering multiple numbers to see if the game still tells me to go higher or not. Also, i verified that the old guess disappeared after submitting it, and the attempts reset when a new game is started.
- Did AI help you design or understand any tests? How? Yes, the agent walked me through the tests and how the fixed logic would pass the tests. For example, the tests would only need the outcome of whether a number is higher than the secret number or not, but the game would only need both the outcome and the message, so with the help of the agent, we changed it to only see the outcome for tests.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit? streamlit is like refreshing a webpage or like waiting in line to buy a concert ticket. To see your line moving, you need to check on the status and see how it's changing. However, the state is not gonna stay the same, the ticket counter would be in the same place, the banner, the line, etc. would be the same everytime you visits, but every visit is different because the variable affecting buying a ticket is different.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  -- Try to investigate the bug on my own first, and understand how the code works/behaves to be able to ask better questions if I decide to use AI to help me with fixing the code.
- What is one thing you would do differently next time you work with AI on a coding task?
  -- I would try to take it one step a time, and not accept the fix, and try to fix it on my own before accepting any AI solutions. Use AI as a guide to understand how to fix a bug or better a code.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  --- It might not look buggy or without issues but at the end of the day, it's a human user trying to use it, and it's the human touch the AI lack for now - it might not in the future, but the human experience can't be coded, so it's needed that we understand how AI work and utilize it for the betterment of the society.
