# Get up! — Turn Intention into Action

## Inspiration

Knowing what to do is often not the real problem. The hardest part is taking the first step.

People make schedules, set reminders, and write long to-do lists, yet still struggle to get out of bed, begin studying, exercise, or start an important assignment. Traditional productivity tools are good at organizing work, but they often add more decisions at the exact moment when a user already feels overwhelmed.

We built **Get up!** around a simple idea:

> Motivation does not always come before action. Sometimes action creates motivation.

We wanted to create an AI action coach that does not produce another intimidating plan. Instead, it helps a user identify the smallest meaningful action they can take right now.

## What it does

Get up! turns an overwhelming goal into one clear next action.

A user describes what they need to do in natural language—for example:

> I need to study for tomorrow's exam, but I feel overwhelmed.

Rather than returning a long checklist, Get up! suggests a small first step:

> Put your phone aside and open your notes. Estimated time: one minute.

After completing the step, the user receives the next manageable action. If the step still feels too difficult, the user can say they are stuck and request an even smaller step. This creates a simple loop:

1. Describe the goal.
2. Take one small action.
3. Report progress or difficulty.
4. Receive an adapted next step.
5. Continue until the task has genuinely started or is complete.

The experience focuses on reducing decision fatigue, lowering the emotional barrier to starting, and building momentum through visible progress.

## How we built it

We built Get up! as a lightweight AI-guided workflow using **Python**, **Streamlit**, and the **OpenAI API**.

The application sends the user's goal and current feedback to the model using a structured prompt. The model returns a concise action containing:

- one concrete next step;
- a short time estimate;
- a supportive explanation;
- a smaller fallback action when the user is stuck;
- a clear completion condition.

The Streamlit interface keeps the interaction focused on one action at a time. The application updates the next prompt based on whether the user completed the action or asked for a smaller step.

We used **Codex** during OpenAI Build Week to shape the product concept, prototype the interface, refine the prompting logic, debug the workflow, and prepare the project for demonstration.

## Challenges we ran into

### Making AI responses immediately actionable

Early responses could sound encouraging while remaining too generic. Advice such as “stay focused” or “manage your time” does not help a user begin. We constrained the response format so every suggestion starts with a physical or observable action that can be attempted within a few minutes.

### Keeping the experience small

AI naturally tends to produce comprehensive plans. For a procrastinating user, more information can create more resistance. We deliberately show one action at a time and reveal the next step only after the user responds.

### Handling moments of failure

Real users get distracted or discover that a step is still too difficult. Instead of treating this as failure, Get up! offers a smaller recovery action. The user can continue without restarting the entire plan.

### Balancing support with pressure

An action coach needs to be direct without becoming judgmental. We refined the tone to acknowledge difficulty, avoid guilt, and keep attention on achievable progress.

## Accomplishments that we're proud of

We are proud that Get up! converts a vague intention into an action a user can perform immediately.

The prototype demonstrates a focused interaction in which AI can:

- turn an overwhelming goal into a concrete first step;
- guide progress one action at a time;
- reduce a difficult step when the user feels stuck;
- help the user recover without judgment;
- create momentum without requiring a complex productivity system.

Most importantly, the project does not try to maximize the amount of advice generated. It tries to maximize the chance that the user actually begins.

## What we learned

We learned that procrastination is not only a scheduling problem. It can also be caused by uncertainty, emotional resistance, decision fatigue, or a first step that feels too large.

We also learned that shorter AI responses can be more useful than longer ones. A single specific action may produce more progress than a perfect ten-step plan.

Building Get up! reinforced an important product principle: AI should not replace a user's choices. It should reduce friction, make the next decision easier, and help the user act on goals they already care about.

## What's next for Get up!

Next, we want to test Get up! with real users and measure whether smaller AI-generated actions improve task-start rates.

Future directions include:

- personalized coaching styles;
- optional voice interaction;
- calendar and task-manager integration;
- focus timers and reminders;
- progress history and habit insights;
- specialized modes for studying, exercise, work, and daily routines;
- user-controlled privacy and data-retention settings.

Our long-term vision is a daily AI companion that does not merely remind people about their goals, but helps them through the hardest part: getting started.

**Get up! does not ask you to finish everything at once. It helps you begin.**

