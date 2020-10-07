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
            _condition = []

            for i, _str in enumerate(WHERE):
            #    print("{} : {}".format(i,_str))

                # 순서가 중요. >=,<=가 나머지 보다 앞에 있어야 한다.
                _keyword =['or','and','>=', '<=', '>', '<', '=']
                _pair = {'or': '|', 'and': '&'}

                for key in _keyword:
                    if (_str.lower().find(key)>=0):
                        cond = None
                        if(key != 'or' and key != 'and'):
                            cond = _str.lower().split(key)
                            if (key =='='):
                                key='=='
                            cond.insert(1, key)
                            _condition.append("( FROM['" + cond[0].strip() + "']" + cond[1] + cond[2] + ") ") 
                        elif(key == 'or' or key == 'and') :
                            _condition.append(_pair[key.lower()] + " ")        

                        break

            print("".join(_condition))
            FROM = FROM.loc[eval("".join(_condition)),:]

    if not isinstance(SELECT, list):
        print("'SELECT' type should be List")
        return None
    else:
        if(SELECT[0]=='*'):
            FROM = FROM
        else:
            FROM = FROM[SELECT]

            
    return FROM

