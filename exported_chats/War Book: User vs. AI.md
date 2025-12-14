# War Book: User vs. AI



---



---

i need to alter this to allow a system message and also to append to a file named Book of War.json: import requests
import json
import os

def query_openai(messages, assistant_model):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": assistant_model,
        "messages": messages,
        "max_tokens": 4096
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", json=data, headers=headers)
    if response.status_code != 200:
        print("Error:", response.status_code, response.text)
        return None
    return response.json()

def append_to_json(output_file_path, conversation_history):
    try:
        # Read the current content of the json file
        with open(output_file_path, 'r') as file:
            existing_conversation = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # File does not exist or is empty/invalid; we will create a new list
        existing_conversation = []
    
    # Append the new conversation to the list
    existing_conversation.append(conversation_history)

    # Write the updated conversation back to the file
    with open(output_file_path, 'w') as file:
        json.dump(existing_conversation, file, indent=4)

# Make sure your OpenAI API key is set in an environment variable
api_key = os.environ.get('YOUR_OPENAI_API_KEY')
assistant_model_identifier = 'ft:gpt-3.5-turbo-1106:crown-of-water::8mg0fwHS'


output_path = 'conversation.json'  # Output JSON file
conversation_history = []

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Exiting conversation.")
        break
    conversation_history.append({"role": "user", "content": user_input})
    
    response = query_openai(conversation_history, assistant_model_identifier)
    if response is not None and 'choices' in response:
        assistant_response = response['choices'][0]['message']['content']
        print("Assistant:", assistant_response)
        conversation_history.append({"role": "assistant", "content": assistant_response})
        
        # Save each interaction to the JSON file
        append_to_json(output_path, conversation_history)
    else:
        print("No valid response received.")
        break

---

To modify your script to include a system message and append the conversation history to a file named `Book of War.json`, you can adjust the `output_path` to point to the new file and include a system message in the conversation history. Here's how you can do it:

1. Change `output_path` to `'Book of War.json'`.
2. Add a system message to the `conversation_history` before the loop starts or as part of the loop, depending on when you want the message to appear.

Here's the updated code with these changes:

```python
import requests
import json
import os

def query_openai(messages, assistant_model):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": assistant_model,
        "messages": messages,
        "max_tokens": 4096
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", json=data, headers=headers)
    if response.status_code != 200:
        print("Error:", response.status_code, response.text)
        return None
    return response.json()

def append_to_json(output_file_path, conversation_history):
    try:
        with open(output_file_path, 'r') as file:
            existing_conversation = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_conversation = []
    
    existing_conversation.append(conversation_history)

    with open(output_file_path, 'w') as file:
        json.dump(existing_conversation, file, indent=4)

api_key = os.environ.get('YOUR_OPENAI_API_KEY')
assistant_model_identifier = 'ft:gpt-3.5-turbo-1106:crown-of-water::8mg0fwHS'

output_path = 'Book of War.json'  # Updated output JSON file
conversation_history = [{"role": "system", "content": "System message goes here."}]  # Add your system message here

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Exiting conversation.")
        break
    conversation_history.append({"role": "user", "content": user_input})
    
    response = query_openai(conversation_history, assistant_model_identifier)
    if response is not None and 'choices' in response:
        assistant_response = response['choices'][0]['message']['content']
        print("Assistant:", assistant_response)
        conversation_history.append({"role": "assistant", "content": assistant_response})
        
        append_to_json(output_path, conversation_history)
    else:
        print("No valid response received.")
        break
```

This script now includes a system message in the conversation history and appends the conversation to `Book of War.json`. Adjust the system message content as needed for your application.

---

no I just want to be able to add a system message into the app. not store it every time. I already have it in the json so I dont need to save anymore as it wont change

---

If you want to include a system message in your application without storing it every time in the JSON file, you can simply add the message to the conversation history within your application logic without appending it to the file. You can display the system message at the beginning of the conversation without saving it to `Book of War.json`. Here's how you can adjust your code to include the system message:

```python
import requests
import json
import os

def query_openai(messages, assistant_model):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": assistant_model,
        "messages": messages,
        "max_tokens": 4096
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", json=data, headers=headers)
    if response.status_code != 200:
        print("Error:", response.status_code, response.text)
        return None
    return response.json()

def append_to_json(output_file_path, conversation_history):
    try:
        with open(output_file_path, 'r') as file:
            existing_conversation = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        existing_conversation = []
    
    existing_conversation.append(conversation_history)

    with open(output_file_path, 'w') as file:
        json.dump(existing_conversation, file, indent=4)

api_key = os.environ.get('YOUR_OPENAI_API_KEY')
assistant_model_identifier = 'ft:gpt-3.5-turbo-1106:crown-of-water::8mg0fwHS'

output_path = 'Book of War.json'

# Display the system message at the start without saving it to the JSON file
print("System Message: System message goes here.")

conversation_history = []

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Exiting conversation.")
        break
    conversation_history.append({"role": "user", "content": user_input})
    
    response = query_openai(conversation_history, assistant_model_identifier)
    if response is not None and 'choices' in response:
        assistant_response = response['choices'][0]['message']['content']
        print("Assistant:", assistant_response)
        conversation_history.append({"role": "assistant", "content": assistant_response})
        
        # Save each interaction to the JSON file except the system message
        append_to_json(output_path, conversation_history)
    else:
        print("No valid response received.")
        break
```

In this updated code, the system message is displayed once at the beginning of the conversation using `print` and is not added to `conversation_history`, so it won't be stored in your JSON file.

---

will this send the system message with the query?

---

No, the updated code snippet I provided will not send the system message with the query to OpenAI's API. The system message is only displayed locally in the console and is not included in the `conversation_history` that gets sent to the API. The system message is effectively just a print statement in the script, separate from the conversation logic that interacts with the API.

If you want the system message to be part of the interaction that gets sent to the API (which could influence the responses based on the context provided by the system message), you need to include it in the `conversation_history` before making the API call. Here's how you can modify the code to include the system message in the API query:

```python
import requests
import json
import os

def query_openai(messages, assistant_model):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": assistant_model,
        "messages": messages,
        "max_tokens": 4096
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", json=data, headers=headers)
    if response.status_code != 200:
        print("Error:", response.status_code, response.text)
        return None
    return response.json()

api_key = os.environ.get('YOUR_OPENAI_API_KEY')
assistant_model_identifier = 'ft:gpt-3.5-turbo-1106:crown-of-water::8mg0fwHS'

# Start the conversation history with the system message
conversation_history = [{"role": "system", "content": "System message goes here."}]

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Exiting conversation.")
        break
    conversation_history.append({"role": "user", "content": user_input})
    
    response = query_openai(conversation_history, assistant_model_identifier)
    if response is not None and 'choices' in response:
        assistant_response = response['choices'][0]['message']['content']
        print("Assistant:", assistant_response)
        conversation_history.append({"role": "assistant", "content": assistant_response})
    else:
        print("No valid response received.")
        break
```

With this setup, the system message is part of the initial `conversation_history` and will influence the context of the conversation as understood by the AI model. However, remember that any changes you make to the `conversation_history` will affect how the AI generates its responses, as it uses the provided conversation history to understand the context of the interaction.

---

what Im looking for is to initialize the app and the system message goes in when the app initializes. then when i have that conversation its using the system message until close the session. It will save on tokens

---

To initialize your application with a system message that influences the conversation context throughout the session without consuming extra tokens on repeated submissions, you can include the system message at the start of the `conversation_history`. This way, the system message is set when the application initializes and remains part of the conversation context for every query within the session. However, it's crucial to note that the system message will be counted towards the token limit in the initial query only, not in subsequent queries.

Here's how you can adjust your script to achieve this:

```python
import requests
import json
import os

def query_openai(messages, assistant_model):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": assistant_model,
        "messages": messages,
        "max_tokens": 4096
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", json=data, headers=headers)
    if response.status_code != 200:
        print("Error:", response.status_code, response.text)
        return None
    return response.json()

api_key = os.environ.get('YOUR_OPENAI_API_KEY')
assistant_model_identifier = 'ft:gpt-3.5-turbo-1106:crown-of-water::8mg0fwHS'

# Initialize conversation history with the system message
conversation_history = [{"role": "system", "content": "System message goes here."}]

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        print("Exiting conversation.")
        break
    conversation_history.append({"role": "user", "content": user_input})
    
    response = query_openai(conversation_history, assistant_model_identifier)
    if response is not None and 'choices' in response:
        assistant_response = response['choices'][0]['message']['content']
        print("Assistant:", assistant_response)
        conversation_history.append({"role": "assistant", "content": assistant_response})
    else:
        print("No valid response received.")
        break
```

In this script, the system message is included from the start and influences the entire conversation. It's sent to the API only once per session, during the initial query, so it won't consume extra tokens with each subsequent user query. The conversation context maintained includes this system message for the session's duration, providing consistency and relevance based on the initialized context.

---

Okay it would be really cool if it saved the first instance of the system message to the file as well. Then when the app closes it can end that conversation. that way each new conversation will have an initial system message saved and an endpoint. Just in case I change the system message here and there

---

To achieve the functionality you're describing, we need to make a few adjustments to your script. The goal is to save the initial system message to the `Book of War.json` file at the start of each conversation and then mark the end of the conversation when the application closes. Here's how you can modify your script:

1. Save the initial system message to the JSON file when the app starts.
2. Append a closing message or marker to the conversation history and save it to the JSON file when the application closes.

Here's the updated script:

```python
import requests
import json
import os

def query_openai(messages, assistant_model):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": assistant_model,
        "messages": messages,
        "max_tokens": 4096
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", json=data, headers=headers)
    if response.status_code != 200:
        print("Error:", response.status_code, response.text)
        return None
    return response.json()

def append_to_json(output_file_path, data):
    try:
        with open(output_file_path, 'r+') as file:
            existing_data = json.load(file)
            existing_data.append(data)
            file.seek(0)
            json.dump(existing_data, file, indent=4)
    except (FileNotFoundError, json.JSONDecodeError):
        with open(output_file_path, 'w') as file:
            json.dump([data], file, indent=4)

api_key = os.environ.get('YOUR_OPENAI_API_KEY')
assistant_model_identifier = 'ft:gpt-3.5-turbo-1106:crown-of-water::8mg0fwHS'

output_path = 'Book of War.json'

# Initialize conversation history with the system message
system_message = {"role": "system", "content": "System message goes here."}
conversation_history = [system_message]

# Save the initial system message to the JSON file
append_to_json(output_path, system_message)

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        # Mark the end of the conversation
        end_message = {"role": "system", "content": "End of conversation."}
        conversation_history.append(end_message)
        # Save the end message to the JSON file
        append_to_json(output_path, conversation_history)
        print("Exiting conversation.")
        break
    conversation_history.append({"role": "user", "content": user_input})
    
    response = query_openai(conversation_history, assistant_model_identifier)
    if response is not None and 'choices' in response:
        assistant_response = response['choices'][0]['message']['content']
        print("Assistant:", assistant_response)
        conversation_history.append({"role": "assistant", "content": assistant_response})
    else:
        print("No valid response received.")
```

With these changes, each new conversation will begin with a system message that is saved to the file. When the conversation ends, a closing message is added and saved, marking the end of that particular conversation in the JSON file. This way, you can track when conversations start and end, even if the system message changes over time.

---

this isnt appending the question or response

---

I see the issue. The `append_to_json` function is designed to append an entire conversation history at once, which is not suitable for appending individual messages as the conversation progresses. We need to modify this function so that it appends each user and assistant message to the existing conversation in the JSON file.

Here's how you can adjust the script to append each message to the JSON file correctly:

1. Modify the `append_to_json` function to read the existing file, update the last conversation with the new message, and then save the file.
2. Ensure that each message (user, assistant, system) is appended correctly during the conversation.

Here's the updated code:

```python
import requests
import json
import os

def query_openai(messages, assistant_model):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": assistant_model,
        "messages": messages,
        "max_tokens": 4096
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", json=data, headers=headers)
    if response.status_code != 200:
        print("Error:", response.status_code, response.text)
        return None
    return response.json()

def append_to_json(output_file_path, message):
    try:
        with open(output_file_path, 'r+') as file:
            existing_data = json.load(file)
            if not existing_data:  # If the file is empty, create a new list
                existing_data = []
            # Assuming the last list item is the current conversation
            if isinstance(existing_data[-1], list):
                existing_data[-1].append(message)
            else:
                existing_data.append([message])  # Start a new conversation if the last item is not a list
            file.seek(0)
            file.truncate()
            json.dump(existing_data, file, indent=4)
    except (FileNotFoundError, json.JSONDecodeError):
        with open(output_file_path, 'w') as file:
            json.dump([[message]], file, indent=4)  # Start a new file with a new conversation

api_key = os.environ.get('YOUR_OPENAI_API_KEY')
assistant_model_identifier = 'ft:gpt-3.5-turbo-1106:crown-of-water::8mg0fwHS'

output_path = 'Book of War.json'

# Initialize and save the system message
system_message = {"role": "system", "content": "System message goes here."}
append_to_json(output_path, system_message)

conversation_history = [system_message]

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        # Mark the end of the conversation and save it
        end_message = {"role": "system", "content": "End of conversation."}
        append_to_json(output_path, end_message)
        print("Exiting conversation.")
        break
    user_message = {"role": "user", "content": user_input}
    conversation_history.append(user_message)
    append_to_json(output_path, user_message)
    
    response = query_openai(conversation_history, assistant_model_identifier)
    if response is not None and 'choices' in response:
        assistant_response = response['choices'][0]['message']['content']
        print("Assistant:", assistant_response)
        assistant_message = {"role": "assistant", "content": assistant_response}
        conversation_history.append(assistant_message)
        append_to_json(output_path, assistant_message)
    else:
        print("No valid response received.")
```

With this updated script, each message (system, user, and assistant) is appended to the current conversation in the JSON file as the conversation progresses. When you start a new session, a new conversation array is created in the JSON file.