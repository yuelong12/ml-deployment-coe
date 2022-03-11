# import necessary packages
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# read datasets
df_sample_customer = pd.read_csv(r'C:\Users\ZihaoYan\Downloads\API_Deploy\Data\sample_customer.csv',index_col=[0])
df_sample_product = pd.read_csv(r'C:\Users\ZihaoYan\Downloads\API_Deploy\Data\sample_product.csv',index_col=[0])
df_sample_tlog = pd.read_csv(r'C:\Users\ZihaoYan\Downloads\API_Deploy\Data\sample_tlog.csv',index_col=[0])

# combined three datasets
df_combined = df_sample_tlog.merge(df_sample_customer, on='customer_id', how='inner').merge(df_sample_product, on='upc_no', how='inner')

# label encoding
le = preprocessing.LabelEncoder()
df_combined['convenience_dim_seg'] = le.fit_transform(df_combined['convenience_dim_seg'])
df_combined['quality_dim_seg'] = le.fit_transform(df_combined['quality_dim_seg'])
df_combined['health_dim_seg'] = le.fit_transform(df_combined['health_dim_seg'])
df_combined['price_dim_seg'] = le.fit_transform(df_combined['price_dim_seg'])

# drop empty values
df_combined.dropna(inplace=True)

# select variables
X = df_combined[['purchase_unit', 'sales_amt']]
y = df_combined['purchase_price']

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25)

# initiate linear regression model
regr = LinearRegression()

# train the model
regr.fit(X_train, y_train)
print(regr.score(X_test, y_test))

# saving the pipeline
from joblib import dump
dump(regr, 'regression_model.joblib')