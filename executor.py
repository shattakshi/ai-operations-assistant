from tools.github_tool import search_github_repositories
from tools.weather_tool import get_weather


def execute_plan(plan):
    """
    Executes each step from the planner.
    Calls the appropriate tool.
    """

    results = []

    for step in plan["steps"]:

        tool = step["tool"].lower()
        action = step["action"]
        input_data = step["input"]

        if tool == "github":
            result = search_github_repositories(input_data)

        elif tool == "weather":
            result = get_weather(input_data)

        else:
            result = {"error": f"Unknown tool {tool}"}

        results.append({
            "tool": tool,
            "action": action,
            "input": input_data,
            "output": result
        })

    return results
