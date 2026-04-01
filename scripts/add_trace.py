import braintrust
from braintrust.wrappers.google_genai import setup_genai
from google.genai import types
from google.genai.client import Client

# Use setup_genai to automatically trace all Google GenAI API calls
setup_genai(project_name="RC Project")

# Create a native Google GenAI client
client = Client(vertexai=True, project="kablamo-labs-sandbox", location="us-central1")

with braintrust.start_span("rc-test"):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            types.Content(
                role="user",
                parts=[
                    types.Part(
                        text="Come up with a list of at least 5 words that a cup can be made from. Then choose one of the words randomly from the list. Return a single word"
                    )
                ],
            )
        ],
    )
    print(response.text)
    if response.parts:
        for part in response.parts:
            print(part.text)
