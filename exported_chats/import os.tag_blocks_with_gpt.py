import os
import openai
import re
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_blocks(content):
    return [b.strip() for b in re.split(r"\n\s*---\s*\n", content) if b.strip()]

def call_gpt_on_block(text):
    prompt = f"""You are organizing a theological knowledge archive. For the block below, return:
- primary_topic: main concept
- tags: list of keywords (max 5)
- tone: choose one of [inquiry, reflection, teaching, prophecy, historical]
- summary: a one-sentence summary

Text Block:
{text}

Respond only in JSON."""
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
    )
    return json.loads(response['choices'][0]['message']['content'])

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()
    blocks = extract_blocks(text)
    results = []
    for i, block in enumerate(blocks):
        print(f"🔍 {os.path.basename(filepath)} - block {i+1}/{len(blocks)}")
        try:
            result = call_gpt_on_block(block)
            results.append({
                "block": block,
                **result
            })
        except Exception as e:
            print(f"⚠️ Block {i+1} error: {e}")
    return results

def run(folder="./exported_chats"):
    tagged = {}
    for file in os.listdir(folder):
        if file.endswith(".md"):
            filepath = os.path.join(folder, file)
            try:
                tagged[file] = process_file(filepath)
            except Exception as e:
                print(f"❌ Error processing {file}: {e}")
    with open("tagged_blocks.json", "w", encoding="utf-8") as f:
        json.dump(tagged, f, indent=2)

if __name__ == "__main__":
    run()