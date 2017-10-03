from skrebate import ReliefFPercent
import pandas as pd
import sys

filename = sys.argv[1]

test_data = pd.read_csv(filename, sep='\t')

features = test_data.drop('Class', axis=1).values
labels = test_data['Class'].values

fs = ReliefFPercent(percent_neighbors=0.382, verbose=True)

print(filename)
print(fs)

fs.fit(features, labels)

feature_importances = pd.DataFrame(data={'FeatureName': test_data.drop('Class', axis=1).columns.values,
                                         'FeatureImportance': fs.feature_importances_})

for i, row in feature_importances.sort_values('FeatureImportance', ascending=False).iterrows():
    print('{}\t{}'.format(row['FeatureName'], row['FeatureImportance']))
