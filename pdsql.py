import pandas as pd

def pdsql(SELECT, FROM, WHERE=None, ORDER_BY=None) -> pd.DataFrame:
    """
    Return dataframe with condition of SQL

    Parameters
    ----------
    SELECT : list of columns. ['*'] is all column
    FROM : source dataframe
    WHERE : list of where condition
    ORDER_BY : list of order by

    Returns
    -------
    queried result
"""

    if not isinstance(FROM, pd.DataFrame):
        print("'FROM' type should be Pandas Dataframe")
        return None
    
    FROM.columns = map(str.lower, FROM.columns)

    if(WHERE != None):
        if not isinstance(WHERE, list):
            print("'WHERE' type should be List")
            return None
        else:

            WHERE = [element.lower() for element in WHERE]

            _condition = []

            for i, _str in enumerate(WHERE):
            #    print("{} : {}".format(i,_str))

                # 순서가 중요. >=,<=가 나머지 보다 앞에 있어야 한다.
                _keyword =['or','and','>=', '<=', '!=', '>', '<', '=']
                _pair = {'or': '|', 'and': '&'}

                for key in _keyword:
                    if (_str.find(key)>=0):
                        cond = None
                        if(key != 'or' and key != 'and'):
                            cond = _str.split(key)
                            if (key =='='):
                                key='=='
                            cond.insert(1, key)
                            _condition.append("( FROM['" + cond[0].strip() + "']" + cond[1] + cond[2] + ") ") 
                        elif(key == 'or' or key == 'and') :
                            _condition.append(_pair[key] + " ")        
                        
                        break

            # print("".join(_condition))
            FROM = FROM.loc[eval("".join(_condition)),:]

    if(ORDER_BY!= None):
        if not isinstance(ORDER_BY, list):
            print("'ORDER_BY' type should be List")
            return None
        else:
            _sort = {'asc': 'True', 'desc': 'False'}

            # lowercase
            ORDER_BY = [element.lower() for element in ORDER_BY]
            # print(ORDER_BY)
            if(ORDER_BY[len(ORDER_BY)-1] in _sort):
                FROM = FROM.sort_values(by=ORDER_BY[:len(ORDER_BY)-1], ascending=eval(_sort[ORDER_BY[len(ORDER_BY)-1]]))
            else:
                FROM = FROM.sort_values(by=ORDER_BY[:len(ORDER_BY)], ascending=True)

    if not isinstance(SELECT, list):
        print("'SELECT' type should be List")
        return None
    else:
        SELECT = [element.lower() for element in SELECT]
        if(SELECT[0]=='*'):
            FROM = FROM
        else:
            FROM = FROM[SELECT]

            
    return FROM


if __name__ == '__main__':
    emp = pd.read_csv('emp.csv')

    result = pdsql(SELECT=['*'], FROM=emp)
    print(result)

    result = pdsql(SELECT=['ENAME'], FROM=emp)
    print(result)

    result = pdsql(SELECT=['ENAME','SAL'], FROM=emp)
    print(result)

    result = pdsql(SELECT=['*'], FROM=emp, WHERE=["sal > 1000", "and", "depno=30"])
    print(result)


    result = pdsql(SELECT=['*'], FROM=emp, WHERE=["sal > 1000", "and", "depno=30", "or", "job='SALESMAN'"])
    print(result)


    result = pdsql(SELECT=['*'], FROM=emp, WHERE=["sal > 1000", "and", "depno=30", "or", "job='SALESMAN'"], ORDER_BY=['job','sal','desc'])
    print(result)
