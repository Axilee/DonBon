

import openai
openai.api_key = "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"
prompt="Hello, ChatGPT! Can you generate a response for this message?"
async def chatgpt(prompt):
    

    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.3,
    )

    print(response.choices[0])
    return response.choices[0].text.strip()

