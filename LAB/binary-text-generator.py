import openai
from dotenv import dotenv_values

env_vars = dotenv_values('.env')

openai.api_key = env_vars['OPENAI_API_KEY']

def generate_text(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()

def text_to_binary(text):
    binary = ' '.join(format(ord(c), '08b') for c in text)
    return binary

def main():
    prompt = "Once upon a time in a distant land, there was a magical forest where..."
    generated_text = generate_text(prompt)
    print("Generated Text:")
    print(generated_text)

    binary_representation = text_to_binary(generated_text)
    print("\nBinary Text Representation:")
    print(binary_representation)

if __name__ == "__main__":
    main()
