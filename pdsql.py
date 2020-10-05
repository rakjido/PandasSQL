

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
            cond = None
            cond = WHERE[0].split('>')
            cond.insert(1,'>')
            filter1 = eval("FROM['" + cond[0].strip() + "']" + cond[1] + cond[2])
            FROM = FROM.loc[filter1,:]

    if not isinstance(SELECT, list):
        print("'SELECT' type should be List")
        return None
    else:
        if(SELECT[0]=='*'):
            FROM = FROM
        else:
            FROM = FROM[SELECT]

            
    return FROM
