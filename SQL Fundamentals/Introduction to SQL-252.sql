## 3. Your First Query ##

Select *
    FROM recent_grads

## 4. Understanding your First Query ##

SELECT * 
  FROM recent_grads;
select *
  from recent_grads

## 6. The LIMIT Clause ##

select *
    from recent_grads
limit 5;

## 7. Selecting Specific Columns ##

SELECT Major, ShareWomen
    FROM recent_grads;

## 8. Filtering Rows Using WHERE ##

SELECT Major, ShareWomen
FROM recent_grads
WHERE ShareWomen < 0.5

## 9. Expressing Multiple Filter Criteria Using 'AND' ##

SELECT Major, Major_category, Median, ShareWomen
FROM recent_grads
WHERE ShareWomen>0.5
AND Median>50000

## 10. Returning One of Several Conditions With OR ##

SELECT Major, Median, Unemployed
FROM recent_grads
WHERE Median>=10000
OR Men>Women
LIMIT 20

## 11. Grouping Operators With Parentheses ##

SELECT Major, Major_category, ShareWomen, Unemployment_rate
FROM  recent_grads
WHERE (Major_category = 'Engineering')
AND (ShareWomen>0.5 OR Unemployment_rate<0.051)

## 12. Ordering Results Using ORDER BY ##

select Major, ShareWomen, Unemployment_rate
from recent_grads
where ShareWomen>0.3 and Unemployment_rate<0.1
order by ShareWomen DESC

## 13. Practice Writing a Query ##

select Major_category, Major, Unemployment_rate
from recent_grads
where Major_category="Engineering" or Major_category="Physical Sciences"
order by Unemployment_rate