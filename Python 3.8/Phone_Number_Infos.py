import phonenumbers
from phonenumbers import geocoder, timezone,carrier

num = input("Please write the phone number with the prefix which you want infos: ")
c_num = phonenumbers.parse(num, "CH" )
print("City: ",geocoder.description_for_number(c_num,"en"))
# Pass the parsed phone number in below function
timeZone = timezone.time_zones_for_number(c_num)
# It print the timezone of a phonenumber
print("Time zone: ",timeZone)

ro_num = phonenumbers.parse(num, "RO" )
# Getting carrier of a phone number

Car = carrier.name_for_number(ro_num, 'en')

if not Car:
    print("Sadly the carrie's infos are not available ")
else:
    print(Car)


