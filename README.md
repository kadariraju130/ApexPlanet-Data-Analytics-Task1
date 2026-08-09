# ApexPlanet Data Analytics Internship - Task 1

## Project Overview
This project focuses on **Data Immersion & Wrangling**, covering data access, profiling, quality assessment, and cleaning using Python (Pandas) to prepare an analysis-ready dataset.

---

## Data Dictionary

| Column Name | Data Type | Description / Meaning | Potential Business Relevance |
| :--- | :--- | :--- | :--- |
| **Order_ID** | String / Text | Unique alphanumeric identifier assigned to each individual sales transaction. | Used for tracking orders, managing returns, and joining tables. |
| **Order_Date** | Date (YYYY-MM-DD) | The specific calendar date when the order was placed. | Essential for trend analysis, seasonality tracking, and monthly/yearly performance forecasting. |
| **Customer_ID** | String / Text | Unique identifier assigned to each registered customer. | Used for calculating customer lifetime value (LTV) and tracking repeat purchasers. |
| **Customer_Name** | String / Text | The anonymized name or code label of the customer (e.g., Customer_227). | Used for customer-level segmentation and personalized reporting. |
| **Age** | Integer / Numeric | The age of the customer at the time of purchase. | Helps identify target demographic segments and age-specific buying preferences. |
| **Gender** | String / Categorical | The recorded gender of the customer (Male, Female, Unknown). | Useful for demographic market segmentation and targeted promotional strategies. |
| **City** | String / Categorical | The geographic city location where the order originated or was delivered. | Critical for regional sales distribution analysis and identifying top-performing markets. |
| **Product** | String / Categorical | The specific name of the item purchased (e.g., Rice, Mobile, Laptop, Shoes, Chair, Book). | Tracks inventory performance, high-demand items, and cross-selling opportunities. |
| **Category** | String / Categorical | The broad classification of the product (Grocery, Education, Electronics, Fashion, Furniture). | Helps evaluate category-level revenue contributions and business portfolio performance. |
| **Quantity** | Integer / Numeric | The total number of units of the product purchased in a single order. | Measures bulk-buying behavior and inventory turnover rates. |
| **Unit_Price** | Float / Numeric | The price of a single unit of the product in local currency. | Used for pricing strategy analysis, discount tracking, and margin assessments. |
| **Total_Sales** | Float / Numeric | The total revenue generated for the order (Quantity × Unit_Price). | The primary Key Performance Indicator (KPI) for financial performance and overall revenue tracking. |

---

## Data Cleaning Process
1. **Missing Values Handling:** * Categorical columns (`City`, `Gender`) with missing entries were imputed with `"Unknown"`.
   * Numerical columns (`Age`) were processed and imputed using the dataset's median age to avoid skewness.
2. **Output:** Saved as `Cleaned_Sales_Dataset.csv` for downstream exploratory data analysis and visualization tasks.
