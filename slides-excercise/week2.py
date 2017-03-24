#For the purchase records from the pet store, how would you get a list of all items
#which had been purchased (regardless of where they might have been
#purchased, or by whom)?
import pandas as pd

purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame(
    [purchase_1, purchase_2, purchase_3],
    index=['Store 1', 'Store 1', 'Store 2']
)
# Your code here
# print(df['Item Purchased'])


#For the purchase records from the pet store, how would you update the DataFrame,
#applying a discount of 20% across all the values in the 'Cost' column?

purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])


# Your answer here
df['Cost'] *= 0.8
# print(df)

#Reindex the purchase records DataFrame to be indexed hierarchically, first by store, then by person. Name these #
# indexes 'Location' and 'Name'. Then add a new entry to it with the value of:
#<p>Name: 'Kevyn', Item Purchased: 'Kitty Food', Cost: 3.00 Location: 'Store 2'.</p>

purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})

df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])

df = df.reset_index()
df.columns = ['Location', 'Name', 'Item Purchased', 'Cost']
df = df.set_index(['Location', 'Name'])
# Your answer here
df2 = pd.DataFrame([['Store 2', 'Kevyn','Kitty Food', 3.0]], columns = ['Location', 'Name', 'Item Purchased', 'Cost'])
# TODO find a better way to set index and value
df2 = df2.set_index(['Location', 'Name'])
df = df.append(df2)
print(df)