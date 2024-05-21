from openai import OpenAI
import json

api_key = "replace with API key"

# Function to call the ChatGPT API
def generate_article_data(example1, example2, example3, tst):
    prompt = f"""
    Given the following text, generate a headline, URL, and social media post in JSON format. Here are 3 examples

    Example 1:
    Text: "{example1['text']}"

    Output format:
    {{
        "headline": "{example1['headline']}",
        "url": "{example1['url']}",
        "social_media_post": "{example1['social_media_post']}"
    }}

    Example 2:
    Text: "{example2['text']}"

    Output format:
    {{
        "headline": "{example2['headline']}",
        "url": "{example2['url']}",
        "social_media_post": "{example2['social_media_post']}"
    }}
    Example 3:
    Text: "{example3['text']}"

    Output format:
    {{
        "headline": "{example3['headline']}",
        "url": "{example3['url']}",
        "social_media_post": "{example3['social_media_post']}"
    }}

    """

    client = OpenAI(api_key=api_key)
    response_format = { "type": "json_object" }
    completion = client.chat.completions.create(
    model="gpt-4o",
    response_format=response_format,
        messages=[
            {"role": "system", "content": "You are a helpful assistant helping the San Francisco Chronicle create web content that drives SEO but also matches the tone of other articles from the San Francisco Chronicle."},
            {"role": "user", "content": prompt},
            {"role": "user", "content": tst}
        ],
        n=1,
        stop=None,
        temperature=0.7,
    )

    article_data = completion.choices[0].message.content
    return article_data


