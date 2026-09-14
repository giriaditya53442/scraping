import requests
from bs4 import BeautifulSoup
import logging


# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="scraping.log",
    filemode="a"
)


url = "https://example.com"

logging.info("Scraping started")
logging.info(f"URL: {url}")


try:

    # Request website
    response = requests.get(
        url,
        timeout=10
    )

    response.raise_for_status()

    logging.info("Website accessed successfully")


    # BeautifulSoup
    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    logging.info("HTML parsed successfully")


    # Find paragraphs
    paragraphs = soup.find_all("p")

    logging.info(
        f"Total paragraphs found: {len(paragraphs)}"
    )


    # Extract text
    data = []

    for paragraph in paragraphs:

        text = paragraph.get_text(
            strip=True
        )

        if text:

            data.append(text)

            logging.info(
                "Text extracted successfully"
            )


    # Print scraped data
    for text in data:
        print(text)


    logging.info(
        f"Total text extracted: {len(data)}"
    )

    logging.info("Scraping completed successfully")


except requests.exceptions.RequestException as e:

    logging.error(
        f"Website request failed: {e}"
    )


except Exception as e:

    logging.exception(
        f"Unexpected error: {e}"
    )