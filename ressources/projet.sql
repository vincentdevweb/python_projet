DROP DATABASE IF EXISTS python_projet;
CREATE DATABASE python_projet;

USE python_projet;

-- create table utilisateur 

CREATE TABLE IF NOT EXISTS utilisateur (
    id int auto_increment primary key,
    nom varchar(255) not null,
    prenom varchar(255) not null,
    email varchar(255) not null,
    gender varchar(255) not null,
    password varchar(255) not null,
    old_password varchar(255) not null
);

--  create table compte

CREATE TABLE IF NOT EXISTS compte (
    id int auto_increment primary key,
    cle varchar(255) not null,
    sel varchar(255) not null,
    id_utilisateur int not null
);

-- foreign key constraints id_utilisateur

ALTER TABLE 
    compte
ADD 
    CONSTRAINT fk_id_utilisateur FOREIGN KEY (id_utilisateur) REFERENCES utilisateur(id) ON DELETE CASCADE ON UPDATE CASCADE;

-- email unique constraint

ALTER TABLE
    utilisateur
ADD 
    CONSTRAINT email_unique UNIQUE (email);

-- -- test with insert table manually

-- INSERT INTO utilisateur (nom, prenom, email, gender, password, old_password) VALUES ("")