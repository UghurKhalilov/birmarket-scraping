# Birmarket.az — Web Scraping, EDA & Machine Learning

## Overview
An end-to-end data science project focused on the Azerbaijani e-commerce market. Product data was collected from Birmarket.az via automated web scraping, followed by exploratory data analysis and predictive modeling.

## Tech Stack
| Area | Tools |
|------|-------|
| Web Scraping | Selenium, BeautifulSoup4 |
| Data Analysis | Pandas, Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Statistical Testing | Scipy |
| Environment | Python 3.14, UV |

## Project Structure
Bir_market/
├── birmarket_selenium/
│ ├── birmarket.py # Base Chrome driver class
│ ├── birmarket_filter.py # Category navigation
│ └── get_all_result.py # Product scraping logic
├── analysis/
│ └── analysis.ipynb # EDA & ML notebook
├── main.py
├── products.csv
└── requirements.txt

## Data Collection
- **Source:** Birmarket.az — Large Home Appliances category
- **Products scraped:** 2,367
- **Features:** name, new price, old price, discount, rating score, rating count
- **Method:** Dynamic scraping with Selenium ("Load More" button automation) + BeautifulSoup for fast HTML parsing

## Exploratory Data Analysis

### Key Findings
- **Biryusa** leads in product count (254 products), while **LG** has the highest average price (1,959 AZN)
- **Wine cabinets** have the highest average price (~2,800 AZN) — nearly twice that of refrigerators
- Most products fall in the **0–1,000 AZN** price range (right-skewed distribution)
- Discounts are concentrated between **20–50%**, with a peak at 25–35%
- Products with higher rating scores (4.0–5.0) receive significantly more reviews
- **A/B Testing** (Soyuducu vs Qabyuyan): statistically significant price difference confirmed (p = 0.0017)

## Machine Learning

### Model 1 — Price Prediction
| Metric | Value |
|--------|-------|
| R² | 0.59 |
| MAE | ~371 AZN |
| RMSE | ~614 AZN |

Brand and category explain 59% of price variance — aligning with the intuition that pricing is closely tied to brand positioning and product type.

### Model 2 — Rating Score Prediction
| Metric | Value |
|--------|-------|
| R² | -0.47 |
| MAE | ~0.52 |
| RMSE | ~0.58 |

Rating score cannot be reliably predicted from available features. Customer ratings are likely driven by product quality, durability, and personal experience — factors not captured in this dataset.

## Conclusion
Price prediction is feasible using brand and category as features, achieving a moderate R² of 0.59. Rating prediction, however, requires richer data such as product specifications or customer reviews. Future improvements could include scraping additional features and applying more advanced models (Random Forest, XGBoost).