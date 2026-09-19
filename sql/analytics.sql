-- Total Revenue
SELECT SUM (total_amount) AS total_revenue
FROM orders
WHERE status = 'Completed';

-- Total Orders
SELECT COUNT(*) AS total_orders
FROM orders;

-- Total Customers
SELECT COUNT(*) AS total_customers
FROM customers;

-- Average Order Value
SELECT AVG(total_amount) AS average_order_value
FROM orders 
WHERE status = 'Completed';

-- Revenue By Customers
SELECT c.customers_id, 
       c.first_name, 
       c.last_name, 
       COUNT(o.order_id) AS total_orders,
       SUM(o.total_amount) AS total_spent,
       FROM customers customers
       JOIN orders o 
        ON c.customers_id = o.customers_id
       WHERE o.status = 'Completed'
       GROUP BY c.customers_id,
                c.first_name,
                c.last_name
       ORDER BY total_spent DESC;