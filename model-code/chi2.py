from sklearn.feature_selection import chi2
import pandas as pd
import sys
import time

filename = sys.argv[1]

test_data = pd.read_csv(filename, sep='\t')

features = test_data.drop('Class', axis=1).values
labels = test_data['Class'].values

if len(test_data['Class'].unique()) < 10:
    fs = chi2
else:
    print('Chi2 cannot be used with continuous data')
    sys.exit(1)

print(filename)
print('chi2')

start = time.time()

try:
    chi2, pval = fs(features, labels)
except:
    print('Chi2 cannot handle negative feature values')
    sys.exit(1)

elapsed = time.time() - start
print('Completed scoring in {} seconds.'.format(elapsed))

feature_importances = pd.DataFrame(data={'FeatureName': test_data.drop('Class', axis=1).columns.values,
                                         'FeatureImportance': chi2})

for i, row in feature_importances.sort_values('FeatureImportance', ascending=False).iterrows():
    print('{}\t{}'.format(row['FeatureName'], row['FeatureImportance']))
