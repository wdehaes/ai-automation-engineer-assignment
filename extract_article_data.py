def extract_article_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    data = {
        "headline": "",
        "url": "",
        "social_media_post": "",
        "text": ""
    }

    separator_found = False
    text = []

    for line in lines:
        if line.startswith("Headline:"):
            data["headline"] = line[len("Headline:"):].strip()
        elif line.startswith("URL:"):
            data["url"] = line[len("URL:"):].strip()
        elif line.startswith("Social media post:"):
            data["social_media_post"] = line[len("Social media post:"):].strip()
        elif line.startswith("---"):
            separator_found = True
        elif separator_found:
            text.append(line.strip())

    data["text"] = " ".join(text)

    return data