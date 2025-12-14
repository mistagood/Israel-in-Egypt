# Extracting Query Response Pairs



---



---

this trsining data failed because it only had one example. i need each set of query and response to create an example.
import os
import json
import PyPDF2

def extract_conversations_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        messages = []
        current_role = None
        current_content = []

        for i in range(num_pages):
            text = reader.pages[i].extract_text()
            lines = [line.strip() for line in text.split('\n') if line.strip()]

            for line in lines:
                if line.startswith('You:') or line.startswith('Assistant:'):
                    if current_content and current_role:
                        messages.append({"role": current_role, "content": " ".join(current_content)})
                    current_role = "user" if line.startswith('You:') else "assistant"
                    current_content = [line.split(':', 1)[1].strip()]
                elif current_role:  # Continue accumulating text under the current role
                    current_content.append(line)

        # Append the last message if it's valid
        if current_content and current_role:
            messages.append({"role": current_role, "content": " ".join(current_content)})

        return messages

# Directory containing your PDFs
pdf_directory = 'pdfs'
all_conversations = []

# Loop through each PDF in the directory
for filename in os.listdir(pdf_directory):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(pdf_directory, filename)
        conversation = extract_conversations_from_pdf(pdf_path)
        if conversation:
            all_conversations.append({"messages": conversation})

# Writing to a JSONL file
with open('formatted_conversations.jsonl', 'w') as file:
    for conversation in all_conversations:
        json_line = json.dumps(conversation)
        file.write(json_line + '\n')


---



---

Your script is well on its way to processing conversations from PDF files and formatting them into a JSONL file. However, to create training data that includes distinct examples of queries and responses, you need to ensure each conversation is split appropriately into separate query-response pairs. Here’s an improved version of your script that does this:

### Updated Script for Extracting Query-Response Pairs from PDFs

```python
import os
import json
import PyPDF2

def extract_conversations_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        # To hold all extracted query-response pairs
        examples = []

        # Tracking conversation context
        current_role = None
        current_content = []
        user_query = None
        assistant_response = None

        for i in range(num_pages):
            text = reader.pages[i].extract_text()
            lines = [line.strip() for line in text.split('\n') if line.strip()]

            for line in lines:
                if line.startswith('You:'):
                    # If we encounter a 'You:' line, it means a new user query has started
                    # Save the previous assistant response as a complete example
                    if user_query and assistant_response:
                        examples.append({"query": user_query, "response": assistant_response})

                    # Start a new user query
                    user_query = line.split(':', 1)[1].strip()
                    assistant_response = None  # Reset assistant response

                elif line.startswith('Assistant:'):
                    # If we encounter an 'Assistant:' line, it means a new assistant response has started
                    # Continue adding to the current assistant response
                    assistant_response = line.split(':', 1)[1].strip()

                elif current_role:  # Accumulate text under the current role
                    if current_role == "user":
                        user_query += " " + line
                    elif current_role == "assistant":
                        assistant_response += " " + line

                # Determine the current role
                if line.startswith('You:'):
                    current_role = "user"
                elif line.startswith('Assistant:'):
                    current_role = "assistant"

        # Append the last example if valid
        if user_query and assistant_response:
            examples.append({"query": user_query, "response": assistant_response})

        return examples

# Directory containing your PDFs
pdf_directory = 'pdfs'
all_examples = []

# Loop through each PDF in the directory
for filename in os.listdir(pdf_directory):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(pdf_directory, filename)
        examples = extract_conversations_from_pdf(pdf_path)
        if examples:
            all_examples.extend(examples)

# Writing to a JSONL file
with open('formatted_conversations.jsonl', 'w') as file:
    for example in all_examples:
        json_line = json.dumps(example)
        file.write(json_line + '\n')
```

### Key Changes Made:
1. **Splitting Conversations into Query-Response Pairs**: The script now creates a new example each time it detects a new user query (`You:`). It saves the last user query and the subsequent assistant response as a new entry.
   
2. **Resetting and Capturing Roles Properly**: The `current_role` is determined by the starting keyword (`You:` or `Assistant:`), and it resets when it switches roles, making it easier to extract the query and response content.

3. **Appending Final Example**: Ensures the last user query and assistant response are appended if they are valid.

4. **Output Format**: The script writes each query-response pair in a JSONL format, suitable for training many machine learning models.

### Instructions:
- **Input PDF Directory**: Ensure the `pdf_directory` variable points to the correct path containing your PDF files.
- **Output File**: The extracted conversations are written to `formatted_conversations.jsonl`.

This script should provide a dataset with individual examples that can be used effectively for training purposes.

---

write to a new json everytime if it already exists

---

To ensure that a new JSON file is created every time the script runs, even if one already exists, we can add a timestamp or a unique identifier to the filename. This approach avoids overwriting previous outputs and keeps track of different runs.

Here's an updated version of your script that incorporates this feature:

### Updated Script to Write to a New JSON File Every Time

```python
import os
import json
import PyPDF2
from datetime import datetime

def extract_conversations_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        # To hold all extracted query-response pairs
        examples = []

        # Tracking conversation context
        current_role = None
        current_content = []
        user_query = None
        assistant_response = None

        for i in range(num_pages):
            text = reader.pages[i].extract_text()
            lines = [line.strip() for line in text.split('\n') if line.strip()]

            for line in lines:
                if line.startswith('You:'):
                    # If we encounter a 'You:' line, it means a new user query has started
                    # Save the previous assistant response as a complete example
                    if user_query and assistant_response:
                        examples.append({"query": user_query, "response": assistant_response})

                    # Start a new user query
                    user_query = line.split(':', 1)[1].strip()
                    assistant_response = None  # Reset assistant response

                elif line.startswith('Assistant:'):
                    # If we encounter an 'Assistant:' line, it means a new assistant response has started
                    # Continue adding to the current assistant response
                    assistant_response = line.split(':', 1)[1].strip()

                elif current_role:  # Accumulate text under the current role
                    if current_role == "user":
                        user_query += " " + line
                    elif current_role == "assistant":
                        assistant_response += " " + line

                # Determine the current role
                if line.startswith('You:'):
                    current_role = "user"
                elif line.startswith('Assistant:'):
                    current_role = "assistant"

        # Append the last example if valid
        if user_query and assistant_response:
            examples.append({"query": user_query, "response": assistant_response})

        return examples

# Directory containing your PDFs
pdf_directory = 'pdfs'
all_examples = []

# Loop through each PDF in the directory
for filename in os.listdir(pdf_directory):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(pdf_directory, filename)
        examples = extract_conversations_from_pdf(pdf_path)
        if examples:
            all_examples.extend(examples)

# Create a unique filename with timestamp
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
output_filename = f'formatted_conversations_{timestamp}.jsonl'

# Writing to a new JSONL file
with open(output_filename, 'w') as file:
    for example in all_examples:
        json_line = json.dumps(example)
        file.write(json_line + '\n')

print(f"Conversations have been written to {output_filename}")
```

### Key Changes Made:
1. **Unique Output Filename**: The output filename is generated using the current timestamp (formatted as `YYYYMMDD_HHMMSS`). This ensures every output file is unique and prevents overwriting previous files.
   
2. **Informing the User of Output**: Added a `print` statement at the end to confirm the file creation and its name.

### Usage Instructions:
- **Input PDF Directory**: Ensure the `pdf_directory` variable points to the correct directory containing your PDF files.
- **Output File**: The script will create a new JSONL file each time it runs, named with a timestamp to ensure uniqueness. 

By running this updated script, you can keep a chronological record of all extracted conversations, which is helpful for version control and analyzing different runs.

---

The job failed due to an invalid training file. Unexpected file format, expected either prompt/completion pairs or chat messages.

---

To ensure that your training file format meets the expected standards, you need to provide either prompt-completion pairs (for text-based models) or chat messages (for chat-based models) in a properly formatted JSONL file. Here’s how you can structure your JSONL file correctly for both types:

### 1. Format for Prompt/Completion Pairs

For prompt-completion training, each line of the JSONL file should have a `prompt` and a `completion` field. For example:

```jsonl
{"prompt": "You: How do I reset my password?\n", "completion": "Assistant: To reset your password, go to the settings page and click on 'Reset Password'. Follow the instructions sent to your email."}
{"prompt": "You: What is the capital of France?\n", "completion": "Assistant: The capital of France is Paris."}
```

### 2. Format for Chat Messages

For chat-based training, each line in the JSONL file should contain a `messages` field, which includes an array of objects with `role` (either `user` or `assistant`) and `content` fields. For example:

```jsonl
{"messages": [{"role": "user", "content": "How do I reset my password?"}, {"role": "assistant", "content": "To reset your password, go to the settings page and click on 'Reset Password'. Follow the instructions sent to your email."}]}
{"messages": [{"role": "user", "content": "What is the capital of France?"}, {"role": "assistant", "content": "The capital of France is Paris."}]}
```

### Updated Script to Generate Properly Formatted Training Data

Below is an updated version of your script that writes the extracted conversations in the correct format for chat-based training data. Each conversation will be formatted as a chat message with the `messages` field:

```python
import os
import json
import PyPDF2
from datetime import datetime

def extract_conversations_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        # To hold all extracted chat messages
        chat_messages = []
        conversation = []

        # Tracking conversation context
        current_role = None
        current_content = []

        for i in range(num_pages):
            text = reader.pages[i].extract_text()
            lines = [line.strip() for line in text.split('\n') if line.strip()]

            for line in lines:
                if line.startswith('You:'):
                    # If there is ongoing conversation, append to chat_messages
                    if conversation:
                        chat_messages.append({"messages": conversation})
                    # Start a new conversation
                    conversation = []
                    user_message = line.split(':', 1)[1].strip()
                    conversation.append({"role": "user", "content": user_message})
                elif line.startswith('Assistant:'):
                    assistant_message = line.split(':', 1)[1].strip()
                    conversation.append({"role": "assistant", "content": assistant_message})
                else:
                    if conversation:
                        # Add continuation of current role's content
                        if conversation[-1]['role'] == 'user':
                            conversation[-1]['content'] += ' ' + line
                        elif conversation[-1]['role'] == 'assistant':
                            conversation[-1]['content'] += ' ' + line
        
        # Append the last conversation if valid
        if conversation:
            chat_messages.append({"messages": conversation})

        return chat_messages

# Directory containing your PDFs
pdf_directory = 'pdfs'
all_conversations = []

# Loop through each PDF in the directory
for filename in os.listdir(pdf_directory):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(pdf_directory, filename)
        conversations = extract_conversations_from_pdf(pdf_path)
        if conversations:
            all_conversations.extend(conversations)

# Create a unique filename with timestamp
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
output_filename = f'formatted_conversations_{timestamp}.jsonl'

# Writing to a new JSONL file
with open(output_filename, 'w') as file:
    for conversation in all_conversations:
        json_line = json.dumps(conversation)
        file.write(json_line + '\n')

print(f"Conversations have been written to {output_filename}")
```

### Explanation of the Changes:
1. **Correctly Formats Conversations as Chat Messages**: The script now collects user and assistant messages and formats them in a chat message structure with `role` and `content`.
2. **Handles Line Continuation**: If a message spans multiple lines, the script correctly continues appending content under the same role.
3. **Handles Multiple Conversations**: The script saves each conversation separately in the `messages` field.

### Instructions:
- Make sure your PDF files are correctly placed in the `pdfs` directory.
- Run the script to generate a new JSONL file with properly formatted chat messages for each run.
- Verify that the output file matches the expected format for your training job.

This approach should resolve the "Unexpected file format" error, ensuring the data is formatted correctly for the model training requirements.