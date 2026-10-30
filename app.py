import datetime
import io
import math
import typing
import requests

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    Image,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from sklearn.metrics import mean_absolute_error, r2_score

# ==============================================================================
# CONFIGURATION & GLOBAL CONSTANTS
# ==============================================================================
st.set_page_config(
    page_title="Hispanic Heritage Historical Data Explorer",
    page_icon="🌎",
    layout="wide",
    initial_sidebar_state="expanded",
)

CURRENT_YEAR = datetime.datetime.now().year
START_YEAR = CURRENT_YEAR - 70
END_YEAR = CURRENT_YEAR - 1

COUNTRIES = {
    "Costa Rica": "CR",
    "Mexico": "MX",
    "Brazil": "BR",
    "Argentina": "AR",
    "Colombia": "CO",
    "Chile": "CL",
    "Peru": "PE",
    "Venezuela": "VE",
    "Ecuador": "EC",
    "Uruguay": "UY",
}

INDICATORS = {
    "Life Expectancy at Birth": {
        "code": "SP.DYN.LE00.IN",
        "units": "Years",
        "min_val": 0.0,
        "max_val": 120.0,
        "desc": "Life expectancy at birth indicates the number of years a newborn infant would live if prevailing patterns of mortality at the time of its birth stay the same.",
    },
    "Unemployment Rate (National Estimate)": {
        "code": "SL.UEM.TOTL.NE.ZS",
        "units": "% of Total Labor Force",
        "min_val": 0.0,
        "max_val": 100.0,
        "desc": "The share of the labor force that is without work but available for and seeking employment, based on national estimates.",
    },
    "GDP per Capita": {
        "code": "NY.GDP.PCAP.CD",
        "units": "Current US$",
        "min_val": 0.0,
        "max_val": 200000.0,
        "desc": "Gross Domestic Product divided by midyear population. Measures aggregate economic output per person, NOT individual average wealth or household income.",
    },
    "Crude Birth Rate": {
        "code": "SP.DYN.CBRT.IN",
        "units": "Births per 1,000 People",
        "min_val": 0.0,
        "max_val": 100.0,
        "desc": "Annual number of live births per 1,000 population estimated at midyear. This measures rate relative to population, NOT total birth count.",
    },
    "Net Migration": {
        "code": "SM.POP.NETM",
        "units": "Net Population Count",
        "min_val": -10000000.0,
        "max_val": 10000000.0,
        "desc": "Net total of migrants during 5-year periods (arrivals minus departures). Positive indicates net immigration; negative indicates net emigration. NOT an absolute emigration count.",
    },
    "Intentional Homicide Rate": {
        "code": "VC.IHR.PSRC.P5",
        "units": "Per 100,000 People",
        "min_val": 0.0,
        "max_val": 300.0,
        "desc": "Unlawful deaths purposefully inflicted on a person by another person, expressed per 100,000 inhabitants.",
    },
    "Consumer Price Inflation": {
        "code": "FP.CPI.TOTL.ZG",
        "units": "Annual %",
        "min_val": -100.0,
        "max_val": 10000.0,
        "desc": "Annual percentage change in the cost to the average consumer of acquiring a basket of goods and services.",
    },
    "Central Government Debt": {
        "code": "GC.DOD.TOTL.GD.ZS",
        "units": "% of GDP",
        "min_val": 0.0,
        "max_val": 500.0,
        "desc": "Gross debt of central government liabilities requiring future payments of interest and/or principal.",
    },
    "Total Reserves (Includes Gold)": {
        "code": "FI.RES.TOTL.CD",
        "units": "Current US$",
        "min_val": 0.0,
        "max_val": 1e12,
        "desc": "Foreign assets held by central monetary authorities including gold holdings at market prices.",
    },
    "External Balance on Goods & Services": {
        "code": "NE.RSB.GNFS.ZS",
        "units": "% of GDP",
        "min_val": -100.0,
        "max_val": 100.0,
        "desc": "Exports of goods and services minus imports of goods and services expressed as a percentage of GDP.",
    },
}

# ==============================================================================
# DATA RETRIEVAL & CACHING
# ==============================================================================
@st.cache_data(ttl=3600, show_spinner=False)
def fetch_world_bank_data(country_code: str, indicator_code: str, start_yr: int, end_yr: int) -> pd.DataFrame:
    """
    Fetches official historical data directly from World Bank API v2.
    Returns DataFrame with columns ['Year', 'Value'].
    Handles network errors, empty payloads, and missing records safely without fabrication.
    """
    url = f"http://api.worldbank.org/v2/country/{country_code}/indicator/{indicator_code}"
    params = {
        "date": f"{start_yr}:{end_yr}",
        "format": "json",
        "per_page": 1000,
    }
    try:
        resp = requests.get(url, params=params, timeout=10)
        resp.raise_for_status()
        json_data = resp.json()

        if len(json_data) < 2 or json_data[1] is None:
            return pd.DataFrame(columns=["Year", "Value"])

        records = json_data[1]
        extracted = []
        for rec in records:
            val = rec.get("value")
            yr = rec.get("date")
            if val is not None and yr is not None:
                try:
                    extracted.append({"Year": int(yr), "Value": float(val)})
                except ValueError:
                    continue

        df = pd.DataFrame(extracted)
        if not df.empty:
            df = df.sort_values("Year").reset_index(drop=True)
        return df
    except Exception as e:
        st.error(f"API Error fetching data for {country_code} ({indicator_code}): {e}")
        return pd.DataFrame(columns=["Year", "Value"])

# ==============================================================================
# MATHEMATICAL MODELING &