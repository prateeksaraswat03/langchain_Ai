from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()

client = InferenceClient(
    api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN")
)

print(
    client.chat_completion(
        messages=[{"role": "user", "content": "Hello"}],
        model="google/gemma-2-2b-it"
    )
)