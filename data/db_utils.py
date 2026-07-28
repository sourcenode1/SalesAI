"""
Data-layer utilities for SalesAI — loads from local Excel files (MainData).
Provides real KPIs from Zenex sales data.
"""
import os
import streamlit as st
import pandas as pd
import numpy as np

BASE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "files")

MONTH_MAP = {
    "January": 1, "February": 2, "March": 3, "April": 4,
    "May": 5, "June": 6, "July": 7, "August": 8,
    "September": 9, "October": 10, "November": 11, "December": 12,
}


@st.cache_data(ttl=600)
def _load_sales():
    path = os.path.join(BASE_PATH, "sales_transactions.csv.gz")
    if not os.path.exists(path):
        return pd.DataFrame()
    df = pd.read_csv(path, compression="gzip")
    df["Document_Date"] = pd.to_datetime(df.get("Document_Date"), errors="coerce")
    df["Net_Sales_Value"] = pd.to_numeric(df.get("Net_Sales_Value", 0), errors="coerce").fillna(0)
    df["Net_Sales_Qty"] = pd.to_numeric(df.get("Net_Sales_Qty", 0), errors="coerce").fillna(0)
    df["sale_month"] = df["Document_Date"].dt.month
    df["sale_year"] = df["Document_Date"].dt.year
    return df


@st.cache_data(ttl=600)
def _load_targets():
    path = os.path.join(BASE_PATH, "targets.csv.gz")
    if not os.path.exists(path):
        return pd.DataFrame()
    return pd.read_csv(path, compression="gzip")


@st.cache_data(ttl=600)
def _load_chemist_visits():
    path = os.path.join(BASE_PATH, "chemist_visit.csv.gz")
    if not os.path.exists(path):
        return pd.DataFrame()
    df = pd.read_csv(path, compression="gzip")
    df["POB value"] = pd.to_numeric(df.get("POB value", 0), errors="coerce").fillna(0)
    return df


@st.cache_data(ttl=600)
def fetch_module_data(module: str, year: int, month: str) -> dict:
    """Fetch primary KPI data for a module/year/month combination."""
    m = MONTH_MAP.get(month, 1)

    if module == "sales":
        sales = _load_sales()
        if sales.empty:
            return {}
        month_data = sales[(sales["sale_month"] == m) & (sales["sale_year"] == year)]
        prev_m = m - 1 if m > 1 else 12
        prev_y = year if m > 1 else year - 1
        prev_data = sales[(sales["sale_month"] == prev_m) & (sales["sale_year"] == prev_y)]

        net_sales = month_data["Net_Sales_Value"].sum()
        prev_sales = prev_data["Net_Sales_Value"].sum()
        growth = ((net_sales - prev_sales) / prev_sales * 100) if prev_sales > 0 else 0
        invoice_count = len(month_data)
        avg_invoice = net_sales / invoice_count if invoice_count > 0 else 0

        return {
            "net_sales": net_sales,
            "invoice_count": invoice_count,
            "avg_invoice": avg_invoice,
            "mom_growth": growth,
            "total_qty": month_data["Net_Sales_Qty"].sum(),
            "active_hqs": month_data["HqCode"].nunique(),
            "active_products": month_data["ProductCode"].nunique(),
        }

    if module == "salesforce":
        cv = _load_chemist_visits()
        if cv.empty:
            return {}
        month_data = cv[(cv["Work Month"] == m) & (cv["Work Year"] == year)]
        total_visits = len(month_data)
        productive = int((month_data["POB value"] > 0).sum())
        conversion = (productive / total_visits * 100) if total_visits > 0 else 0
        active_reps = month_data["Employee Code"].nunique()

        return {
            "total_visits": total_visits,
            "productive_visits": productive,
            "conversion_rate": conversion,
            "active_reps": active_reps,
            "avg_pob": month_data["POB value"].mean(),
        }

    return {}


@st.cache_data(ttl=600)
def fetch_yearly_trend(module: str, year: int) -> list[dict]:
    """Fetch month-by-month KPI data for trend charts."""
    if module == "Sales":
        sales = _load_sales()
        if sales.empty:
            return []
        year_data = sales[sales["sale_year"] == year]
        monthly = year_data.groupby("sale_month").agg(
            net_sales=("Net_Sales_Value", "sum"),
            invoice_count=("Net_Sales_Value", "count"),
            total_orders=("Net_Sales_Qty", "sum"),
        ).reset_index()
        from config.app_config import MONTHS
        result = []
        for i, m_name in enumerate(MONTHS, 1):
            row = monthly[monthly["sale_month"] == i]
            if not row.empty:
                result.append({
                    "month": m_name,
                    "net_sales": round(row["net_sales"].iloc[0] / 100000, 1),
                    "invoice_count": int(row["invoice_count"].iloc[0]),
                    "total_orders": int(row["total_orders"].iloc[0]),
                })
            else:
                result.append({"month": m_name, "net_sales": None, "invoice_count": None, "total_orders": None})
        return result

    if module == "SalesForce":
        cv = _load_chemist_visits()
        if cv.empty:
            return []
        year_data = cv[cv["Work Year"] == year]
        monthly = year_data.groupby("Work Month").agg(
            total_visits=("Customer Code", "count"),
            productive=("POB value", lambda x: (x > 0).sum()),
        ).reset_index()
        from config.app_config import MONTHS
        result = []
        for i, m_name in enumerate(MONTHS, 1):
            row = monthly[monthly["Work Month"] == i]
            if not row.empty:
                result.append({
                    "month": m_name,
                    "total_visits": int(row["total_visits"].iloc[0]),
                    "sessions_conducted": int(row["productive"].iloc[0]),
                })
            else:
                result.append({"month": m_name, "total_visits": None, "sessions_conducted": None})
        return result

    return []


@st.cache_data(ttl=600)
def fetch_module_summary(module: str, year: int) -> dict:
    """Fetch a high-level summary for the drill-down header."""
    return {}
