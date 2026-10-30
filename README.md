# Hispanic Heritage Historical Data Explorer

A Streamlit web application that retrieves historical socioeconomic data from the World Bank API (1956–2025), fits polynomial models using centered time variables, analyzes polynomial mathematical features (Calculus, Precalculus, and Algebra 2 pathways), performs comparative country evaluations, and exports publication-ready PDF, Excel, and CSV analytical reports.

---

## Research Question & Choices
- **Primary Country:** Costa Rica (CR)
- **Research Question:** How has Costa Rica's Gross Domestic Product (GDP) per capita evolved over the past seven decades compared to regional peer countries, and how effectively can higher-degree polynomial models capture long-term structural economic shifts versus short-term macroeconomic volatility?
- **Featured Indicator:** GDP per capita (Current US$) (`NY.GDP.PCAP.CD`)
- **Assigned Mathematics Pathway:** Calculus

---

## Local Installation & Execution

1. **Clone or download the project files into a single directory:**
   - `app.py`
   - `requirements.txt`
   - `README.md`
   - `sources.md`

2. **Set up a Python Virtual Environment (Recommended):**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate