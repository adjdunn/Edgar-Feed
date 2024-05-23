import requests
from bs4 import BeautifulSoup

# Function to get company details using CIK
def get_company_details(cik):
    headers = {
        'User-Agent': 'Your Company Name (your-email@example.com)',
        'Accept-Encoding': 'gzip, deflate',
        'Host': 'data.sec.gov'
    }
    url = f'https://data.sec.gov/submissions/CIK{cik}.json'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch company details. Status code: {response.status_code}")

# Function to extract the ticker symbol from the company details
def get_ticker_symbol(cik):
    company_details = get_company_details(cik)
    #return company_details
    ticker = company_details.get('tickers')
    if ticker:
        return ticker[0]
    else:
        return None

# # Example CIK for Apple Inc.
# apple_cik = '0001134982'

# try:
#     ticker = get_ticker_symbol(apple_cik)
#     print(f'Ticker symbol for CIK {apple_cik}: {ticker}')
# except Exception as e:
#     print(str(e))

# Function to fetch the page content
def fetch_page_content(url):
    headers = {
        'User-Agent': 'Your Company Name (your-email@example.com)',
        'Accept-Encoding': 'gzip, deflate',
        'Host': 'www.sec.gov'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch page content. Status code: {response.status_code}")

# Function to parse the page content and extract the first URL from the table
def get_first_table_url(url):
    page_content = fetch_page_content(url)
    soup = BeautifulSoup(page_content, 'html.parser')
    table = soup.find('table', {'class': 'tableFile'})
    if table:
        first_link = table.find('a', href=True)
        if first_link:
            return 'https://www.sec.gov' + first_link['href']
    return url


# Example URL
# example_url = 'https://www.sec.gov/Archives/edgar/data/1852019/000141057824000948/0001410578-24-000948-index.htm'

# try:
#     page_content = fetch_page_content(example_url)
#     first_url = get_first_table_url(page_content)
#     print(f'First URL: {first_url}')
# except Exception as e:
#     print(str(e))