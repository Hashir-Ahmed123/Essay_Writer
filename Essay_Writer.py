import requests
from bs4 import BeautifulSoup

def fetch_wikipedia_content(topic):
    wikipedia_url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
    response = requests.get(wikipedia_url)
    soup = BeautifulSoup(response.content, "html.parser")
    paragraphs = soup.find_all("p")
    essay = "\n\n".join([p.get_text() for p in paragraphs])

    return essay

def write_essay_from_wikipedia():
    try:
        topic = input("Enter the topic for the essay: ")
        essay_content = fetch_wikipedia_content(topic)
        if essay_content:                   
            file_name = input("Enter the name of the txt file to save the essay in (without extension): ")
            with open(f"{file_name}.txt", "w") as file:
                file.write(essay_content)
            print(f"An essay on {topic} has been written and saved as {file_name}.txt")
        else:
            print(f"Unable to retrieve content for {topic}. Please check the topic or try another one.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")                    
  
write_essay_from_wikipedia()
