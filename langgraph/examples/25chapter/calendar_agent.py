from langchain.agents import create_agent
from langchain_core.tools import tool

from dotenv import load_dotenv

load_dotenv()

CALENDAR_SYSTEM_PROMPT = (
    "You are a calendar scheduling assistant. "
    "Parse natural language scheduling requests (e.g., 'next Tuesday at 2pm"
    "into proper ISO datetime formats. "
    "Use get_available_time_slots to check availability when needed. "
    "Use create_calendar_event to schedule events."
    "Always confirm what was scheduled in your fina1 response."
)

@tool
def get_available_time_slots() ->list[str]:
    """create"""
    return ["09:00","14:00","16:00"]

@tool
def create_calendar_event(title:str,start_time:str,end_time:str,attendess:list[str]) -> str:
    """Create a calendar event. Requires exact ISO datetime format."""
    return f"Event create :{title} from {start_time} to {end_time} at {attendess}"



calendar_agent = create_agent(
    model="deepseek:deepseek-chat",
    system_prompt=CALENDAR_SYSTEM_PROMPT,
    tools=[get_available_time_slots,create_calendar_event]
)

def test_calendar_agent():
    query = "schedule a team meeting ['design-team@abc.com'] on 2025-11-15 at 2pm 1 hour"
    for event in create_calendar_event.stream(
        {"messages":{"role":"user","content":query}},
        stream_mode="values",
    ):
        message = event["messages"][-1].prettry_print()
        print(message)


