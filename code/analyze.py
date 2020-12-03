from dataclasses import dataclass, field, fields
from os import sep
from typing import Dict, List
import pprint
from functools import reduce
from nltk.probability import FreqDist

from openpyxl import load_workbook
from openpyxl.styles import Font

# Wieringa classes: ER, VR, SP, PP, OP, PEP


@dataclass
class Paper:
    number: int
    name: str
    keywords: List[str]
    w_classes: List[str]
    categories: List[str] = field(default_factory=list)


def load_papers(path: str = "../gradu/material/final_results.xlsx") -> List[Paper]:
    """Loads the papers and returns their relevant information as list of Papers"""
    number_col = "A"
    name_col = "B"
    keywords_col = "M"
    w_classes_col = "N"
    papers = []

    def parse_words(s: str):
        words = s.split(sep=",")
        return list(
            filter(
                lambda x: 1 < len(x),
                map(
                    lambda x: x.lower().strip().replace("(", "").replace(")", ""), words
                ),
            )
        )

    wb = load_workbook(path)
    sheet = wb["Accepted Papers"]
    for i in range(3, 95):
        row = str(i)
        paper = Paper(
            number=sheet[number_col + row].value,
            name=sheet[name_col + row].value,
            keywords=parse_words(sheet[keywords_col + row].value),
            w_classes=parse_words(sheet[w_classes_col + row].value),
        )
        papers.append(paper)
    return papers


def load_categories(
    path: str = "../gradu/material/final_results.xlsx",
) -> Dict[str, str]:
    """
    Loads the categories and their respective keywords

    Returns a dict with keywords as keys and their respective categories as values
    """
    categorization = {}
    wb = load_workbook(path)
    if not "Categorization" in wb:
        return None
    sheet = wb["Categorization"]
    for row in sheet.iter_rows(min_row=3, max_row=297, min_col=2, max_col=15):
        for cell in row:
            if cell.value and "/" in cell.value:
                keyword = cell.value[: cell.value.rfind("/")]
                category = sheet["A" + str(cell.row)].value or None
                categorization[keyword] = category
    return categorization


def count_keywords(path: str = "../gradu/material/final_results.xlsx"):
    """Counts the occurrences of keyword instances on the same row"""
    result_column = "Q"
    results_row = 3

    wb = load_workbook(path)
    sheet = wb["Categorization"]
    for row in sheet.iter_rows(min_row=results_row, max_row=297, min_col=2, max_col=15):
        count = 0

        for cell in row:
            if cell.value and "/" in cell.value:
                count += int(cell.value[cell.value.rfind("/") + 1 :])
            results_row = cell.row
        result_cell = sheet[result_column + str(results_row)]
        result_cell.value = count
        if 4 <= count:
            result_cell.font = Font(bold=True)

    wb.save(path)


def calculate_category_distribution(path: str = "../gradu/material/final_results.xlsx"):
    """Calculates how the articles would be divided based on the current categorization"""
    papers = load_papers()
    categories = load_categories()
    dist = {}
    empty_papers = []
    # Every possible category for paper is fetched
    for paper in papers:
        cats = []
        for kw in paper.keywords:
            cat = categories[kw]
            if cat not in cats:
                cats.append(cat)
            else:
                continue
        # If multiple categories are found, None-category is removed
        if 1 < len(cats) and None in cats:
            cats = [i for i in cats if i]
        # paper's final categories are added to the distribution
        # Notice that paper.categories is not assigned as it is unnecessary
        if len(cats) == 1 and None in cats:
            empty_papers.append(paper)
        for cat in cats:
            if cat in dist:
                dist[cat] += 1
            else:
                dist[cat] = 1

    pp = pprint.PrettyPrinter()
    c = sum(dist.values())
    print("Total categorizations: " + str(c))
    pp.pprint(dist)
    print("The following are papers with no categories:")
    pp.pprint(empty_papers)
    return dist

def write_category_dist_to_workbook(c_dist: Dict[str, int],  path: str = "../gradu/material/final_results.xlsx"):
    """Writes the given category distribution to the worksheet"""

    row_number = 6
    category_name_column = "T"
    category_count_column = "U"

    wb = load_workbook(path)
    if not "Categorization" in wb:
        return
    sheet = wb["Categorization"]
    for name, count in sorted(c_dist.items(), key=lambda x: x[1], reverse=True):
        sheet[category_name_column + str(row_number)] = name
        sheet[category_count_column + str(row_number)] = count
        row_number += 2

    wb.save(path)


def write_freq_dist_to_workbook(
    f_dist: FreqDist, path: str = "../gradu/material/final_results.xlsx"
):
    """Writes the frequency distribution of keywords on the the worksheet"""
    data_column = "B"
    data_row = 3
    wb = load_workbook(path)
    if not "Keywords" in wb:
        wb.create_sheet(title="Keywords", index=2)
    sheet = wb["Keywords"]
    for word, count in sorted(f_dist.items(), key=lambda x: x[1], reverse=True):
        sheet[data_column + str(data_row)] = f"{word}/{count}"
        data_row += 1
    wb.save(path)



def main():
    # papers = load_papers()
    # all_keywords = []
    # for p in papers:
    #     all_keywords += p.keywords
    # fdist = FreqDist(all_keywords)
    # write_freq_dist_to_workbook(fdist)

    # count_keywords()

    c_dist = calculate_category_distribution()
    write_category_dist_to_workbook(c_dist)


if __name__ == "__main__":
    main()
