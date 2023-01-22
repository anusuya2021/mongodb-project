#program to perform CRUD operations using MONGODB
import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["telephone"]
col = db["directory"]
ch=0
data={}
def add():
    na = input("Enter name of the person:")
    ph = int(input("Enter phone number:"))
    ad = input("Enter Address:")
    pla = input("Enter place:")
    pin = int(input("Enter pincode :"))
    data["name"] = na
    data["phone"]=ph
    data["address"] = ad
    data["place"]=pla
    data["pincode"] = pin
    x = col.insert_one(data)
    print("record inserted")
    return
def delete(u):
    k ={"phone":u}
    x=col.delete_one(k)
    print("record deleted")
    return
def retre():
    for x in col.find():
        print(x)
    return
def update():
    n1 = input("Enter the name of the record to be modified:")
    na = input("Enter name of the person:")
    ph = int(input("Enter phone number:"))
    ad = input("Enter Address:")
    pla = input("Enter place:")
    pin = int(input("Enter pincode :"))
    myquery = { "name":n1  }
    newvalues = { "$set": { "name": na } }
    col.update_one(myquery, newvalues)
    newvalues = { "$set": { "phone": ph } }
    col.update_one(myquery, newvalues)
    newvalues = { "$set": { "address": ad } }
    col.update_one(myquery, newvalues)
    newvalues = { "$set": { "place": pla } }
    col.update_one(myquery, newvalues)
    newvalues = { "$set": { "pincode": pin } }
    col.update_one(myquery, newvalues)
    for x in col.find():
      print(x)
    return
while(ch!=5):
    print(" 1. Add \n 2. Delete \n 3. Retrieve \n 4. Update \n 5. Exit")
    ch = int(input("Enter your choice:"))
    if ch==1:
        add()
    elif ch==2:
        u = int(input("Enter phone no of record to be deleted"))
        delete(u)
    elif ch==3:
        retre()
    elif ch==4:
        update()
    elif ch== 5:
        print("Thank You! See you again.")
        break
    
    else:
        print("Incorrect Choice. Please, try again.")


    
    
