# from openai import OpenAI

from generate_article_data import generate_article_data
from extract_article_data import extract_article_data
import json

# file_path1 = 'data/sfc_article_001.txt'
# file_path2 = 'data/sfc_article_002.txt'
# file_path3 = 'data/sfc_article_003.txt'
# file_path_test = 'data/test_article.txt'
# with open(file_path_test, 'r') as file:
#     lines = file.readlines()

# tst = " ".join(lines)
# example1 = extract_article_data(file_path1)
# example2 = extract_article_data(file_path2)
# example3 = extract_article_data(file_path3)

# output = generate_article_data(example1=example1, example2=example2, example3=example3, tst=tst)
# print(output)


def main():
    file_path1 = 'data/sfc_article_001.txt'
    file_path2 = 'data/sfc_article_002.txt'
    file_path3 = 'data/sfc_article_003.txt'
    example1 = extract_article_data(file_path1)
    example2 = extract_article_data(file_path2)
    example3 = extract_article_data(file_path3)
    print("Welcome to the Article Data Generator!")
    print("You can generate a headline, URL, and social media post by providing the text below the separator.")
    print("Type 'exit' to quit the program.")

    while True:
        text = input("\nEnter the text below:\n")
        if text.lower() == "exit":
            print("Goodbye!")
            break

        if (len(text) > 10): # prevent accidental inputs
            try:
                article_data = generate_article_data(example1=example1, example2=example2, example3=example3,tst=text)
                print("\nGenerated Article Data:")
                print(json.dumps(article_data, indent=2))
            except Exception as e:
                print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()