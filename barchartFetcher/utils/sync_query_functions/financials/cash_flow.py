from io import StringIO

import pandas as pd


def cash_flow(
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

    url = f"https://www.barchart.com/stocks/quotes/{symbol}/cash-flow/{frequency}?reportPage={page}"
    data = StringIO(query_manager.sync_query(url=url, output_format="html"))

    return data


def process_cash_flow_response(data, format: str = "dict"):
    df = pd.read_html(data)[0].T

    df.columns = df.iloc[0]
    df = (
        df[1:]
        .dropna(how="all", axis=1)
        .rename(columns={df.columns[0]: "Period Ending"})
    )
    df["Period Ending"] = pd.to_datetime(
        df["Period Ending"], errors="coerce", format="%m-%Y"
    )
    df = df.set_index("Period Ending")
    df = df.apply(
        lambda col: pd.to_numeric(
            col.astype(str).str.replace(r"[,\$]", "", regex=True),
            errors="coerce",
        )
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
