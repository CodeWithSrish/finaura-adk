from google.adk.agents import LlmAgent

execution_analyst_agent = LlmAgent(
    name="execution_analyst_agent",
    model="gemini-2.0-flash",
    instruction="""
You are an Execution Analyst Agent.
Translate trading strategies into executable steps.
Define order types, position sizing, timing, and execution plans.
You create step-by-step investment plans and portfolios.
""",
    output_key="analysis" ,
    description="Turns trading strategy into actionable execution plan.",
)

def handler(input):
    summary = analyze_spending(input)  
    return {"analysis": plan}