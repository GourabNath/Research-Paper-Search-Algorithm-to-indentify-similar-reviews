# Importing python packages

import pandas as pd

# Importing mlxtend packages for sparse matrix & apriori

from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules

def apriori_func(noun_listoflist,maxlen):
    # Preparing the dataframe as list of list for the sparse matrix
    df_list = []
    for i in noun_list:
        for j in i:
            df_list.append(j.split(','))

    te = TransactionEncoder()
    te_ary1 = te.fit(noun_list).transform(noun_list)
    df1 = pd.DataFrame(te_ary1, columns=te.columns_)
    
    apr = apriori(df1, min_support=0.01, use_colnames=True, max_len=maxlen)
    sorted_apr = apr.sort_values(['support'], ascending=False)

    return sorted_apr