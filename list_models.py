import google.generativeai as genai
import sys

# Configure API key
genai.configure(api_key="YOUR_API_KEY")

print("Listing all available models...")

try:
    for m in genai.list_models():
        print(f"Name: {m.name}")
        print(f"Methods: {m.supported_generation_methods}")
        print()

except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)