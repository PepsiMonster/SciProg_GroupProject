def transfrom(meter,santimeter):
    millimeter = meter*1000 + santimeter*10
    return millimeter
meter = int(input())
santimeter = int(input())
value = transfrom(meter,santimeter)