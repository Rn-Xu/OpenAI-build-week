# Public YouTube demo script — target 2:35

Record the real product in landscape orientation. Keep the cursor visible, enlarge the browser, and hide notifications, email, local paths, account details, and credentials. The final YouTube video must be **Public**, include English voice-over, and remain under three minutes.

## 0:00–0:15 — The problem

**Visual:** Show the Get up! landing screen.

**Voice-over:**

> Most productivity tools help us organize everything we need to do. But when a task feels overwhelming, the hardest part is often much smaller: taking the first step. That is why I built Get up!

## 0:15–0:32 — The product

**Visual:** Keep the goal input and Demo mode label visible.

**Voice-over:**

> Get up! is an action coach that turns an overwhelming goal into one immediate, achievable move. The public app runs in a free, clearly labeled demo mode, so anyone can test it without an account or API key.

## 0:32–1:02 — Generate the first action

**Visual:** Enter `I need to study for tomorrow's exam, but I feel overwhelmed.` Click **Help me begin** and show the resulting action card.

**Voice-over:**

> I describe my goal in ordinary language. Instead of a long checklist, Get up! gives me one observable action, a realistic time estimate, and a short supportive message. Here, it asks me to put the study material in front of me and open it. That is small enough to do immediately.

## 1:02–1:25 — Continue and recover

**Visual:** Click **Done**, show the next action, then click **Make it smaller**.

**Voice-over:**

> When I click Done, the app gives me the next manageable step and records visible progress. If that step still feels difficult, Make it smaller reduces the action again instead of judging me or making me restart.

## 1:25–1:50 — Architecture and GPT-5.6

**Visual:** Show the GitHub README section “How Codex and GPT-5.6 were used,” then briefly show `generate_action` in `app.py`.

**Voice-over:**

> The app has a dual-mode architecture. Without credentials, local demo plans keep the public experience reliable. When an OpenAI API key is configured, the same generate-action function uses the OpenAI Responses API with GPT-5.6 and validates a structured action, estimate, and encouragement response.

## 1:50–2:22 — How Codex accelerated the build

**Visual:** Show the Git commit history and the README evidence section. Optionally show a brief, non-sensitive view of the primary Codex thread.

**Voice-over:**

> I used Codex with GPT-5.6 as the primary development workflow. It helped turn the product idea into the one-action interaction contract, implement Streamlit session state, refine the structured prompt, harden model output before HTML rendering, add the no-key demo fallback, test the main interaction paths with Streamlit AppTest, and deploy the project. The submitted feedback Session ID links to the primary build thread.

## 2:22–2:35 — Close

**Visual:** Return to the working app and show one completed action.

**Voice-over:**

> Get up! does not ask people to finish everything at once. It helps them begin—because motivation does not always create action. Sometimes action creates motivation.

## Recording checklist

- Public YouTube video, not Unlisted or Private.
- 16:9, preferably 1080p.
- Final duration under 3:00; target 2:35.
- English voice-over is audible throughout.
- Show the real live app, the Codex/GPT-5.6 README section, and the relevant code path.
- Add corrected English captions using the narration above.
- Use `media/01-get-up-cover.png` as the thumbnail.
