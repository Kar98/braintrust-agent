# Use setup_genai to automatically trace all Google GenAI API calls
import os

import braintrust
from braintrust.wrappers.google_genai import setup_genai
from google.genai import types
from google.genai.client import Client

bt_project_name = os.environ.get("PROJECT_NAME")
gcp_project_name = os.environ.get("GOOGLE_CLOUD_PROJECT")
gcp_location = os.environ.get("GOOGLE_CLOUD_LOCATION")

setup_genai(project_name=bt_project_name)

# Create a native Google GenAI client
client = Client(vertexai=True, project=gcp_project_name, location=gcp_location)

with braintrust.start_span("rc-test"):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            types.Content(
                role="user",
                parts=[types.Part(text="Come up with a list of at least 5 words that a cup can be made from. Then choose one of the words randomly from the list. Return a single word")],
            )
        ],
    )
    if response.parts:
        for part in response.parts:
            print(part.text)
