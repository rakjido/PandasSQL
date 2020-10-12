import pandas as pd
from pandasql import sqldf
dfsql = lambda q: sqldf(q, globals())


emp = pd.read_csv('emp.csv')
dept = pd.read_csv("dept.csv")

# print(globals())


print(dfsql("select * from emp"))

print(dfsql("select * from emp where sal > 2000"))

print(dfsql("select * from emp where mgr = '7839' order by sal asc"))

print(dfsql("select ename, job, mgr, sal from emp where sal > 2000 order by sal desc, ename asc"))

print(dfsql("""
                select e.job, sum(sal) as sum_sal, avg(sal) as avg_sal, max(sal) as max_sal, min(sal) as min_sal
                from emp e inner join dept d 
                on e.depno = d.deptno
                where d.loc='DALLAS'
                group by e.job
                order by e.job desc
            """))


dfsql("""
                select e.job, sum(sal) as sum_sal, avg(sal) as avg_sal, max(sal) as max_sal, min(sal) as min_sal
                from emp e inner join dept d 
                on e.depno = d.deptno
                where d.loc='DALLAS'
                group by e.job
                order by e.job desc
            """).to_json('sal_job.json', orient='table')