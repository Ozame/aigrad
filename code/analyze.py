import pprint
import sys
from collections import OrderedDict
from dataclasses import dataclass, field, fields
from functools import reduce
from os import sep
from sys import argv
from typing import Dict, List

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


def parse_cat_numbers(s):
    if type(s) == int:
        return [s]
    cats = filter(lambda x: len(x.strip()), s.split(sep=","))
    return list(map(int, cats))


def parse_words(s: str):
    words = s.split(sep=",")
    return list(
        filter(
            lambda x: 1 < len(x),
            map(lambda x: x.lower().strip().replace("(", "").replace(")", ""), words),
        )
    )


def load_papers(path: str = "../gradu/material/final_results.xlsx") -> List[Paper]:
    """Loads the papers and returns their relevant information as list of Papers"""
    number_col = "A"
    name_col = "B"
    keywords_col = "M"
    w_classes_col = "N"
    papers = []

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


def write_category_dist_to_workbook(
    c_dist: Dict[str, int], path: str = "../gradu/material/final_results.xlsx"
):
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


def calculate_category_count(
    path: str = "../gradu/material/final_results.xlsx",
) -> Dict[int, int]:
    """Calculates the number of papers in each category"""
    number_col = "A"
    name_col = "B"
    keywords_col = "M"
    w_classes_col = "N"
    category_column = "P"
    dist = dict([(x, 0) for x in range(1, 27)])

    wb = load_workbook(path)
    sheet = wb["Accepted Papers"]
    for i in range(3, 95):
        row = str(i)
        cat_string = sheet[category_column + row].value
        cats = parse_cat_numbers(cat_string)
        for cat in cats:
            dist[cat] += 1

    sorted_dist = OrderedDict(sorted(dist.items(), key=lambda x: x[1], reverse=True))
    return sorted_dist


def get_category_papers(
    cat_numbers: List[int],
    path: str = "../gradu/material/final_results.xlsx",
) -> Dict[int, int]:
    """Returns the list of papers in given category"""
    number_col = "A"
    name_col = "B"
    keywords_col = "M"
    w_classes_col = "N"
    category_column = "P"
    papers = []

    if not cat_numbers:
        return None

    wb = load_workbook(path)
    sheet = wb["Accepted Papers"]
    for i in range(3, 95):
        row = str(i)
        cat_string = sheet[category_column + row].value
        cats = parse_cat_numbers(cat_string)
        match_counter = 0
        for number in cat_numbers:
            if number in cats:
                match_counter += 1
        if match_counter == len(cat_numbers):
            papers.append(
                Paper(
                    number=sheet[number_col + row].value,
                    name=sheet[name_col + row].value,
                    keywords=parse_words(sheet[keywords_col + row].value),
                    w_classes=parse_words(sheet[w_classes_col + row].value),
                    categories=list((map(str, cats))),
                )
            )

    sorted_list = sorted(papers, key=lambda x: x.number, reverse=True)
    return sorted_list


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


def finalize_categories(path: str = "../gradu/material/final_results.xlsx"):
    """Updates the category numbers and writes them to the workbook"""
    mapping = {
        1: 1,
        8: 2,
        15: 3,
        13: 4,
        17: 5,
        23: 6,
        3: 7,
        22: 8,
        9: 9,
        20: 10,
        24: 11,
        26: 12,
        4: 13,
        6: 14,
        16: 15,
        5: 16,
        2: 17,
        14: 18,
        7: 19,
        10: 20,
        11: 21,
        18: 22,
    }

    old_cats_column = "P"
    new_cats_column = "Q"

    wb = load_workbook(path)
    sheet = wb["Accepted Papers"]
    for i in range(3, 95):
        row = str(i)
        cat_string = sheet[old_cats_column + row].value
        cats = parse_cat_numbers(cat_string)
        new_cats = (str(mapping[x]) for x in cats)
        new_cats_str = ", ".join(new_cats)
        sheet[new_cats_column + row] = new_cats_str
    wb.save(path)


def main():
    # Initial keyword extraction is done and written to workbook
    # papers = load_papers()
    # all_keywords = []
    # for p in papers:
    #     all_keywords += p.keywords
    # fdist = FreqDist(all_keywords)
    # write_freq_dist_to_workbook(fdist)

    # Counts the similar keyword instances on a row and writes it to workbook
    # count_keywords()

    # Category distribution is written to the workbook
    # c_dist = calculate_category_distribution()
    # write_category_dist_to_workbook(c_dist)

    # Amount of articles in categories is printed
    # cat_count = calculate_category_count()
    # print(cat_count)

    # Shows the papers that are included in given categories
    # cat_numbers = sys.argv[1:] if 1 < len(sys.argv) else []
    # cat_numbers = list(map(int, cat_numbers))
    # papers = get_category_papers(cat_numbers)
    # pp = pprint.PrettyPrinter()
    # pp.pprint(papers)

    # Updates category numbers and writes them into workbook
    # finalize_categories()
    pass


if __name__ == "__main__":
    main()
