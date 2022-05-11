# Web scraper
## Wikipedia citations needed

Uses 'requests' and 'bs4.BeautifulSoup' libraries to identify statements that have a 'citation needed' tag on a wikipedia page.

The 'get_citations_needed_count' function
takes in a url string and returns an integer corresponding to the number of 'citation needed' tags on the page.

The 'get_citations_needed_report' function
takes in a url string and returns a report string containing each of the paragraphs with a 'citation needed' tag.
