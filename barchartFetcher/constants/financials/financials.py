# from barchartFetcher.utils.query_manager import QueryManager

# from io import StringIO
# import pandas as pd
#
#
# qm = QueryManager()
#
#
# import pandas as pd
# from io import StringIO
#
#
# def fetch_financials(type="income-statement", frequency="quarterly", ticker="NVDA"):
#
#    if type not in ["income-statement", "balance-sheet", "cash-flow"]:
#        raise ValueError(
#            "Invalid type. Choose from 'income-statement', 'balance-sheet', or 'cash-flow'."
#        )
#    if frequency not in ["quarterly", "annual"]:
#        raise ValueError("Invalid frequency. Choose from 'quarterly' or 'annual'.")
#
#    url = f"https://www.barchart.com/stocks/quotes/{ticker}/{type}/{frequency}?reportPage=1"
#    html = qm.sync_query(url, output_format="html")
#
#    df = pd.read_html(StringIO(html))[0].T
#    df.columns = df.iloc[0]
#    df = df.drop(index=0).reset_index(drop=True)
#
#    df = df.rename(columns={df.columns[0]: "Period"})
#    df = df.loc[:, ~df.columns.duplicated()]
#
#    df["Period"] = pd.to_datetime(df["Period"], errors="coerce")
#
#    for col in df.columns.drop("Period"):
#        df[col] = (
#            df[col].astype(str).str.replace(",", "", regex=False).str.replace("$", "", regex=False)
#        )
#        df[col] = pd.to_numeric(df[col], errors="coerce")
#
#    return df
#
#
# fetch_financials(type="cash-flow", frequency="quarterly", ticker="NVDA")
#
