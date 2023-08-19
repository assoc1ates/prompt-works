import openai
import openai_async

async def generate_completion(prompt, model_name="gpt-3.5-turbo", max_tokens=256, temperature=0.9):
    model_to_use = "gpt-4" if model_name == "gpt-3.5-turbo" else model_name
    response = await openai_async.chat_complete(
        openai.api_key,
        timeout=60,
        payload={
            "model": model_to_use,
            "messages": [
                {"role": "system", "content": "You are a helpful assistant and great at guessing what files may have info based on loose summaries of the files."},
                {"role": "user", "content": prompt},
            ]
        }
    )
    json_response = response.json()
    llm_content = json_response['choices'][0]['message']['content']

    return llm_content
