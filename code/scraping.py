import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook, Workbook

def get_page(url):
    return requests.get(url).content


def get_paper_info(url):
    """Scrape abstract and keywords from given Springer-Link paper url"""
    results = {}
    if len(url) == 0:
        return None
    page = get_page(url)
    soup = BeautifulSoup(page, features="html.parser")

    section = soup.find(id="Abs1")
    paragraphs = section.find_all("p")
    ps = []
    for p in paragraphs:
        ps.append(p.text)
    abstract = " ".join(ps)

    keyword_elements = soup.find_all('span',class_="Keyword")
    keywords = []
    if len(keyword_elements) != 0:
        for word in keyword_elements:
            try:
                keywords.append(word.string.strip())
            except AttributeError as e:
                continue

        keywords = ", ".join(keywords)

    else:
        keywords = ""

    results['abstract'] = abstract
    results['keywords'] = keywords
    return results

def add_abstracts_and_keywords(path='../gradu/material/ICAGI.xlsx', target="../gradu/material/test.xlsx"):
    """Add info from given articles to material_search file"""
    wb = load_workbook(path)
    ws = wb.active
    wb_new = load_workbook("../gradu/material_search.xlsx")
    wsn = wb_new.active
    number_of_articles_to_be_added = 152
    start_row = 39
    number_col = 1
    title_col = 2
    author_col = 3
    year_col = 4
    venue_col = 5
    abstract_col = 6
    keywords_col = 7
    link_col = 8
    doi_col = 9
    cite_col = 10
    type_col = 11
    access_col = 12
    source_col = 13
    volume_col = 14

    for row in range(start_row, start_row + number_of_articles_to_be_added - 1):
        # TODO: Rows don't match!!! start row etc
        title = ws.cell(row=row, column=1).value
        doi = ws.cell(row=row, column=6).value
        authors = ws.cell(row=row, column=7).value
        year = ws.cell(row=row, column=8).value
        url = ws.cell(row=row, column=9).value

        abstract = get_paper_info(url)['abstract']
        keywords = get_paper_info(url)['keywords']

        wsn.cell(row=row, column=abstract_col).value = abstract
        wsn.cell(row=row, column=keywords_col).value = keywords
        wsn.cell(row=row, column=title_col).value = title
        wsn.cell(row=row, column=doi_col).value = doi
        wsn.cell(row=row, column=author_col).value = authors
        wsn.cell(row=row, column=year_col).value = year

        wsn.cell(row=row, column=type_col).value = "Conference Paper"
        wsn.cell(row=row, column=venue_col).value = "ICAGI"
        wsn.cell(row=row, column=link_col).value = url
        wsn.cell(row=row, column=source_col).value = "Springer-Link"
        
    wb_new.save(target)

if __name__ == "__main__":
    add_abstracts_and_keywords()