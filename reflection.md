# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
When I first ran the game, it looked legitimate at first glance. There was text input, a submit button, and a score display. There was a new game button and options to select difficult levels for the game. The game displayed "Guess a number between 1 and 100" no matter which difficulty I chose, so the UI was misleading too.

- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  1. The hints were flipped meaning if my guess was too low, it told me to go lower and if it was too high, it told me to go higher, sending me in the wrong direction with my guesses

  2. The New Game button ignores difficulty and just always chooses a number 1-100

  3. The difficulty range doesn't make sense. Hard should have the widest range, but Normal has a wider range than Hard

  4. the scoring calculation is off
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Claude caught the even/odd attempt bug where the secret gets converted to a string on even turns, making it impossible to win on those attempts. I verified it by submitting guesses on attempt 2 and 4 specifically and confirming it never registered as a win even when I entered the exact secret number.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Claude didn't really mislead me in this project. Everything matched with the code this time around.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided a bug was fixed by playing the game with the developer info panel open so I could see the secret number as I played. 

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
For the hints, I'd enter a number I knew was lower than the secret number and check if that worked as it should. I also tested the New Game button by switching levels and clicking the button, then checking to see if the secret was generating in the correct difficulty range. Claude explained to me how the logic was off for the function checking the guess number against the secret number by showing that the secret was being turned into a string on even attempts which I wouldn't have noticed just by playing the game.
- Did AI help you design or understand any tests? How?
Yes, AI helped by explaining the even/odd attempt bug which showed me I needed to test specifically on even attempts rather than just playing and trying to see what broke.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
Every time you clicked a button, Streamlit re-ran the entire script from top to bottom, and the line generating a new random secret had no guard around it, so it was firing on every single click.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Every time you click a button, Streamlit reruns the whole script like it's starting over. Session state is just a way to save values so they don't get wiped on every rerun.
- What change did you make that finally gave the game a stable secret number?
The fix was wrapping the secret generation in if "secret" not in st.session_state so it only runs an creates once, then stays put.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
Definitely using Claude as I create and test code. Helps explain things and catch things quickly, while allowing me to talk to it in plain language and explain the issues and ideal outcome.
- What is one thing you would do differently next time you work with AI on a coding task?
I would definitely be sure to check each AI suggestion and try to make sure I understand everything instead of blindly trusting it to make those changes.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I was actually very impressed with the AI generated code in this project. I thought that it did really well at catching the issue, explaining why things were happening and providing fixes specific to that. Definitely wouldn't put it down as production-level code without reviewing, but gives a great starting point and helps with efficiency for sure.
