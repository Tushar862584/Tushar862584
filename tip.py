def main():
    dollar = dollar_in_float (input("How much was meal ?"))
    percent = percent_in_float (input("enter tip"))
    tip = dollar * percent
    print(f"leave ${tip:.2f}")
def dollar_in_float(d):
    d1 = d.replace("$","")
    return float(d1)
def percent_in_float(p):
    p1 = p.replace("%","")
    p2 = float(p1) / 100
    return (p2)



main()

