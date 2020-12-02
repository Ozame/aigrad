from dataclasses import dataclass, fields
from os import sep
from typing import List
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


def load_papers(path: str = "../gradu/material/final_results.xlsx") -> List[Paper]:
    """Loads the papers and returns their relevant information as list of Papers"""
    number_col = "A"
    name_col = "B"
    keywords_col = "M"
    w_classes_col = "N"
    papers = []

    def parse_words(s: str):
        words = s.split(sep=",")
        return list(map(lambda x: x.lower().strip(), words))

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
        if 4 < count:
            result_cell.font = Font(bold=True)

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
    count_keywords()


if __name__ == "__main__":
    main()
