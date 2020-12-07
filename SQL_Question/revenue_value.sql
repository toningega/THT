WITH prices
        AS (
            SELECT product
                ,price_effective_date
                ,price
                ,coalesce(LEAD(price_effective_date, 1, NULL) OVER (
                        PARTITION BY product ORDER BY price_effective_date
                        ), '12/31/9999') AS price_effective_to
            FROM prices
            )

SELECT SUM(quantity * price) AS total_revenue_value
FROM sales s
INNER JOIN prices p 
    ON s.product = p.product
        AND s.sales_date BETWEEN p.price_effective_date
            AND p.price_effective_to