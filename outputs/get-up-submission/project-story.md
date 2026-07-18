# Get up! — Turn Intention into Action

## Inspiration

Knowing what to do is often not the real problem. The hardest part is taking the first step.

People make schedules, set reminders, and write long to-do lists, yet still struggle to begin studying, exercise, clean a room, or start an important assignment. Traditional productivity tools are good at organizing work, but they can add more decisions at the exact moment when a user already feels overwhelmed.

We built **Get up!** around a simple idea:

> Motivation does not always come before action. Sometimes action creates motivation.

We wanted an action coach that does not produce another intimidating plan. Instead, it identifies the smallest meaningful action a user can take right now.

## What it does

Get up! turns an overwhelming goal into one clear next action.

A user describes what they need to begin—for example:

> I need to study for tomorrow's exam, but I feel overwhelmed.

Get up! responds with a concrete first move, a short time estimate, and one supportive sentence. After the user clicks **Done**, it reveals the next manageable action. If the step still feels too difficult, **Make it smaller** reduces the action again without judging the user or forcing them to restart.

The public deployment runs in a clearly labeled, credential-free demo mode so judges can test the entire interaction immediately. The repository also contains an optional GPT-5.6 path using the OpenAI Responses API; when an API key is configured, the same interface produces personalized actions from the user's goal and progress feedback.

## How we built it

We built Get up! with **Python**, **Streamlit**, **Codex**, and the **OpenAI Responses API**.

The application has a dual-mode action engine:

1. With an `OPENAI_API_KEY`, it sends the goal, feedback, and previous action to GPT-5.6 through the Responses API.
2. Without a key, it selects a small sequence from local demo plans for studying, writing, cleaning, exercise, or a general goal.
3. Both modes return the same `action`, `estimate`, and `encouragement` structure, so the interface and progress loop behave consistently.

For the GPT-5.6 path, we designed a strict prompt that requests exactly one physical or observable action and valid JSON. We validate the required fields before rendering them and escape output used inside the styled HTML card.

Codex was our primary build environment. Working with GPT-5.6 in Codex, we shaped the product concept, designed the one-action interaction, implemented the Streamlit state flow, refined the structured prompt, added the safe demo fallback, tested the **Done** and **Make it smaller** paths with Streamlit AppTest, prepared the repository, and deployed the app to Streamlit Community Cloud.

## Challenges we ran into

### Making responses immediately actionable

Encouraging advice can still be too vague. Suggestions such as “stay focused” or “manage your time” do not help someone begin. We constrained each result to an observable action that can usually be attempted within a few minutes.

### Keeping the experience small

Generative systems naturally produce comprehensive plans. For a user who is already stuck, more information can create more resistance. We deliberately show one action at a time and reveal the next step only after the user responds.

### Creating a public demo without sharing credentials

Embedding a private API key in a public application would be unsafe, and requiring every judge to supply a paid key would make the demo difficult to test. We solved this with a transparent dual-mode architecture: deterministic local guidance for the public demo and an optional GPT-5.6 Responses API path for personalized use.

### Balancing support with pressure

An action coach needs to be direct without becoming judgmental. We refined the tone and fallback actions to acknowledge difficulty, avoid guilt, and keep attention on visible progress.

## Accomplishments that we're proud of

We are proud that Get up! converts a vague intention into an action a user can perform immediately.

The working prototype demonstrates:

- one-action-at-a-time guidance;
- progress after clicking **Done**;
- a smaller recovery action when the user feels stuck;
- a consistent interface across demo and GPT-5.6 modes;
- a public deployment that requires no login or credentials;
- a tested, documented OpenAI Responses API integration in the repository.

Most importantly, Get up! does not try to maximize the amount of advice generated. It tries to maximize the chance that a user actually begins.

## What we learned

We learned that procrastination is not only a scheduling problem. It can also come from uncertainty, decision fatigue, emotional resistance, or a first step that still feels too large.

We also learned that shorter AI outputs can be more useful than longer ones. A single specific action may create more progress than a perfect ten-step plan.

Building with Codex and GPT-5.6 reinforced another product principle: AI should not replace the user's choices. It should reduce friction, make the next decision easier, and help the user act on goals they already care about.

## What's next for Get up!

Next, we want to test Get up! with real users and compare task-start rates between generic reminders, local demo guidance, and personalized GPT-5.6 actions.

Future directions include:

- personalized coaching styles;
- optional voice interaction;
- calendar and task-manager integration;
- focus timers and reminders;
- progress history and habit insights;
- specialized modes for studying, exercise, work, and daily routines;
- user-controlled privacy and data-retention settings.

**Get up! does not ask you to finish everything at once. It helps you begin.**
