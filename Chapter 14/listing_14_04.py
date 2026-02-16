def monthly_sum(df, date_col, value_cols):
    return (
        df.set_index(date_col)
          .resample("M")
          .agg({col: "sum" for col in value_cols})
          .rename_axis("month")
          .reset_index()
)

monthly = monthly_sum(df, "date", ["sales_a", "sales_b"])

