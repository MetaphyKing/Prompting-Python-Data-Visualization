import matplotlib as mpl, json, pathlib

def export_rcparams(path="styles/rcparams.json"):
    p = pathlib.Path(path); p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(dict(mpl.rcParams), indent=2))

def load_rcparams(path="styles/rcparams.json"):
    params = json.loads(pathlib.Path(path).read_text())
    mpl.rcParams.update(params)

def data_contract(df):
    assert df["date"].min() >= pd.Timestamp("2023-01-01")
    assert df["date"].max() <= pd.Timestamp("2025-12-31")
    assert df["category"].nunique() <= 50
    assert df["value"].notna().mean() > 0.9
