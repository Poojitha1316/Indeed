# Config.py

class Config:
    proxy = "http://dc0950da5da2e980256957106ccdf277fca47202:@proxy.zenrows.com:8001"
    url_template = "https://www.indeed.com/jobs?q={keyword}&sc=0kf%3Ajt%28contract%29%3B&page={page}"
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15"
    ]

    # Output CSV file name
    output_csv = "output12_{keyword}.csv"

    # Keywords for job search
    keywords = ["Data Analyst", "Business Analyst", "System Analyst", "Data Scientists", "Data engineer", "Business System Analyst"]
