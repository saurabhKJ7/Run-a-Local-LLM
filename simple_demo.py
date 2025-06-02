import requests
import json

# LM Studio API endpoint
API_URL = "http://127.0.0.1:1234/v1/chat/completions"

def send_prompt(prompt):
    """Send a prompt to LM Studio and get AI response"""
    payload = {
        "model": "deepseek-r1-distill-qwen-7b",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 100
    }
    
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(API_URL, json=payload, headers=headers, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            return result['choices'][0]['message']['content']
        else:
            return f"Error: {response.status_code} - Check if model is loaded in LM Studio"
            
    except requests.exceptions.ConnectionError:
        return "Error: Cannot connect to LM Studio. Make sure it's running on http://127.0.0.1:1234"
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # Test prompt
    prompt = "What is a local LLM?"
    
    print(f"Prompt: {prompt}")
    print(f"AI Response: {send_prompt(prompt)}")