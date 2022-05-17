SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;



SET default_tablespace = '';

SET default_with_oids = false;


DROP TABLE IF EXISTS quiz.responses;
DROP TABLE IF EXISTS quiz.questions;
DROP TABLE IF EXISTS quiz.invitation;
DROP TABLE IF EXISTS quiz.quiz_table;
DROP TABLE IF EXISTS quiz.user_table;

DROP DATABASE IF EXISTS quiz;


CREATE DATABASE quiz;

\connect quiz;

CREATE TABLE user_table (
   user_name VARCHAR(100),
   user_password VARCHAR(100),
   id VARCHAR(100),
   PRIMARY KEY(id)
);

CREATE TABLE quiz_table (
   quiz_name VARCHAR(100),
   id VARCHAR(100),
   user_id VARCHAR(100),
   date_creation TIMESTAMP,
   PRIMARY KEY(id),
   FOREIGN KEY(user_id) REFERENCES user_table(id)
);


CREATE TABLE  invitation (
   invit_url VARCHAR(100),
   quiz_id VARCHAR(100),
   PRIMARY KEY(invit_url),
   FOREIGN KEY(quiz_id) REFERENCES quiz_table(id)
);

CREATE TABLE  questions (
   quiz_id VARCHAR(100),
   id VARCHAR(100),
   number_question NUMERIC,
   content VARCHAR(1000),
   PRIMARY KEY(id),
   FOREIGN KEY(quiz_id) REFERENCES quiz_table(id)
);

CREATE TABLE  responses (
   question_id VARCHAR(100),
   id VARCHAR(100),
   content VARCHAR(1000),
   is_true BOOLEAN,
   PRIMARY KEY(id),
   FOREIGN KEY(question_id) REFERENCES questions(id)
);
