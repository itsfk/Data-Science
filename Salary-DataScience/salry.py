import pandas as pd
sal=pd.read_csv('Salaries.csv')
# print(sal.head())
# print(sal.info())
# print(sal["BasePay"].mean)
# print(sal["OvertimePay"].max())
# print(sal[sal['EmployeeName']=='JOSEPH DRISCOLL']['JobTitle'])
# print(sal.loc[sal['TotalPayBenefits'].idxmax()])
# print(sal.groupby('Year').mean()['BasePay'])
# print(sal['JobTitle'].value_counts().head(5))
# print(sum(sal[sal['Year']==2013]['JobTitle'].value_counts() == 1))