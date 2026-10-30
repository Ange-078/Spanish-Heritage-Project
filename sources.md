# Data Sources & Indicator Definitions

All historical time-series data in this application are retrieved directly from the **World Bank Open Data API v2** (`http://api.worldbank.org/v2/country/{country_code}/indicator/{indicator_code}`).

---

## Supported Indicators & Official Mappings

### 1. Life Expectancy at Birth, Total (Years)
- **Indicator Code:** `SP.DYN.LE00.IN`
- **Definition:** Life expectancy at birth indicates the number of years a newborn infant would live if prevailing patterns of mortality at the time of its birth were to stay the same throughout its life.
- **Source:** World Bank Group / UN Population Division.
- **Units:** Years

### 2. Unemployment, Total (% of Total Labor Force, National Estimate)
- **Indicator Code:** `SL.UEM.TOTL.NE.ZS`
- **Definition:** The share of the labor force that is without work but available for and seeking employment, based on national estimates.
- **Source:** International Labour Organization (ILO) / National Statistics Offices via World Bank.
- **Units:** Percent (%)

### 3. GDP per Capita (Current US$)
- **Indicator Code:** `NY.GDP.PCAP.CD`
- **Definition:** Gross domestic product divided by midyear population. GDP is the sum of gross value added by all resident producers plus any product taxes minus any subsidies not included in the value of products.
- **Note:** Represents economic output per person, **not** average wealth or individual household income.
- **Source:** World Bank national accounts data, and OECD National Accounts data files.
- **Units:** Current United States Dollars (US$)

### 4. Crude Birth Rate (per 1,000 People)
- **Indicator Code:** `SP.DYN.CBRT.IN`
- **Definition:** Annual number of live births occurring during the year per 1,000 population estimated at midyear.
- **Note:** Measures the rate of live births relative to population size, **not** total birth count.
- **Source:** UN Population Division / World Bank estimates.
- **Units:** Births per 1,000 people

### 5. Net Migration
- **Indicator Code:** `SM.POP.NETM`
- **Definition:** Net total of migrants during a 5-year period (total arrivals minus total departures). Positive values indicate net immigration; negative values indicate net emigration.
- **Note:** Represents net balance over time, **not** an total emigration count.
- **Source:** UN Population Division.
- **Units:** Net count of individuals

### 6. Intentional Homicides (per 100,000 People)
- **Indicator Code:** `VC.IHR.PSRC.P5`
- **Definition:** Unlawful deaths purposefully inflicted on a person by another person, expressed per 100,000 inhabitants.
- **Source:** UN Office on Drugs and Crime (UNODC) / World Bank.
- **Units:** Incidents per 100,000 people

### 7. Consumer Price Inflation (Annual %)
- **Indicator Code:** `FP.CPI.TOTL.ZG`
- **Definition:** The annual percentage change in the cost to the average consumer of acquiring a basket of goods and services.
- **Source:** International Monetary Fund, International Financial Statistics via World Bank.
- **Units:** Annual percentage (%)

### 8. Central Government Debt, Total (% of GDP)
- **Indicator Code:** `GC.DOD.TOTL.GD.ZS`
- **Definition:** Gross debt consists of all liabilities that require payment or payments of interest and/or principal by the debtor to the creditor at a date or dates in the future.
- **Source:** IMF Government Finance Statistics / World Bank.
- **Units:** Percent of GDP (%)

### 9. Total Reserves Including Gold (Current US$)
- **Indicator Code:** `FI.RES.TOTL.CD`
- **Definition:** Foreign assets held by central monetary authorities including SDRs, foreign exchange, reserve position in the IMF, and gold holdings at market prices.
- **Source:** IMF International Financial Statistics via World Bank.
- **Units:** Current United States Dollars (US$)

### 10. External Balance on Goods and Services (% of GDP)
- **Indicator Code:** `NE.RSB.GNFS.ZS`
- **Definition:** Exports of goods and services minus imports of goods and services expressed as a percentage of Gross Domestic Product.
- **Source:** World Bank national accounts data.
- **Units:** Percent of GDP (%)

---

## Featured Countries & Comparison Note
- **Costa Rica (CR)** — Primary focus country.
- **Mexico (MX)** — Hispanic Latin America.
- **Argentina (AR)** — Southern Cone / Hispanic Latin America.
- **Colombia (CO)** — Andean / Hispanic Latin America.
- **Chile (CL)** — Southern Cone / Hispanic Latin America.
- **Peru (PE)** — Andean / Hispanic Latin America.
- **Venezuela (VE)** — Hispanic Latin America.
- **Ecuador (EC)** — Andean / Hispanic Latin America.
- **Uruguay (UY)** — Southern Cone / Hispanic Latin America.
- **Brazil (BR)** — Latin American Lusophone (Portuguese-speaking) comparison benchmark. Brazil serves as a regional control to analyze macroeconomic and demographic trends across Latin America beyond Spanish-speaking nations.