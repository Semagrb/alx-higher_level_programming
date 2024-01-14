-- Create states table in hbtn_0e_0_usa with some data
DROP DATABASE IF EXISTS hbtn_0e_0_usa;
CREATE DATABASE hbtn_0e_0_usa;
USE hbtn_0e_0_usa;

CREATE TABLE states ( 
	    id INT AUTO_INCREMENT PRIMARY KEY, 
	    name VARCHAR(256) NOT NULL
);

INSERT INTO states (name) VALUES 
("California"), 
("Arizona"), 
("Texas"), 
("New York"), 
("Nevada");
