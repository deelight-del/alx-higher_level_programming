-- create db and table
-- CODE below.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
--USE hbtn_0d_usa
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id UNIQUE AUTO_INCREMENT INT PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	CONSTRAINT fk_cities FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id)
	) ENGINE=InnoDB;
