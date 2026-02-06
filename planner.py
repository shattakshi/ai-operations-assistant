from llm.llm_config import get_llm
import json


def create_plan(task: str):
    """
    Generates a step-by-step plan using the LLM.
    Returns parsed JSON.
    """

    llm = get_llm()

    prompt = f"""
You are an AI planner.

Break the user task into steps using ONLY this JSON format:

{{
  "steps": [
    {{
      "tool": "github or weather",
      "action": "what to do",
      "input": "search query or city"
    }}
  ]
}}

Available tools:

- github → returns top 3 repositories automatically
  (DO NOT create multiple github steps)

- weather → get current weather by city


Return ONLY valid JSON.
Do not add explanations.

User task: {task}
"""

    response = llm.invoke(prompt)

    content = response.content.strip()

    # Remove markdown if LLM adds it
    content = content.replace("```json", "").replace("```", "")

    plan = json.loads(content)

    return plan
