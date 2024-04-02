import requests
from bs4 import BeautifulSoup

def fetch_wikipedia_content(topic):
    # Define the Wikipedia URL for the given topic
    wikipedia_url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"

    # Send an HTTP request to the Wikipedia page
    response = requests.get(wikipedia_url)

    # Parse the HTML content using Beautiful Soup
    soup = BeautifulSoup(response.content, "html.parser")

    # Extract relevant content (e.g., paragraphs) from the page
    paragraphs = soup.find_all("p")

    # Combine the paragraphs into a single essay
    essay = "\n\n".join([p.get_text() for p in paragraphs])

    return essay

def write_essay_from_wikipedia():
    try:
        # Ask user for the topic of the essay
        topic = input("Enter the topic for the essay: ")

        # Fetch content from Wikipedia
        essay_content = fetch_wikipedia_content(topic)
        if essay_content:
            # Ask user for the name of the txt file
            file_name = input("Enter the name of the txt file to save the essay in (without extension): ")

            # Save the essay to the specified file
            with open(f"{file_name}.txt", "w") as file:
                file.write(essay_content)
            print(f"An essay on {topic} has been written and saved as {file_name}.txt")
        else:
            print(f"Unable to retrieve content for {topic}. Please check the topic or try another one.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage: Ask user for a topic and file name, then write the essay
write_essay_from_wikipedia()
