import phonenumbers 
from phonenumbers import carrier 
from phonenumbers import geocoder 
phone_number = phonenumbers.parse(str(input("Enter your phone number with country code: ")))  
yourLocation = geocoder.description_for_number(phone_number,"en")
print(("location : "+yourLocation))
yourServiceProvider = carrier.name_for_number(phone_number,"en")
print(("service provider : "+yourServiceProvider))

