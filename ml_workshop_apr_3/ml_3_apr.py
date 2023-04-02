# https://www.dataquest.io/blog/sci-kit-learn-tutorial/

from yellowbrick.classifier import ClassificationReport
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier

file_location = "WA_Fn-UseC_-Sales-Win-Loss.csv"
sales_data = pd.read_csv(file_location)
print(sales_data.head())
print(sales_data.head(n=2))
print(sales_data.tail())
print(sales_data.tail(n=2))
print(sales_data.dtypes)


sns.set(style="whitegrid", color_codes=True)
sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.countplot(x='Route To Market',data=sales_data,hue = 'Opportunity Result')
sns.despine(offset=10, trim=True)

plt.show()

sns.set(rc={'figure.figsize':(16.7,13.27)})
sns.violinplot(x="Opportunity Result", y="Client Size By Revenue",
               hue="Opportunity Result", data=sales_data)
plt.show()


le = preprocessing.LabelEncoder()
encoded_value = le.fit_transform(["paris", "paris", "tokyo", "amsterdam"])
print(encoded_value)


print("Supplies Subgroup' : ",sales_data['Supplies Subgroup'].unique())
print("Region : ",sales_data['Region'].unique())
print("Route To Market : ",sales_data['Route To Market'].unique())
print("Opportunity Result : ",sales_data['Opportunity Result'].unique())
print("Competitor Type : ",sales_data['Competitor Type'].unique())
print("'Supplies Group : ",sales_data['Supplies Group'].unique())


le = preprocessing.LabelEncoder()
sales_data['Supplies Subgroup'] = le.fit_transform(
    sales_data['Supplies Subgroup'])
sales_data['Region'] = le.fit_transform(sales_data['Region'])
sales_data['Route To Market'] = le.fit_transform(sales_data['Route To Market'])
sales_data['Opportunity Result'] = le.fit_transform(
    sales_data['Opportunity Result'])
sales_data['Competitor Type'] = le.fit_transform(sales_data['Competitor Type'])
sales_data['Supplies Group'] = le.fit_transform(sales_data['Supplies Group'])

print(sales_data.head())


cols = [col for col in sales_data.columns if col not in [
    'Opportunity Number', 'Opportunity Result']]
data = sales_data[cols]
target = sales_data['Opportunity Result']

print(data.head())
print(target.head())

data_train, data_test, target_train, target_test = train_test_split(
    data,target, test_size = 0.30, random_state = 10)


gnb = GaussianNB()
pred = gnb.fit(data_train, target_train).predict(data_test)
print("Naive-Bayes accuracy : ",accuracy_score(target_test, pred, normalize = True))


svc_model = LinearSVC(random_state=0)
pred = svc_model.fit(data_train, target_train).predict(data_test)
print("LinearSVC accuracy : ",accuracy_score(target_test, pred, normalize = True))


neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(data_train, target_train)
pred = neigh.predict(data_test)
print ("KNeighbors accuracy score : ",accuracy_score(target_test, pred))

visualizer = ClassificationReport(gnb, classes=['Won', 'Loss'])
visualizer.fit(data_train, target_train)
visualizer.score(data_test, target_test)  
g = visualizer.poof() 

visualizer = ClassificationReport(svc_model, classes=['Won', 'Loss'])
visualizer.fit(data_train, target_train)
visualizer.score(data_test, target_test) 
g = visualizer.poof() 


visualizer = ClassificationReport(neigh, classes=['Won', 'Loss'])
visualizer.fit(data_train, target_train)
visualizer.score(data_test, target_test)
g = visualizer.poof()
