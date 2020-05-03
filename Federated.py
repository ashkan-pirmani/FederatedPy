import pandas as pd
df = pd.read_csv("./Data/example_data.csv")

### Suspected COVID19 ( symptoms)

patients_with_covid19 = df.loc[((df.covid19_has_symptoms=="yes") | (df.covid19_suspected_case == "yes"))]["secret_name"]
print(f"Number of patients with covid : {patients_with_covid19.shape[0]}")

patients_confirmed = df.loc[df.covid19_confirmed_case=="yes"]
print(f"Number of CONFIRMED patients with covid : {patients_confirmed.shape[0]}")

### Type of MS

print("Number of patients per MS Type : ")
print(df.groupby("ms_type").count()["secret_name"])

### Number of different countries

unique_countries = df["covid19_country"].nunique()
print(f"Number of unique countries : {unique_countries}")
print("Number of patients per country : ")
print(df.groupby("covid19_country").count()["secret_name"])

### Counts of patients ( treated - non treated - never treated)
print("Counts of patients : ")
print(df.groupby("current_dmt")["secret_name"].count())

### Subset of treated patients

print("Subset of treated patients : ")
current_dmt = df.loc[df.current_dmt=="yes"].groupby("type_dmt").count().copy()

print(current_dmt.sort_values("current_dmt",ascending=False)["secret_name"])

import matplotlib.pyplot as plt

labels = current_dmt.index
sizes = current_dmt.current_dmt.values
#colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
plt.pie(sizes, shadow=True, autopct='%1.1f%%', startangle=90)
plt.legend( labels, bbox_to_anchor=(0.8, 1.05))
plt.axis('equal')
plt.tight_layout()
plt.title("Repartition of patients currently treated")
plt.savefig('Repartition of patients currently treated.pdf')
plt.show(block=True)

### Subset of previously treated patients

print("Subset of previously treated patients : ")
last_dmt = df.loc[df.current_dmt=="no"].groupby("type_dmt").count().copy() # no is "no but was in the past"
print(last_dmt.sort_values("current_dmt",ascending=False)["secret_name"])

labels = last_dmt.index
sizes = last_dmt.current_dmt.values
#colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
plt.pie(sizes, shadow=True, autopct='%1.1f%%', startangle=90)
plt.legend( labels, bbox_to_anchor=(0.8, 1.05))
plt.axis('equal')
plt.tight_layout()
plt.title("Repartition of patients treated in the past but not currently treated")
plt.savefig("Repartition of patients treated in the past but not currently treated.pdf")
plt.show(block=True)
