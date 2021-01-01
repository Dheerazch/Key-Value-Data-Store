import data_store as d
d.access.create("Dheeraz",15)#data successfully stored
d.access.create("Neeraz",66)#data successfully stored
d.access.create("Mahesh",21)#data successfully stored
d.access.create("Sarath",86,3600)# data stored with time to live property given value is in sec
d.access.create("Dheeraz",75)#raise error:key already stored
d.access.read("Dheeraz")#it gives the value in Jasonobject format 'key-value'
d.access.read("Mahesh")#it gives the value in Jasonobject format if time to live property is not expired
d.access.delete("Sarath")#deleting the key and its value from database
d.access.delete("Eshwar")#raise error: given key doesn't exist in the database


#output
#data successfully stored
#data successfully stored
#data successfully stored
#data successfully stored
#raise error:key already stored
#Dheeraz-15
#Sarath-86
#key is successfully deleted
#raise error: given key doesn't exist in the database
