
# read the csv file
import pandas as pd
from icecream import ic


# df as a verbule that holds diamons data
df = pd.read_csv('diamons_data.csv') 

# misson 1
highest_diamond = df['price'].max()
ic(highest_diamond)


# misson 2
average_diamond_price = df['price'].mean() 
ic(average_diamond_price)

# # misson 3
ideal_type_diamonds = df[df['cut'] == 'Ideal'].shape[0] 
ic(ideal_type_diamonds)

# misson 4
num_diamont_colors = df['color'].nunique()
ic(num_diamont_colors)

# misson 5
median_carat_premium = df[df['cut'] == 'Premium']['carat'].median()
ic(median_carat_premium)

# misson 6
average_carat_per_cut = df.groupby('cut')['carat'].mean()
print("average is: ")
ic(average_carat_per_cut)

# misson 7
average_price_per_color = df.groupby('color')['price'].mean()
print("Price average: ")
ic(average_price_per_color)