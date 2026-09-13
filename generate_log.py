from lib.generate_log import fetch_data, generate_log


if __name__ == "__main__":
    post = fetch_data()
    title = post.get("title", "No title found")
    generate_log([f"Fetched post title: {title}"])
    print("Fetched Post Title:", title)