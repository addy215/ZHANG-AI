import openai

# 替换为你的实际 API 密钥
openai.api_key = "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"  # 在这里替换为你的 OpenAI API 密钥

try:
    # 使用 ChatGPT 模型（例如 gpt-3.5-turbo 或 gpt-4）
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # 使用 GPT-3.5 模型
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello, world!"}
        ]
    )

    # 打印返回的内容
    print("API 密钥有效！返回结果：")
    print(response['choices'][0]['message']['content'].strip())

except Exception as e:
    print(f"Error: {e}")
