def make_string(x,y,z):
    return ("{}時の{}は{}").format(x,y,z)

print(make_string(12,"気温", 22.4))


from string import Template

def string_temp(x,y,z):
    string = Template("$hour時の$sthは$val")
    cont = {"hour":x,"sth":y,"val":z}
    return string.substitute(cont)

print(string_temp(12,"気温", 22.4))