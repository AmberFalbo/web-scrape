import requests
from bs4 import BeautifulSoup

assert requests
assert BeautifulSoup


url = "https://en.wikipedia.org/wiki/History_of_Mexico"

def get_soup(url):
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    return soup


def get_citations_needed_count(url):
    soup = get_soup(url)
    results = soup.find_all('a',title='Wikipedia:Citation needed')
    count_of_citations = len(results)
    print("Citations needed: ", count_of_citations)
    return count_of_citations

get_citations_needed_count(url)

    # counter = 0
    # for citations_needed in results:
    #     counter += 1
    # get_citations_needed_report(counter)

counter = get_citations_needed_count('https://en.wikipedia.org/wiki/History_of_Mexico')


def get_citations_needed_report(url):
    surrounding_text = ""
    soup = get_soup(url)
    counter = get_citations_needed_count(url)
    results_counter = f"There are {counter} needed citations for this wiki page"
    results = soup.find_all(class_='noprint Inline-Template Template-Fact')
    # ^^^^ stuggled finding how to parse I adapted from Sian C's for this

    for i in results:
        p = i.find_parent('p')
        surrounding_text += p.text.strip()
        surrounding_text += '\n'*2

    print(surrounding_text, results_counter)
    return surrounding_text

get_citations_needed_report(url)


# print(get_citations_needed_report)        


# if __name__ == "__main__":
#     # get_citations_needed_report(url)
#     print(get_citations_needed_report(url))








