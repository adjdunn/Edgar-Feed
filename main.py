import requests
import xml.etree.ElementTree as ET
import re
from utils import get_ticker_symbol, get_first_table_url

# URL of the RSS feed
feed_url = 'https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&CIK=&type=10-Q&company=&dateb=&owner=include&start=0&count=40&output=atom'

# Function to fetch and parse the RSS feed
def fetch_rss_feed(url):
    headers = {
        'User-Agent': 'Your Company Name (your-email@example.com)',
        'Accept-Encoding': 'gzip, deflate',
        'Host': 'www.sec.gov'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f"Failed to fetch RSS feed. Status code: {response.status_code}")

# Function to parse the XML and extract the required information
def parse_feed(xml_data):
    namespaces = {'atom': 'http://www.w3.org/2005/Atom'}
    root = ET.fromstring(xml_data)
    entries = root.findall('atom:entry', namespaces)

    data = []
    for entry in entries:
        title = entry.find('atom:title', namespaces).text
        link = entry.find('atom:link', namespaces).attrib['href']
        report_url = get_first_table_url(link)
        
        # Extract filing type, company name, and CIK number using regex
        match = re.match(r'(.*) - (.*) \((\d+)\) \(Filer\)', title)
        if match:
            filing_type = match.group(1)
            company_name = match.group(2)
            cik_number = match.group(3)
            ticker = get_ticker_symbol(cik_number)
            data.append([filing_type, company_name, ticker, report_url])
    return data

def get_feed():

    # Fetch and parse the RSS feed
    rss_data = fetch_rss_feed(feed_url)
    entries_data = parse_feed(rss_data)

    return entries_data

# Print the extracted data
# for entry in entries_data:
#     print(entry)
