from app.core.llm import llm
from app.schemas.service_request import ServiceRequest


structured_extractor = llm.with_structured_output(
    ServiceRequest
)


EXTRACTION_PROMPT = """
You are the information extraction component of AutoMate AI.

Extract information from the customer's message.

Your task is to identify:

1. Vehicle manufacturer.
2. Vehicle model or variant.
3. Manufacturing year.
4. Fuel type.
5. Car part.
6. Requested operation.
7. Requested information.

OPERATION RULES:

- repair: Customer explicitly wants to repair or fix a part.
- replacement: Customer explicitly wants a new part installed
  or an existing part replaced.
- comparison: Customer explicitly wants to compare repair
  and replacement.
- unknown: The operation is not clear.

REQUESTED INFORMATION RULES:

- cost: Customer asks about price or charges.
- time: Customer asks about repair or installation duration.
- repair_availability: Customer asks whether a part can be repaired.
- general_information: Customer asks a general informational question.
- unknown: The requested information is unclear.

IMPORTANT:

- Extract only information explicitly provided by the customer.
- Do not infer vehicle details.
- Do not diagnose mechanical problems.
- Do not assume repair or replacement from a symptom.
- If information is missing, return null.
- Do not invent a part name.
- If the customer says "shock absorber", extract "Shock Absorber".
- Preserve the customer's actual meaning.
"""


def extract_service_request(message: str) -> ServiceRequest:

    response = structured_extractor.invoke([
        ("system", EXTRACTION_PROMPT),
        ("human", message)
    ])

    return response