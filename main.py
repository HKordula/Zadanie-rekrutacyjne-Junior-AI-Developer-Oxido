import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def read_article(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def save_html(text, filename = "artykul.html"):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

def create_html(text):
    prompt = (
        "Generate high-quality, well-structured HTML code for the given article content. Follow these specific guidelines:\n"
        "- Use appropriate HTML tags for content structure, such as <h1>, <h2>, and <p> to ensure logical formatting.\n"
        "- Identify up to 3 appropriate places within the content for images and use <figure> and <figcaption> tags.\n"
        "- For each identified image location, include <img src=\"image_placeholder.jpg\" alt=\"a specific, detailed prompt describing the image in Polish\" />.\n"
        "- Ensure each alt attribute is detailed and contextually relevant to the section where the image is placed.\n"
        "- Include a <figcaption> element directly under each <img> tag with an appropriate caption that relates to the image content.\n"
        "- Maintain the integrity of the original article text without modifications.\n"
        "- Do not use or include any CSS or JavaScript code. The output should only contain raw HTML.\n"
        "- Exclude <html>, <head>, and <body> tags from the output. Only generate the code meant to be placed within the <body> tags.\n"
        "- Ensure the final HTML code is properly indented, readable, and conforms to HTML5 standards.\n"
        "Ensure all guidelines are followed strictly, and no essential detail is overlooked."
    )

    full_prompt = prompt + "\n" + text

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages = [
            {
                "role": "user",
                "content": full_prompt
            }
        ],
        max_tokens = 1300,
        temperature = 0.1,
        top_p=1.0,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].message.content

article = read_article("tekst.txt")

html_code = create_html(article)

save_html(html_code)