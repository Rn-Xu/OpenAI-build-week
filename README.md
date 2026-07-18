# Get up!

**Turn intention into action.**

Get up! is an AI action coach that turns an overwhelming goal into one small, immediately achievable action. It focuses on the moment before productivity begins: taking the first step.

![Get up! cover](assets/get-up-cover.png)

## What it does

- Accepts a goal in natural language.
- Generates one concrete first action instead of a long plan.
- Provides the next step after the user clicks **Done**.
- Makes an action substantially smaller when the user clicks **Make it smaller**.
- Keeps the interaction supportive, concise, and focused on progress.

## Built with

- OpenAI Responses API
- Codex
- Python
- Streamlit

## Run locally

1. Create and activate a Python virtual environment.
2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set your API key locally. Never commit it:

   ```bash
   export OPENAI_API_KEY="your-key-here"
   ```

4. Start the app:

   ```bash
   streamlit run app.py
   ```

The default model is `gpt-5.6-luna`. To select another supported model, set `OPENAI_MODEL` in your environment or Streamlit Secrets.

## Deploy on Streamlit Community Cloud

1. Fork or clone this repository to your GitHub account.
2. Create a Streamlit Community Cloud app using `app.py` as the entry point.
3. In the app's Secrets settings, add:

   ```toml
   OPENAI_API_KEY = "your-key-here"
   OPENAI_MODEL = "gpt-5.6-luna"
   ```

4. Deploy and test the public URL in a private browser window.

## Safety and privacy

- API credentials are read only from environment variables or Streamlit Secrets.
- The repository ignores local secret files.
- Get up! is a productivity aid, not a medical product or emergency service.
- The prototype does not persist user goals to a database.

## OpenAI Build Week

Get up! was created for OpenAI Build Week as an experiment in using AI to reduce the friction between intention and action.

## Concept gallery

The images below are concept mockups for the Build Week project page. Replace them with screenshots from the deployed application when possible.

![Goal input concept](assets/gallery/02-goal-input-concept.png)
![First action concept](assets/gallery/03-first-action-concept.png)
![Adaptive guidance concept](assets/gallery/04-adaptive-guidance-concept.png)
![Completion concept](assets/gallery/05-completion-concept.png)

