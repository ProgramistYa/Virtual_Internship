--
-- PostgreSQL database cluster dump
--

-- Started on 2023-06-20 17:55:54

SET default_transaction_read_only = off;

SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;

--
-- Roles
--

CREATE ROLE postgres;
ALTER ROLE postgres WITH SUPERUSER INHERIT CREATEROLE CREATEDB LOGIN REPLICATION BYPASSRLS PASSWORD 'SCRAM-SHA-256$4096:Fydx9nN9D00WsdT8MHj3sA==$pLnXlrUM4n7q1c03iCDNguHuiGIiAblUHd/A7FeyNgE=:EnGYqNmQVw3nbcNWu8NYj4GhPh1p8aji8A0VM6fAHy0=';

--
-- User Configurations
--








-- Completed on 2023-06-20 17:55:54

--
-- PostgreSQL database cluster dump complete
--

