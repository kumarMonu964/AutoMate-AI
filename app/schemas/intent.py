from typing import Literal

from pydantic import BaseModel, Field

class IntentResult(BaseModel):

    intent: Literal[
        "general_enquiry",
        "repair_enquiry",
        "replacement_enquiry",
        "cost_enquiry",
        "time_enquiry",
        "repair_vs_replacement",
        "unclear_intent",
        "out_of_scope"
    ] = Field(
        description="The primary intent of the customer's message"

    )

    confidence: float = Field(
        ge=0,
        le=1,
        description="Confidence in the classification, from 0 to 1."
    )

    reason: str = Field(
        description="A short explanation of why this intent was selected."
    )

