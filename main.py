from scraper import all_data
from ai import analyze_jobs

def main():
    print("Fetching jobs...")
    jobs = all_data()

    print("Sending to AI...")
    result = analyze_jobs(jobs)

    print("\n=== AI OUTPUT ===\n")
    print(result)

if __name__ == "__main__":
    main()