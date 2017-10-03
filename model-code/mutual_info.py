from sklearn.feature_selection import mutual_info_classif, mutual_info_regression
import pandas as pd
import sys
import time

filename = sys.argv[1]

test_data = pd.read_csv(filename, sep='\t')

features = test_data.drop('Class', axis=1).values.astype(float)
labels = test_data['Class'].values.astype(float)

if len(test_data['Class'].unique()) < 10:
    fs = mutual_info_classif
else:
    fs = mutual_info_regression

print(filename)
print('MutualInformation')

start = time.time()

mi = fs(features, labels)

elapsed = time.time() - start
print('Completed scoring in {} seconds.'.format(elapsed))

feature_importances = pd.DataFrame(data={'FeatureName': test_data.drop('Class', axis=1).columns.values,
                                         'FeatureImportance': mi})

for i, row in feature_importances.sort_values('FeatureImportance', ascending=False).iterrows():
    print('{}\t{}'.format(row['FeatureName'], row['FeatureImportance']))
