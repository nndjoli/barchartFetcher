import pandas as pd
from bs4 import BeautifulSoup


def parse_financial_table(html: str) -> pd.DataFrame:
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table")

    date_header_cells = table.find_all(
        "tr", class_="bc-financial-report__row-dates"
    )[0].find_all("td")[1:]
    period_texts = [cell.get_text(strip=True) for cell in date_header_cells]
    date_index = pd.to_datetime(period_texts, format="%m-%Y", errors="coerce")

    row_labels: list[str] = []
    data_rows: list[list[float | pd.NA]] = []

    current_group: str | None = None
    current_subgroup: str | None = None

    for row in table.find_all("tr")[1:]:
        row_classes = row.get("class", [])

        if (
            "bc-financial-report__row-separator" in row_classes
            or "bc-financial-report__row-dates" in row_classes
        ):
            continue

        first_cell = row.find("td")
        row_label = first_cell.get_text(strip=True)

        if "bc-financial-report__row-group-label" in row_classes:
            current_group = row_label
            current_subgroup = None
            row_labels.append(current_group)
            data_rows.append([pd.NA] * len(date_index))
            continue

        if "bc-financial-report__row-subgroup-label" in row_classes:
            current_subgroup = row_label
            continue

        row_values: list[float | pd.NA] = []
        for cell in row.find_all("td")[1:]:
            text_value = (
                cell.get_text(strip=True).replace(",", "").replace("$", "")
            )
            if text_value in ("", "-", "—", "NA", "N/A"):
                row_values.append(pd.NA)
            else:
                try:
                    row_values.append(float(text_value))
                except ValueError:
                    row_values.append(pd.NA)

        if len(row_values) < len(date_index):
            row_values += [pd.NA] * (len(date_index) - len(row_values))
        elif len(row_values) > len(date_index):
            row_values = row_values[: len(date_index)]

        if (
            "bc-financial-report__row-subgroup-total" in row_classes
            and current_subgroup
        ):
            line_name = f"Total {current_subgroup}"
        elif "bc-financial-report__row-group-total" in row_classes:
            line_name = row_label
        else:
            line_name = row_label

        row_labels.append(line_name)
        data_rows.append(row_values)

    df = pd.DataFrame(data_rows, index=row_labels, columns=date_index)
    df = df.dropna(how="all", axis=0)

    return df
