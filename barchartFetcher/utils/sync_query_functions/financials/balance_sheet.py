from io import StringIO

import pandas as pd


def balance_sheet(
    query_manager,
    symbol: str = "AAPL",
    frequency: str = "annual",
    page: int = 1,
):
    """Query function for balance_sheet using QueryManager

    frequency == "annual" or frequency == "quarterly"

    """
    if frequency not in ["annual", "quarterly"]:
        raise ValueError("Frequency must be 'annual' or 'quarterly'.")

    if format not in ["dataframe", "dict"]:
        raise ValueError("Format must be 'dataframe' or 'dict'.")

    url = f"https://www.barchart.com/stocks/quotes/{symbol}/balance-sheet/{frequency}?reportPage={page}"
    data = StringIO(query_manager.sync_query(url=url, output_format="html"))
    return data


def process_balance_sheet_responser(data, format: str = "dict"):
    try:
        df = pd.read_html(data)[0].T

        df.columns = [
            "Period Ending",
            "Assets",
            "Current Assets",
            "Cash & Cash Equivalents",
            "Marketable Securities",
            "Receivables",
            "Inventories",
            "Other current assets",
            "Total Current Assets",
            "Empty",
            "Non-Current Assets",
            "PPE Net",
            "Investments And Advances",
            "Other Non-Current Assets",
            "Total Non-Current Assets",
            "Empty",
            "Total Assets",
            "Empty",
            "Liabilities",
            "Current Liabilities",
            "Short Term Debt",
            "Accounts payable and accrued liabilities",
            "Other current liabilities",
            "Total Current Liabilities",
            "Empty",
            "Non-Current Liabilities",
            "Long Term Debt",
            "Deferred Revenues",
            "aiOther Non-Current Liabilities",
            "Total Non-Current Liabilities",
            "Empty",
            "Total Liabilities",
            "Empty",
            "Shareholders' Equity",
            "Shares Outstanding, K",
            "Common Shares",
            "Retained earnings",
            "Other shareholders' equity",
            "Total Shareholders' Equity",
            "Empty",
            "Total Liabilities And Equity",
        ]

        df = (
            df[1:]
            .dropna(how="all", axis=1)
            .rename(columns={df.columns[0]: "Period Ending"})
        )
        df["Period Ending"] = pd.to_datetime(
            df["Period Ending"], errors="coerce", format="%m-%Y"
        )
        df = df.set_index("Period Ending")

        for col in df.columns:
            df[col] = pd.to_numeric(
                df[col].str.replace(",", "").str.replace("$", ""),
                errors="coerce",
            )

        if format == "dataframe":
            return df
        elif format == "dict":
            df_dict = df.reset_index()
            df_dict["Period Ending"] = df_dict["Period Ending"].dt.strftime(
                "%Y-%m-%d"
            )
            df_dict = df_dict.to_dict(orient="records", index=True)

            return df_dict

    except Exception as e:
        print(f"Error processing balance sheet response: {e}")
        return None
