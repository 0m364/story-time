import openai

def get_api_key():
    api_key = input("Enter your OpenAI API key: ")
    return api_key

def get_story_type():
    story_types = ["children", "fantasy", "adventure", "sci-fi", "mystery"]
    story_type = input("What kind of story would you like to hear? ")
    while story_type not in story_types:
        print("Please select a valid story type.")
        story_type = input("What kind of story would you like to hear? ")
    return story_type

def generate_story(story_type):
    prompt = "Write a {} story.".format(story_type)
    response = openai.Completion.create(
        model="gpt-3.5-turbo", prompt=prompt, temperature=0.7, max_tokens=1000
    )
    return response["choices"][0]["text"]

def main():
    api_key = get_api_key()
    openai.api_key = api_key   # Add this line to set your OpenAI API key.
    story_type = get_story_type()
    story = generate_story(story_type)
    print(story)

if __name__ == "__main__":
    main()
