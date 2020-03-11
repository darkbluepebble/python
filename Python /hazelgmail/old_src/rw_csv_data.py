import csv
import datetime
import shutil
from tempfile import NamedTemporaryFile

def read_data(user_id=None, email=None) :
	filename="hazel_data.csv"
	with open(filename,"r") as csvfile:
		reader=csv.DictReader(csvfile)
		items=[]
		unknown_user_id=None
		unknown_email=None

		for row in reader:
			if user_id is not None :
				if int(user_id) == int(row.get("id")):
					return row
				else :
					unknown_user_id=user_id

			if email is not None :
				if email == row.get("email") :
					return row
				else :
					unknown_email=email

		if unknown_user_id is not None :
			print("User id {userid} not found".format(userid=user_id))
		if unknown_email is  not  None :
			print("User email {email} is not found".format(email=email))
	return None			

def get_length(file_path):
	with open(file_path,"r") as csvfile:
		reader=csv.reader(csvfile)
		reader_list=list(reader)
		return len(reader_list)

def append_data(file_path,name,email,amount) :
	fieldnames=['id','name','email','amount','sent','date']
	# the number of rows? # id eklemek için
	next_id=get_length(file_path)
	with open(file_path,"a") as csvfile: 
		writer=csv.DictWriter(csvfile,fieldnames=fieldnames)
		#writer.writeheader()
		writer.writerow({
			"id":next_id,
			"name":name,
			"email":email,
			"sent":"",
			"amount":amount,
			"date":datetime.datetime.now()
			})

def edit_data(edit_id=None, email=None, amount=None, sent=None):
    filename = "hazel_data.csv"
    temp_file = NamedTemporaryFile(delete=False)

    with open(filename, "r+") as csvfile, temp_file:
        reader = csv.DictReader(csvfile)
        fieldnames = ['id', 'name', 'email', 'amount', 'sent', 'date']
        writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            if edit_id is not None:
                if int(row.get('id')) == int(edit_id):
                    row['amount'] = amount
                    row['sent'] = sent
            elif email is not None and edit_id is None:
                if str(row['email']) == str(email):
                    row['amount'] = amount
                    row['sent'] = sent
            else:
                pass
            writer.writerow(row)
        
        shutil.move(temp_file.name, filename)
        return True
    return False

"""
def new_edit_data(new_data):
    filename = "hazel_data.csv"
    temp_file = NamedTemporaryFile(delete=False)

    with open(filename, "rb") as csvfile, temp_file:
        reader = csv.DictReader(csvfile)
        fieldnames = ['id', 'name', 'email', 'amount', 'sent', 'date']
        writer = csv.DictWriter(temp_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            if isinstance(new_data, dict):
                print(new_data)
                id_ = new_data.get("id", None)
                email_ = new_data.get("email", None)
                if id_ and int(row['id']) == int(id_):
                    for key, value in new_data.items():
                        if key in fieldnames:
                            row[key] = value
                elif str(row['email']) == str(email_) and not id_:
                    for key, value in new_data.items():
                        if key in fieldnames:
                            row[key] = value
            writer.writerow(row)
        
        shutil.move(temp_file.name, filename)
        return True
    return False
"""


"""
append_data("hazel_data.csv","Hazel","hazelblake.98@gmail.com",123.32)
append_data("hazel_data.csv","Hazel2","hazelblake.98@gmail.com",123.32)
append_data("hazel_data.csv","Hazel3","hazelblake.98@gmail.com",123.32)
append_data("hazel_data.csv","Hazel4","hazelblake.98@gmail.com",123.32)
append_data("hazel_data.csv","Hazel5","hazelblake.98@gmail.com",123.32)
"""

#edit_data(edit_id='6',email='',amount='12345' ,sent='')

edit_data(edit_id='',email='hazelblake.98@gmail.com', amount=99.99, sent='')

#new_edit_data({"amount": 231, "email": "hello@teamcfe.com", "sent": "adsd", "house": "NOne"})

#read_data(user_id="4",email="")









