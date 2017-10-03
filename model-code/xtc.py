from sklearn.ensemble import ExtraTreesClassifier, ExtraTreesRegressor
import pandas as pd
import sys
import time

filename = sys.argv[1]

test_data = pd.read_csv(filename, sep='\t')

features = test_data.drop('Class', axis=1).values
labels = test_data['Class'].values

if len(test_data['Class'].unique()) < 10:
    fs = ExtraTreesClassifier(n_estimators=500)
else:
    fs = ExtraTreesRegressor(n_estimators=500)

print(filename)
print('ExtraTrees')

start = time.time()

fs.fit(features, labels)

elapsed = time.time() - start
print('Completed scoring in {} seconds.'.format(elapsed))

feature_importances = pd.DataFrame(data={'FeatureName': test_data.drop('Class', axis=1).columns.values,
                                         'FeatureImportance': fs.feature_importances_})

for i, row in feature_importances.sort_values('FeatureImportance', ascending=False).iterrows():
    print('{}\t{}'.format(row['FeatureName'], row['FeatureImportance']))
