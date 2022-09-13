--
-- PostgreSQL database dump
--

-- Dumped from database version 14.5
-- Dumped by pg_dump version 14.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

DROP DATABASE IF EXISTS test_task_dataox;
--
-- Name: test_task_dataox; Type: DATABASE; Schema: -; Owner: aleksandrbarinov
--

CREATE DATABASE test_task_dataox WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.UTF-8';


ALTER DATABASE test_task_dataox OWNER TO aleksandrbarinov;

\connect test_task_dataox

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO postgres;

--
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS 'standard public schema';


SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: apartments; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.apartments (
    id integer NOT NULL,
    image_link text,
    title text,
    date_posted character varying(100),
    location text,
    number_of_beds text,
    description text,
    currency text,
    price numeric
);


ALTER TABLE public.apartments OWNER TO postgres;

--
-- Name: apartments_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.apartments_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.apartments_id_seq OWNER TO postgres;

--
-- Name: apartments_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.apartments_id_seq OWNED BY public.apartments.id;


--
-- Name: apartments id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.apartments ALTER COLUMN id SET DEFAULT nextval('public.apartments_id_seq'::regclass);
