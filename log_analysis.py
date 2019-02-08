#!/usr/bin/env python3

import psycopg2


def do_query(db, query):

    cur = db.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    cur.close()

    return rows


def most_popular_three_articles(db):
    """
    Q: Which articles have been accessed the most?
    This function will display a sorted list with the most popular articles
     at the top.
    """
    query = r"""
    select title, subq.views as views
      from articles,
          ( select substring(path,'\/article\/(.*)') as logslug,
                   count(*) as views
              from log
              group by path ) as subq
      where  slug = subq.logslug
      order by views desc
      limit 3;
    """

    print('\nWhich articles have been accessed the most?\n')
    for row in do_query(db, query):
        print('\t"{}" -- {:,} views'.format(row[0], row[1]))


def most_popular_article_authors(db):
    """
    Who are the most popular article authors of all time? 
    This function will display a sorted list with the most popular author
    at the top.
    """

    query = r"""
    select name, views
      from authors,
          ( select author, count(*) as views
              from articles,
                  ( select substring(path,'\/article\/(.*)') as logslug
                      from log ) as subq1
             where logslug is not null
               and slug = subq1.logslug
             group by author) as subq2
     where authors.id = subq2.author
     order by views desc;
    """

    print('\nWho are the most popular article authors of all time?\n')
    for row in do_query(db, query):
        print('\t{} -- {:,} views'.format(row[0], row[1]))


def daily_error_gt_1pct(db):
    """
    On which days did more than 1% of requests lead to errors?
    """

    query = """
    select day, to_char(error_pct,'999D99%') as error_pct
      from ( select day,
                   ( (  sum(occurance) filter(where status != '200 OK')
                      / sum(occurance) ) * 100 ) as error_pct
              from ( select to_char(time, 'Month DD, YYYY') as day,
                            status,
                            count(*) as occurance
                       from log
                       group by day, status
                       order by day, occurance desc ) as subq1
              group by day ) as subq
     where subq.error_pct > 1;
    """

    print('\nOn which days did more than 1% of requests lead to errors?\n')
    for row in do_query(db, query):
        print('\t{} -- {} errors'.format(row[0], row[1]))


if __name__ == '__main__':

    db = psycopg2.connect("dbname=news")

    most_popular_three_articles(db)
    most_popular_article_authors(db)
    daily_error_gt_1pct(db)

    db.close()
