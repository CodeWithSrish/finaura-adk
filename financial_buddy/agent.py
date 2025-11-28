from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from .sub_agents.data_analyst.agent import data_analyst_agent
from .sub_agents.execution_analyst.agent import execution_analyst_agent
from .sub_agents.risk_analyst.agent import risk_analyst_agent
from .sub_agents.trading_analyst.agent import trading_analyst_agent


MODEL = "gemini-2.0-flash"

financial_coordinator = LlmAgent(
    name="financial_buddy",
    model=MODEL,
    instruction=prompt.FINANCIAL_COORDINATOR_PROMPT,
    description=(
        "An advanced AI financial assistant that coordinates expert sub-agents "
        "to analyze spending, evaluate stocks, build trading strategies, "
        "generate charts, create savings projections, and provide insights."
    ),
    tools=[
        AgentTool(agent=data_analyst_agent),
        AgentTool(agent=trading_analyst_agent),
        AgentTool(agent=execution_analyst_agent),
        AgentTool(agent=risk_analyst_agent),
    ],
    output_key="analysis"
)

root_agent = financial_coordinator
