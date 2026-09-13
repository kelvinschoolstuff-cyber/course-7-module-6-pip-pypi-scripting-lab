from datetime import datetime
import requests

def generate_log(data):
    """Write log entries to a date-stamped text file and return its name."""
    if not isinstance(data, list):
        raise ValueError("data must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}")
    return filename


def fetch_data():
    """Fetch one post from the JSONPlaceholder public API."""
    response = requests.get(
        "https://jsonplaceholder.typicode.com/posts/1",
        timeout=10,
    )
    if response.status_code == 200:
        return response.json()
    return {}


if __name__ == "__main__":
    post = fetch_data()
    title = post.get("title", "No title found")
    generate_log([f"Fetched post title: {title}"])
    print("Fetched Post Title:", title)
