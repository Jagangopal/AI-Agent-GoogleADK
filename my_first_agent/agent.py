from google.adk.agents.llm_agent import LlmAgent
from pydantic import BaseModel, Field

# Define schemas for structured input and output
class GreetingRequest(BaseModel):
    """Input schema for specifying the language of the greeting."""
    language: str = Field(description="The language to greet the user in.")

class GreetingResponse(BaseModel):
    """Output schema for the structured greeting response."""
    greeting_message: str = Field(description="The final, formatted greeting.")

root_agent = LlmAgent(
    name='greeting_agent',
    model='gemini-2.5-flash',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge',
    input_schema=GreetingRequest,
    output_schema=GreetingResponse,
    output_key='final_greeting',
)