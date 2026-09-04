from pydantic import BaseModel


class ChatMessage(BaseModel):

    role: str

    content: str


class AIChatRequest(BaseModel):

    customer_id: str

    question: str

    conversation: list[ChatMessage] = []


class AIChatResponse(BaseModel):

    risk_assessment: str

    key_findings: list[str]

    recommendations: list[str]

    conclusion: str