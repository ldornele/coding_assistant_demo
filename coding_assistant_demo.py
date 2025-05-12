from langchain_community.llms import VLLMOpenAI
import sys
import os

API_URL = "https://granite-3-1-8b-instruct-w4a16-maas-apicast-production.apps.prod.rhoai.rh-aiservices-bu.com:443"
API_KEY = "***************************"



llm = VLLMOpenAI(
    openai_api_key=API_KEY,
    openai_api_base=API_URL+"/v1",
    model_name="granite-3-1-8b-instruct-w4a16",
    temperature=0.2,    
)

def review_golang_code(code):
    prompt = f"""You are an experienced Go code reviewer. Review the following code and point out potential errors, style improvement suggestions, security issues, and refactoring opportunities:\n\n```go\n{code}\n```\n\nProvide your feedback clearly and concisely, listing the issues found and suggestions for correction."""
    feedback = llm.invoke(prompt)
    return feedback

if __name__ == "__main__":
    if len(sys.argv) > 1:
        code_file = sys.argv[1]
        try:
            with open(code_file, "r") as f:
                golang_code = f.read()
            feedback = review_golang_code(golang_code)
            print("Review Feedback:\n")
            print(feedback)
        except FileNotFoundError:
            print(f"Error: File not found: {code_file}")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")
            sys.exit(1)
    else:
        print("Usage: python your_script.py <golang_file>")
        print("Or you can pipe the code through standard input.")
        golang_code = sys.stdin.read()
        if golang_code:
            feedback = review_golang_code(golang_code)
            print("Review Feedback:\n")
            print(feedback)
        else:
            print("No GoLang code provided.")
            sys.exit(1)
