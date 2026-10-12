import pandas as pd
import pytest

from dashvendas.data import load_sales, total_by_country


def test_load_sales_reads_raw_csv():
    df = load_sales()
    assert list(df.columns) == [
        "InvoiceNo", "Description", "OrderValue", "Quantity", "CustomerID", "Country",
    ]
    assert len(df) == 500
    assert df["Country"].nunique() == 5


def test_load_sales_rejects_missing_columns(tmp_path):
    path = tmp_path / "bad.csv"
    pd.DataFrame({"InvoiceNo": [1], "OrderValue": [10.0]}).to_csv(path, index=False)
    with pytest.raises(ValueError, match="Country"):
        load_sales(path)


def test_total_by_country():
    result = total_by_country(load_sales())
    assert len(result) == 5
    assert result.iloc[0]["Country"] == "Australia"
    assert result.iloc[0]["OrderValue"] == pytest.approx(6349.89)
    assert result.iloc[-1]["Country"] == "Hong Kong"
    assert result["OrderValue"].sum() == pytest.approx(16918.64)
