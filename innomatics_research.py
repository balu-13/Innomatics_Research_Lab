import pandas as pd
df = pd.read_csv("C://Users//gatla//Downloads//final_food_delivery_dataset.csv")
df['order_date']=pd.to_datetime(df['order_date'], dayfirst=True)
gold_df=df[df['membership']=='Gold']
top_city_gold_rev=gold_df.groupby('city')['total_amount'].sum().idxmax()
highest_aov_cuisine=df.groupby('cuisine')['total_amount'].mean().idxmax()
user_spend=df.groupby('user_id')['total_amount'].sum()
users_above_1000=(user_spend>1000).sum()
rev_40_45=df[(df['rating']>=4.0)&(df['rating']<4.5)]['total_amount'].sum()
rev_45_50=df[(df['rating']>=4.5)&(df['rating']<=5.0)]['total_amount'].sum()
top_rating_range="4.5-5.0" if rev_45_50>rev_40_45 else "4.0-4.5"
top_aov_city_gold=gold_df.groupby('city')['total_amount'].mean().idxmax()
cuisine_counts=df.groupby('cuisine')['restaurant_id'].nunique()
lowest_res_cuisine=cuisine_counts.idxmin()
gold_order_pct=round((len(gold_df)/len(df))*100)
res_stats=df.groupby('order_restaurant_name').agg(count=('order_id','count'),aov=('total_amount','mean'))
top_res_low_vol=res_stats[res_stats['count']<20]['aov'].idxmax()
best_comb=df.groupby(['membership','cuisine'])['total_amount'].sum().idxmax()
df['quarter']=df['order_date'].dt.quarter
top_quarter=f"Q{df.groupby('quarter')['total_amount'].sum().idxmax()}"

print(f"Top Revenue City (Gold Members)={top_city_gold_rev}")
print(f"Highest AOV Cuisine={highest_aov_cuisine}")
print(f"Distinct Users Spending > 1000={users_above_1000}")
print(f"Highest Revenue Rating Range={top_rating_range}")
print(f"Top AOV City (Gold Members)={top_aov_city_gold}")
print(f"Cuisine with Fewest Restaurants={lowest_res_cuisine}")
print(f"Gold Member Order Percentage={gold_order_pct}%")
print(f"Highest AOV Restaurant (<20 orders)={top_res_low_vol}")
print(f"Highest Revenue Combination={best_comb[0]} + {best_comb[1]}")
print(f"Highest Revenue Quarter={top_quarter}")


total_gold_orders=len(gold_df)
hyd_rev=round(df[df['city']=='Hyderabad']['total_amount'].sum())
distinct_users=df['user_id'].nunique()
gold_aov=round(gold_df['total_amount'].mean(),2)
rating_45_plus_count=len(df[df['rating']>=4.5])
top_gold_city_orders=len(gold_df[gold_df['city']=='Chennai'])

print(f"Total Gold Orders={total_gold_orders}")
print(f"Hyderabad Total Revenue={hyd_rev}")
print(f"Total Distinct Users={distinct_users}")
print(f"Average Order Value (Gold)={gold_aov}")
print(f"Orders with Rating >= 4.5={rating_45_plus_count}")
print(f"Gold Orders in Chennai={top_gold_city_orders}")