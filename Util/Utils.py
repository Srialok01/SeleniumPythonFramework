import inspect

URL="https://demo.nopcommerce.com/"

Email = "aloksri2204@gmail.com"
Password = "Test123"


# WhoAmI function returns the name of function called
def whoami():
    return inspect.stack()[1][3]


# Card details
CardHolderName = "Alok Srivastava"
CardNo = "6331101999990016"
cvv = "123"

# Address details

dict_address = {'First_Name': "Alok",
                'Last_Name': "Srivastava",
                'Guest_Email': "abc@gmail.com",
                'City': "Pune",
                'Address1': "Kharadi",
                'PostCode': "411014",
                'PhoneNo': "9415862204"
                }
