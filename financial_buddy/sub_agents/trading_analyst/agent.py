from google.adk.agents import LlmAgent

trading_analyst_agent = LlmAgent(
    name="trading_analyst_agent",
    model="gemini-2.0-flash",
    instruction="""
You are a Trading Strategy Analyst Agent.
Based on user goals and market analysis, propose trading ideas,
entry/exit points, time horizons, and possible strategies (swing, long-term, etc.).
""",
    output_key="analysis" ,
    description="Creates trading strategies based on market predictions.",
)

def handler(input):
    summary = analyze_spending(input)  
    return {"analysis": insights}
