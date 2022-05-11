import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/Parenting'


def get_citations_needed_count(url):
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  results = soup.find_all(href="/wiki/Wikipedia:Citation_needed")
  print(len(results))
  return

def get_citations_needed_report(url):
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  results = soup.find_all(href="/wiki/Wikipedia:Citation_needed")
  report = ''
  for result in results:
    report += result.parent.parent.parent.text + '\n'
  print(report)
  return report

get_citations_needed_count(url)
get_citations_needed_report(url)


# url2 = 'https://en.wikipedia.org/wiki/Mindset#Fixed_and_growth_mindset'
# url3 = 'https://en.wikipedia.org/wiki/Laughter'
