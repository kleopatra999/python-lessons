for i in [1,2,3]:
    if i > 9:
        break
    # code
    pass
else:
    # wenn kein break vorkommt

for i in (1,2,3):
    # code
    pass

for i in {1:"value1", 2:"value2"}:
    # iteration über die keys
    pass


for i in {1:"value1", 2:"value2"}.items():
    # i ist tuple von (key, value)
    pass

for value1, value2 in [
        (1, "werner"),
        (3, "geh mal in den keller"),
        (42, "ich glaub die russen kommen")
    ]:
    # iteration mit tuple unpacking
    # code

for key, value in {1:"value1", 2:"value2"}.items():
    # iteration über keys und values mit tuple unpacking
    pass