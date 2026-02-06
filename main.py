from fastapi import FastAPI
from pydantic import BaseModel

from agents.planner import create_plan
from agents.executor import execute_plan
from agents.verifier import verify_results


app = FastAPI(
    title="AI Operations Assistant",
    description="A multi-agent AI system that plans tasks, executes tools, and verifies results.",
    version="1.0"
)



class TaskRequest(BaseModel):
    task: str


@app.get("/")
def home():
    return {"message": "AI Ops Assistant is running"}


@app.post("/run-task")
def run_task(request: TaskRequest):

    # 1️⃣ Planner
    plan = create_plan(request.task)

    # 2️⃣ Executor
    execution_results = execute_plan(plan)

    # 3️⃣ Verifier
    final_output = verify_results(execution_results)

    
    return {
    "status": final_output["status"],
    "data": execution_results
}

    
