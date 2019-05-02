def currency_converter(rate_e, rate_d, euros, dollars):
    hryvnas = rate_e * euros + rate_d * dollars
    return hryvnas

re = float(input("Enter rate for euro: \n"))
rd = float(input("Enter rate for dollars: \n"))
e = float(input("Enter euros: \n"))
d = float(input("Enter dollars: \n"))
print("The total amount UAH: " + str(currency_converter(d,e,re,rd)))
