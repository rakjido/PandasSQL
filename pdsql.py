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
    
    if(WHERE != None):
        if not isinstance(WHERE, list):
            print("'WHERE' type should be List")
            return None
        else:

            # 순서가 중요. >=,<=가 나머지 보다 앞에 있어야 한다.
            _keyword =['>=', '<=', '>', '<', '=']

            for key in _keyword:
            #    print(WHERE[0].find(key))
                if (WHERE[0].find(key)>0):
                    cond = None
                    cond=WHERE[0].split(key)
                    if (key =='='):
                        key='=='
                    cond.insert(1, key)
                    print("FROM['" + cond[0].strip() + "']" + cond[1] + cond[2])
                    filter1 = eval("FROM['" + cond[0].strip() + "']" + cond[1] + cond[2])
                    
                    FROM = FROM.loc[filter1,:]
                    break

    if not isinstance(SELECT, list):
        print("'SELECT' type should be List")
        return None
    else:
        if(SELECT[0]=='*'):
            FROM = FROM
        else:
            FROM = FROM[SELECT]

            
    return FROM
