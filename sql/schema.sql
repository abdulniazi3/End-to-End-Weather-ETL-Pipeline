
/*select all data */

SELECT *
FROM weather_data

/*Average temperature */

SELECT
    MAX(temperature) AS highest_temperature
FROM weather_data;

/*Highest temperature recorded */

SELECT
    city,
    COUNT(*) AS total_records
FROM weather_data
GROUP BY city;

/*Creating table */

CREATE TABLE weather_data (
    id SERIAL PRIMARY KEY,
    city VARCHAR(50),
    temperature FLOAT,
    humidity INT,
    condition VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);