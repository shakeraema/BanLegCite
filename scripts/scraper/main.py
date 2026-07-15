import argparse
import sys
from scripts.scraper.dlr_scraper import DLRScraper
from scripts.scraper.blc_scraper import BLCScraper
from scripts.scraper.alr_scraper import ALRScraper

def main():
    parser = argparse.ArgumentParser(description="Orchestrate citation scraping from Bangladeshi legal portals.")
    parser.add_argument("--source", type=str, default="all", choices=["all", "dlr", "blc", "alr"],
                        help="The reporter source to scrape (default: all)")
    parser.add_argument("--limit", type=int, default=50,
                        help="Maximum number of citations to scrape (default: 50)")
    parser.add_argument("--delay", type=float, default=1.0,
                        help="Delay in seconds between requests (default: 1.0)")
    parser.add_argument("--output-dir", type=str, default="data/raw",
                        help="Directory to save raw citation data (default: data/raw)")
    
    args = parser.parse_args()
    
    scrapers = []
    if args.source in ("all", "dlr"):
        scrapers.append(DLRScraper(output_dir=args.output_dir, delay=args.delay))
    if args.source in ("all", "blc"):
        scrapers.append(BLCScraper(output_dir=args.output_dir, delay=args.delay))
    if args.source in ("all", "alr"):
        scrapers.append(ALRScraper(output_dir=args.output_dir, delay=args.delay))
        
    print(f"Executing scraping pipeline for sources: {args.source} (limit per source: {args.limit})")
    for scraper in scrapers:
        try:
            scraper.scrape(limit=args.limit)
        except Exception as e:
            print(f"Failed running scraper {scraper.__class__.__name__}: {e}")

if __name__ == "__main__":
    main()
