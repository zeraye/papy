import re
def num_from_val(value):
    return int("".join(re.findall("[-\d]", value)))

print(type(num_from_val("INTEGER(-35)")))
print(num_from_val("35"))
print(num_from_val("3a5"))
