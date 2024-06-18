import requests
import json

# Step 1: Data Collection (text-only)
def fetch_text_data_from_sources():
    # Replace with actual data sources
    data_sources = [
        "https://api.example.com/data1",
        "https://api.example.com/data2"
    ]
    
    text_data = []
    for source in data_sources:
        response = requests.get(source)
        if response.status_code == 200:
            text_data.append(response.text)
    return text_data

# Step 2: Check Data Size with Prompt
def check_data_size_with_prompt(data, max_prompt_size=4096):
    prompt_header = """
    You are an intelligent system that organizes information. Given the following data, extract and return a list of items with each one having a name, a description, a location, a date or a date-window, and a list of tags.
    
    Data:
    """
    prompt_footer = """
    Return a list of items in the following format:
    [
      {
        "name": "<name>",
        "description": "<description>",
        "location": "<location>",
        "date": "<date>",
        "tags": ["<tag1>", "<tag2>", ...]
      },
      ...
    ]
    """
    max_data_size = max_prompt_size - len(prompt_header) - len(prompt_footer)
    
    data_str = "\n".join(data)
    if len(data_str) > max_data_size:
        raise ValueError("Data exceeds the maximum allowed size for the LLM context window.")
    
    return data_str

# Step 3: LLM Prompt Construction
def create_llm_prompt(data_packet):
    prompt = """
    You are an intelligent system that organizes information. Given the following data, extract and return a list of items with each one having a name, a description, a location, a date or a date-window, and a list of tags.
    
    Data:
    """
    prompt += data_packet
    prompt += """
    Return a list of items in the following format:
    [
      {
        "name": "<name>",
        "description": "<description>",
        "location": "<location>",
        "date": "<date>",
        "tags": ["<tag1>", "<tag2>", ...]
      },
      ...
    ]
    """
    return prompt

# Step 4: LLM API Interaction
def send_to_llm(prompt, api_url, api_key):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    response = requests.post(api_url, headers=headers, json={"prompt": prompt})
    return response.json()

# Step 5: Result Parsing
def parse_llm_response(response):
    try:
        return json.loads(response['choices'][0]['text'].strip())
    except (KeyError, IndexError, json.JSONDecodeError):
        return []

# Main Function
def main():
    api_url = "https://groq.com/api/llm"  # Replace with actual Groq API URL
    api_key = "your_groq_api_key"  # Replace with your Groq API key
    
    data = fetch_text_data_from_sources()
    data_str = check_data_size_with_prompt(data)
    
    prompt = create_llm_prompt(data_str)
    response = send_to_llm(prompt, api_url, api_key)
    results = parse_llm_response(response)
    
    # Output the results
    for item in results:
        print(json.dumps(item, indent=2))

if __name__ == "__main__":
    main()
