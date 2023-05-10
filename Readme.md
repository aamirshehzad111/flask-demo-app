We will create mysql db using docker container, steps are below

--> docker volume create mysql-volume
--> docker run --name=mk-mysql -p3306:3306 -v mysql-volume:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=test -d mysql:latest
--> docker exec -it mk-mysql bash
--> mysql -u root -p (run inside it mysql container)
--> create database usersdb using command create database usersdb;
--> use usersdb via command use usersdb
--> create table,
CREATE DATABASE mydatabase;
USE mydatabase;
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL
);

This is a python rest api based app that perform operations on users
* Add users
* Get users
* Get user by id
* Update users
* Delete user

Dependencies:
* Flask
* Flask-MySQLdb 
* pyyaml
* mysql db

--> sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
--> pip install -r requirements.txt
--> python3 app.py or sudo nohup python3 app.py & (to run bg)
--> ps aux | grep app.py
