from google.adk.agents import LlmAgent

risk_analyst_agent = LlmAgent(
    name="risk_analyst_agent",
    model="gemini-2.0-flash",
    instruction="""
You are a Risk Analyst Agent.
Evaluate risks in user portfolios, trading strategies, markets, and execution plans.
Assess volatility, diversification, and risk exposure.
""",
    output_key="analysis" ,
    
    description="Evaluates financial and portfolio risk.",
)

def handler(input):
    summary = analyze_spending(input)  
    return {"analysis": result}
