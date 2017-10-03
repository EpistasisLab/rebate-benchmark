from sklearn.feature_selection import f_classif, f_regression
import pandas as pd
import sys
import time

filename = sys.argv[1]

test_data = pd.read_csv(filename, sep='\t')

features = test_data.drop('Class', axis=1).values
labels = test_data['Class'].values

if len(test_data['Class'].unique()) < 10:
    fs = f_classif
else:
    fs = f_regression

print(filename)
print('ANOVAFValue')

start = time.time()

fval, pval = fs(features, labels)

elapsed = time.time() - start
print('Completed scoring in {} seconds.'.format(elapsed))

feature_importances = pd.DataFrame(data={'FeatureName': test_data.drop('Class', axis=1).columns.values,
                                         'FeatureImportance': fval})

for i, row in feature_importances.sort_values('FeatureImportance', ascending=False).iterrows():
    print('{}\t{}'.format(row['FeatureName'], row['FeatureImportance']))
