# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input           | Expected Behavior | Actual Behavior | Console Output / Error |
|--------------|-------------------|-----------------|------------------------|
| Switching difficulty toggle between "Normal/Medium" and "Hard" | Medium should be 1–50 and Hard should be 1–100 | The ranges are swapped — Medium shows 1–100 and Hard shows 1–50 | No error; wrong ranges returned silently by `get_range_for_difficulty()` in `app.py` |
| Switching difficulty mid-game | Secret number, attempts, and score should reset and reflect the new difficulty's range (e.g. Easy: 1–20) | Game state carries over — secret number stays the same regardless of difficulty, so it can be out of range (e.g. secret is 38 on Easy 1–20); all difficulty levels behave the same | No error; state is shared across difficulties with no reset |
| Inputting a number to guess | The guess should appear in the history list inside the debugger immediately after submitting | Nothing appears in the history list until the next guess is submitted — history is always one step behind | No error; display update is delayed by one rerun cycle |
| Clicking "New Game" to restart | All game state should reset — message cleared, history wiped, input re-enabled | "Game over. Start a new game to try again." message persists, history list keeps previous outputs, and the game stays frozen; only the secret number updates | Error message "Game over. Start a new game to try again." ; session state is not fully cleared on restart |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
