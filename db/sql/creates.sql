-- table URLS shorted
CREATE TABLE urls (
  id INT NOT NULL,
  title VARCHAR(100) NOT NULL,
  address VARCHAR(500) NOT NULL,
  shorted VARCHAR(50) NOT NULL UNIQUE,
  clicks INT NOT NULL,
  PRIMARY KEY (id)
);
