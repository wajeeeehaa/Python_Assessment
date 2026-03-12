import json


def save_to_json(data, filename="news_data.json"):
    """Saves processed data into a JSON file."""
    try:
        # Convert objects to dictionaries
        json_data = []
        for article in data:
            json_data.append(
                {
                    "title": article.title,
                    "author": article.author,
                    "source": article.source,
                    "url": article.url,
                    "publishedAt": str(article.publishedAt),
                    "description": article.description,
                    "category": getattr(article, "category", ""),
                    "importance_score": getattr(article, "importance_score", 0),
                }
            )

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=4)
        print(f"Data successfully saved to {filename}")
    except Exception as e:
        print(f"Error saving to JSON: {e}")
