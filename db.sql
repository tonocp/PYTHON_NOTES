CREATE DATABASE IF NOT EXISTS python_notes;
use python_notes;

CREATE TABLE users(
    id  int(25) auto_increment not null,
    name varchar(100),
    surnames varchar(255),
    email varchar(255) not null,
    password varchar(255) not null,
    fecha date not null,
    CONSTRAINT pk_users PRIMARY KEY (id),
    CONSTRAINT uq_email UNIQUE(email)
)ENGINE=InnoDb;

CREATE TABLE notes(
    id  int(25) auto_increment not null,
    user_id int(25) not null,
    title varchar(255) not null,
    description MEDIUMTEXT,
    date date not null,
    CONSTRAINT pk_notes PRIMARY KEY(id),
    CONSTRAINT fk_user_note FOREIGN KEY (user_id) REFERENCES users(id)
)ENGINE=InnoDb;