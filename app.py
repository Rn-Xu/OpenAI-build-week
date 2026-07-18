import json
import os
from html import escape
from typing import Any

import streamlit as st
from openai import OpenAI


APP_TITLE = "Get up!"
DEFAULT_MODEL = "gpt-5.6-luna"

SYSTEM_PROMPT = """You are Get up!, a calm AI action coach.
Your job is to help a user begin a task, not to produce a long plan.

Return only valid JSON with this exact shape:
{
  "action": "one observable action",
  "estimate": "a realistic short time such as 30 seconds or 2 minutes",
  "encouragement": "one short, non-judgmental sentence"
}

Rules:
- Give exactly one action.
- The action must be physical or observable and immediately possible.
- Prefer an action that takes five minutes or less.
- Never shame, diagnose, threaten, or pressure the user.
- If the user completed the previous action, give the next smallest meaningful action.
- If the user is stuck, make the previous action substantially smaller.
- Do not claim the entire goal is complete unless the user explicitly says so.
- If the request suggests immediate danger or self-harm, encourage the user to contact local emergency services or a trusted person now instead of giving productivity advice.
"""


def load_secret(name: str) -> str | None:
    """Read a secret without exposing it in the interface or source code."""
    value = os.getenv(name)
    if value:
        return value

    try:
        secret_value = st.secrets.get(name)
    except (FileNotFoundError, KeyError):
        secret_value = None

    return str(secret_value) if secret_value else None


def parse_action(raw_text: str) -> dict[str, str]:
    cleaned = raw_text.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.removeprefix("```json").removeprefix("```")
        cleaned = cleaned.removesuffix("```").strip()

    payload: Any = json.loads(cleaned)
    if not isinstance(payload, dict):
        raise ValueError("The model response was not a JSON object.")

    action = str(payload.get("action", "")).strip()
    estimate = str(payload.get("estimate", "")).strip()
    encouragement = str(payload.get("encouragement", "")).strip()
    if not action or not estimate or not encouragement:
        raise ValueError("The model response was missing a required field.")

    return {
        "action": action,
        "estimate": estimate,
        "encouragement": encouragement,
    }


def generate_action(goal: str, feedback: str, previous_action: str = "") -> dict[str, str]:
    api_key = load_secret("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not configured.")

    model = load_secret("OPENAI_MODEL") or DEFAULT_MODEL
    client = OpenAI(api_key=api_key)

    context = [f"User goal: {goal}", f"Current feedback: {feedback}"]
    if previous_action:
        context.append(f"Previous action: {previous_action}")

    response = client.responses.create(
        model=model,
        instructions=SYSTEM_PROMPT,
        input="\n".join(context),
        max_output_tokens=300,
    )
    return parse_action(response.output_text)


def reset_session() -> None:
    for key in ("goal", "current_action", "completed_actions", "started"):
        st.session_state.pop(key, None)


st.set_page_config(
    page_title="Get up! — Turn intention into action",
    page_icon="☀️",
    layout="centered",
)

st.markdown(
    """
    <style>
    :root {
        --cream: #fffaf2;
        --ink: #17232d;
        --coral: #ff6746;
        --sage: #74866a;
        --line: #eedfce;
    }
    .stApp {
        background:
            radial-gradient(circle at 82% 5%, rgba(255, 186, 101, .25), transparent 28rem),
            var(--cream);
        color: var(--ink);
    }
    .block-container { max-width: 760px; padding-top: 3rem; }
    .brand { font: 700 2rem Georgia, serif; color: var(--ink); margin-bottom: .25rem; }
    .hero { font: 700 clamp(2.6rem, 7vw, 4.8rem)/1.03 Georgia, serif; letter-spacing: -.04em; }
    .subtitle { color: #53606a; font-size: 1.08rem; max-width: 38rem; margin: 1rem 0 2.3rem; }
    .action-card {
        background: rgba(255,255,255,.82);
        border: 1px solid var(--line);
        border-radius: 24px;
        padding: 2rem;
        box-shadow: 0 18px 55px rgba(91, 57, 31, .08);
        margin: 1rem 0 1.25rem;
    }
    .eyebrow { color: var(--coral); font-weight: 800; letter-spacing: .08em; text-transform: uppercase; }
    .action { font: 700 2rem/1.25 Georgia, serif; color: var(--ink); margin: .7rem 0 1rem; }
    .estimate { color: var(--sage); font-weight: 700; }
    .encouragement { color: #53606a; margin-top: .8rem; }
    .progress-note { color: var(--sage); font-weight: 700; }
    .stButton > button[kind="primary"] { background: var(--coral); border-color: var(--coral); }
    footer { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="brand">Get up! <span style="color:#ff6746">●</span></div>', unsafe_allow_html=True)

if not st.session_state.get("started"):
    st.markdown('<div class="hero">Turn intention<br>into action.</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">Describe what feels difficult. Get one small, achievable action—not another overwhelming plan.</div>',
        unsafe_allow_html=True,
    )

    with st.form("goal_form"):
        goal = st.text_area(
            "What do you need to start?",
            placeholder="I need to study for tomorrow's exam, but I feel overwhelmed.",
            height=125,
            max_chars=600,
        )
        submitted = st.form_submit_button("Help me begin", type="primary", use_container_width=True)

    if submitted:
        if not goal.strip():
            st.warning("Tell Get up! what you need to accomplish first.")
        elif not load_secret("OPENAI_API_KEY"):
            st.error("This demo needs an OpenAI API key configured in Streamlit Secrets.")
        else:
            try:
                with st.spinner("Finding the smallest meaningful step…"):
                    first_action = generate_action(goal.strip(), "The user has not started yet.")
                st.session_state.goal = goal.strip()
                st.session_state.current_action = first_action
                st.session_state.completed_actions = []
                st.session_state.started = True
                st.rerun()
            except Exception as exc:
                st.error("Get up! could not create a step right now. Please try again.")
                st.caption(f"Technical detail: {type(exc).__name__}")

else:
    action = st.session_state.current_action
    completed_count = len(st.session_state.completed_actions)

    st.markdown("## Your next small step")
    if completed_count:
        st.markdown(
            f'<div class="progress-note">✓ {completed_count} small action{"s" if completed_count != 1 else ""} completed</div>',
            unsafe_allow_html=True,
        )

    st.markdown(
        f"""
        <div class="action-card">
            <div class="eyebrow">Do this now</div>
            <div class="action">{escape(action['action'])}</div>
            <div class="estimate">◷ Estimated time: {escape(action['estimate'])}</div>
            <div class="encouragement">{escape(action['encouragement'])}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    done_col, smaller_col = st.columns(2)
    with done_col:
        if st.button("Done", type="primary", use_container_width=True):
            try:
                with st.spinner("Building on that momentum…"):
                    next_action = generate_action(
                        st.session_state.goal,
                        "The user completed the previous action. Give the next smallest meaningful action.",
                        action["action"],
                    )
                st.session_state.completed_actions.append(action)
                st.session_state.current_action = next_action
                st.rerun()
            except Exception as exc:
                st.error("Get up! could not create the next step. Please try again.")
                st.caption(f"Technical detail: {type(exc).__name__}")

    with smaller_col:
        if st.button("Make it smaller", use_container_width=True):
            try:
                with st.spinner("Making this easier…"):
                    smaller_action = generate_action(
                        st.session_state.goal,
                        "The user is stuck. Make the previous action substantially smaller and easier.",
                        action["action"],
                    )
                st.session_state.current_action = smaller_action
                st.rerun()
            except Exception as exc:
                st.error("Get up! could not simplify the step. Please try again.")
                st.caption(f"Technical detail: {type(exc).__name__}")

    st.divider()
    if st.button("Start a different goal"):
        reset_session()
        st.rerun()

    with st.expander("My original goal"):
        st.write(st.session_state.goal)

st.caption("Get up! is a productivity aid, not medical or emergency support.")
