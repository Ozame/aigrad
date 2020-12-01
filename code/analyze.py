from dataclasses import dataclass, fields
from os import sep
from typing import List
from nltk.probability import FreqDist

from openpyxl import load_workbook

# Wieringa classes: ER, VR, SP, PP, OP, PEP


@dataclass
class Paper:
    number: int
    name: str
    keywords: List[str]
    w_classes: List[str]


def load_papers(path: str = "../gradu/material/final_results.xlsx") -> List[Paper]:
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


def write_freq_dist_to_workbook(
    f_dist: FreqDist, path: str = "../gradu/material/final_results.xlsx"
):
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
    papers = load_papers()
    all_keywords = []
    for p in papers:
        all_keywords += p.keywords
    fdist = FreqDist(all_keywords)
    write_freq_dist_to_workbook(fdist)


if __name__ == "__main__":
    main()
