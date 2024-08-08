# datematcher
This python code will help you to tag the date of your interest from different date formats present in a text it also provides the position of the dates in the text.

Usage:
  1. Download the date_matcher.py
  2. import date_matcher
  3. date_matcher.match_date("1993-10-20","I was born on 20th october 1993")
  
  out: 
    [(14, 31, '20th october 1993')]

Date_match require two inputs  
1. The date you want to look for, like "1993-10-20" i.e YYYY-MM-DD format in above example
2. Sentence in which you want to tag the date.
