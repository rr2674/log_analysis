# Logs Analysis

A reporting tool that prints out reports (_in plain text_) based on the data in a **PostgreSQL** database.

The tool will connect to the data base, execute three queries and print the results.

## Questions Answered
- What are the most popular three articles of all time?
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests lead to errors?

## Dependencies

PostgreSQL database with the following:

- dbname=news
- Table names
  - articles
  -  authors
  - logs

## Usage

##### Command Line

```
python3 log_analysis.py
```
