import os
import time
import json
import requests
from abc import ABC, abstractmethod
from datetime import datetime

class BaseScraper(ABC):
    def __init__(self, output_dir: str = "data/raw", delay: float = 1.0):
        self.output_dir = output_dir
        self.delay = delay
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
        })
        os.makedirs(self.output_dir, exist_ok=True)

    def fetch_page(self, url: str) -> str:
        """Fetch URL with rate-limiting delay and safety error handling."""
        time.sleep(self.delay)
        try:
            response = self.session.get(url, timeout=15)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching {url}: {e}")
            return ""

    @abstractmethod
    def scrape(self, limit: int = 50) -> list:
        """Perform scraping logic. To be implemented by sub-classes."""
        pass

    def save_corpus(self, data: list, filename: str):
        """Save scraped results with the mandatory metadata header."""
        path = os.path.join(self.output_dir, filename)
        
        metadata = {
            "produced_by": self.__class__.__name__,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "reviewed_by": "pending",
            "stage": "Phase 2 — Data Engineering",
            "commit": "pending"
        }
        
        output = {
            "metadata": metadata,
            "data": data
        }
        
        with open(path, "w", encoding="utf-8") as f:
            json.dump(output, f, indent=2, ensure_ascii=False)
            
        print(f"Saved {len(data)} citations to {path}")
        return path
