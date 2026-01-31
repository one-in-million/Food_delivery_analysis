# Food Delivery Data Analysis Project

## Project Overview
This project involves simulating a real-world data engineering and analysis workflow. It focuses on integrating three disparate data sources (CSV, JSON, and SQL) to create a unified dataset for a food delivery platform. The final dataset is used to perform deep-dive analytics on user behavior, restaurant performance, and revenue trends.

## Datasets
The analysis is based on the following three files:
1.  **orders.csv (Transactional Data):** Contains order details including `order_id`, `user_id`, `restaurant_id`, `order_date`, and `total_amount`.
2.  **users.json (User Master Data):** Contains profile information such as `city` and `membership` status (Gold/Regular).
3.  **restaurants.sql (Restaurant Master Data):** SQL insert statements containing restaurant names, `cuisine` types, and `rating`.

## Analysis Workflow
The project follows a structured data pipeline:
* **Data Ingestion:** Loading CSV via Pandas, JSON via the json library, and parsing SQL using Regular Expressions (Regex).
* **Data Cleaning:** Ensuring correct data types for IDs and numerical values.
* **Data Merging:** Performing Left Joins to combine transactions with user and restaurant metadata without losing order history.
* **Exploratory Data Analysis (EDA):** Calculating Key Performance Indicators (KPIs) such as:
    * Average Order Value (AOV) per membership tier.
    * Revenue distribution across cities and cuisines.
    * Customer segmentation based on lifetime value.

## Key Insights
* **Membership Trends:** Gold members account for approximately 50% of total orders.
* **Regional Performance:** Chennai emerged as the top revenue-generating city among Gold members.
* **Cuisine Popularity:** Mexican cuisine holds the highest average order value across the platform.
* **Rating Impact:** High-rated restaurants (4.6–5.0) are the primary drivers of total revenue.

## How to Run the Notebook
1.  Ensure you have Python installed with the `pandas` library.
2.  Place `orders.csv`, `users.json`, and `restaurants.sql` in the same directory as the notebook.
3.  Run all the codes in `food.py` to generate the `final_food_delivery_dataset.csv` and view the statistical outputs.

## Technologies Used
* Python 3.x
* Pandas (Data Manipulation)
* Regex (SQL Parsing)
* JSON (Data Handling)# Food_delivery_analysis
