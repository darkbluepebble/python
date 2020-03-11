import datetime

class MessageUser():
    user_details=[]
    messages=[]
    email_messages=[]
    base_message="""" Hi {name}!
Thank you for the purchase on {date}.
We hope you are exicted about using it. Just as a
reminder the purchase total was ${total}.
Have a great one!

Team DBP
"""
    def add_user(self,name,amount,email=None ):
        name=name[0].upper()+name[1:].lower()
        amount="%.2f"%(amount)
        detail={
            "name":name,
            "amount":amount,
            }
        
        today=datetime.date.today()
        date_text="{today.month}/{today.day}/{today.year}".format(today=today)
        detail['date']=date_text
        if email is not None: #if email != None
            detail["email"]=email
        self.user_details.append(detail)
        
    def get_details(self):
        return self.user_details
    
    def make_messages(self):
        if len(self.user_details) > 0 :
            for detail in self.get_details() :
                name=detail["name"]
                amount=detail["amount"]
                date=detail["date"]
                message=self.base_message
                new_msg=message.format( #update messages
                    name=name,
                    date=date,
                    total=amount
                )
                user_email=detail.get("email")
                if user_email :
                    user_data={
                        "email":user_email,
                        "message":new_msg
                    }
                    self.email_messages.append(user_data)
                else :
                    self.messages.append(new_msg)

            return self.messages
        return []

    def send_email(self) :
        self.make_messages()

        if(len(self.email_messages) >0) :
            for detail in self.email_messages :
                user_email=detail['email']
                user_message=detail['message']
                # run email 

            return True
        return False
                
            
obj=MessageUser()
obj.add_user("Justin",123.32,'hello@teamcpe.com')
obj.add_user("jOhn",94.23)
obj.add_user("EmiLee",93.23)
obj.add_user("JiM",193.23)
obj.add_user("Ron",13.32)

obj.get_details()

print(obj.make_messages())
