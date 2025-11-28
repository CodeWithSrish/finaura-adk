from google.adk.agents import LlmAgent

data_analyst_agent = LlmAgent(
    name="data_analyst_agent",
    model="gemini-2.0-flash",
    instruction="""
You are a Data Analyst Agent.
Analyze financial data, stock prices, market trends, or user-provided datasets.
Provide insights, summaries, and structured analysis.
""",
    output_key="analysis" ,
    description="Analyzes data and extracts insights.",
)


def handler(input):
    summary = analyze_spending(input)  
    return {"analysis": summary} 