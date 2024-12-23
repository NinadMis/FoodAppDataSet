import pandas as pd

df = pd.read_csv('/Users/ninadmishra/Downloads/FoodAppDataSet.csv')
#print(df)

#seperating city initials from Delivery Person IDs
df['City_Initial']= df['Delivery_person_ID'].str[:3]
#print(df)

cities =  df['City_Initial'].drop_duplicates()
df1 = pd.DataFrame(cities)
#print(df1)

#df1.to_csv('/Users/ninadmishra/Downloads/Dataset_Cities.csv')

#mapping of city initials and names
citi_data = {
    'City_Initial':['DEH','KOC','PUN','LUD','KNP','MUM','MYS','HYD','KOL','RAN','COI','CHE','JAP','SUR','BAN','GOA','AUR','AGR','VAD','ALH','BHP','IND'],
    'City_Name':['Delhi','Kochi','Pune','Ludhiana','Kanpur','Mumbai','Mysore','Hyderabad','Kolkata','Ranchi','Coimbatore','Chennai','Jaipur','Surat','Bangalore','Goa','Aurangabad','Agra','Vadodra','Alhabad','Bhopal','Indore']
    }

df2 = pd.DataFrame(citi_data)
#print(df2)

#merging mapping with og data frame
if 'City_Initial' in df.columns and 'City_Initial' in df2.columns:
    zd = pd.merge(df, df2, on = 'City_Initial')
    #print(zd)

else: print("column'City_Initial' not found")

#changing date format
zd['Order_Date']= pd.to_datetime(zd['Order_Date'], format='mixed')
zd['Order_Date']


#fixing wrong latitude and longitudes by merging with another df and rmoving excess coloumns
df3 = pd.read_csv('/Users/ninadmishra/Downloads/in.csv')
if 'City_Name' in zd.columns and 'city' in df3.columns:
    zd1 = pd.merge(zd, df3, left_on= 'City_Name' , right_on= 'city' , how='left')
    zd2 = zd1.drop(['city','country','iso2','admin_name','capital','population','population_proper','Restaurant_latitude','Restaurant_longitude','Delivery_location_latitude','Delivery_location_longitude'], axis=1)
else: print('City Name not found')

#Changing coloumn names from shortform to fullforms
zd2 = zd2.rename(columns={'lat':'Latitude',
                          'lng':'Longitude'})
zd2.to_csv('/Users/ninadmishra/Downloads/FoodAppDataSet_Updated.csv')