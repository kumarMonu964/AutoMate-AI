from app.services.intent_service import classify_intent

def main():

    test_messages = [
        "What does a shock absorber do?",
        "I want to repair my shock absorber.",
        "I want to replace my brake pads.",
        "How much will a shock absorber cost?",
        "How much does clutch replacement take?",
        "Should I repair or replace my alternator?",
        "My suspension is making noise.",
        "Tell me the weather tomorrow."
    ]

    for message in test_messages:

        print("\nCustomer:", message)

        result = classify_intent(message)

        print("Intent:", result.intent)
        print("Confidence:", result.confidence)
        print("Reason:", result.reason)

if __name__ == "__main__":
    main()