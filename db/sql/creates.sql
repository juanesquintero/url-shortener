-- table URLS shorted
CREATE TABLE urls (
  id SERIAL PRIMARY KEY,
  title VARCHAR(100),
  address VARCHAR(500) NOT NULL,
  shorted VARCHAR(50) UNIQUE,
  clicks INT DEFAULT 0
);
