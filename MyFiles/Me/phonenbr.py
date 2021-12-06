import phonenumbers
from phonenumbers import carrier, timezone, geocoder

x = phonenumbers.parse("0032498304445", "BE")
x=phonenumbers.parse("0498304445", "BE")

#x="0032498304445"

print(phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.NATIONAL))
print(phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.INTERNATIONAL))
print(phonenumbers.format_number(x, phonenumbers.PhoneNumberFormat.E164))