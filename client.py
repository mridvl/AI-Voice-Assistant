from openai import OpenAI

#defaulter to getting the key using os.environ.get("OPENAI_API_KEY")
#if you saved the key under a deifferent environment variable nam, you can do something like:
client = OpenAI(
    api_key="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",
)
completion = client.chat.completions.create (
    model = "gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant,skilled in general task like alexa and google cloud."},
        {"role": "user", "content":"Compose a poem that explains the concept of recursion in programming"}
    ]
)
print(completion.choices[0].message.content)