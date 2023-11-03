CREATE TABLE IF NOT EXISTS exchange_rates (
    id INTEGER PRIMARY KEY,
    fecha DATE,
    value_avg FLOAT,
    value_sell FLOAT,
    value_buy FLOAT,
    currency_type INT,
    currency_name VARCHAR(255)
)
SORTKEY (fecha);
