

import openai
openai.api_key = "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"
def chatgpt(prompt):
    

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=250,
        n=1,
        stop=">>>",
        temperature=0.5,
    )
    odpowiedz = response.choices[0]
    print(response.choices[0])
    print(__file__)
    # with open(__file__, "a") as p:
    #     p.write(odpowiedz)
    return response.choices[0].text.strip()
chatgpt("jak napisac program w pythonie")