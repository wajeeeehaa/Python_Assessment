from api import fetch_news
from processors import get_source_summary, recent_articles_generator, process_articles
from utils import save_to_json


def main():
    print("Fetching news data...")
    data = fetch_news()

    if not data:
        print("Failed to fetch news data.")
        return

    print("\nProcessing articles...")
    processed_articles = process_articles(data)

    if not processed_articles:
        print("No articles with authors found after processing.")
        return

    while True:
        try:
            num = input("\nHow many articles would you like to display? ")
            num_articles = int(num)
            if num_articles <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    num_to_display = min(num_articles, len(processed_articles))

    print("\nTop News Articles")
    print("-----------------")
    for i, article in enumerate(processed_articles[:num_to_display], 1):
        attrs = ["Title", "Author", "Source", "URL"]
        vals = [article.title, article.author, article.source, article.url]

        for attr, val in zip(attrs, vals):
            if attr == "Title":
                print(f"\n{i}. {val}")
            else:
                print(f"   {val}")

    #  Source Summary
    # for better visualization 
    print("\n" )
    print("Source Summary")
    print("\n")
    summary = get_source_summary(processed_articles)

    print("Sources monitored (keys):", list(summary.keys()))
    print("Article counts (values):", list(summary.values()))
    print("\nDetailed breakdown (items):")
    for source, count in summary.items():
        print(f"{source}: {count}")

    #  Generator Function
    print("\n")
    print("Recent Articles Generator")
    for recent in recent_articles_generator(processed_articles):
        print(f"- {recent.title}")

    # bonus task
    print("\n")
    save_to_json(processed_articles)


if __name__ == "__main__":
    main()
