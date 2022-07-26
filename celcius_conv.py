while True:
    #Input
    suhu = float(input("Masukan Nilai Suhu Dalam °C : "))
        
    #Processing
    reamur = 4/5 * suhu #Rumus Reamur
    fahrenheit = (9/5 * suhu) + 32 #Rumus Fahrenheit
    kelvin = suhu + 273.15 #Rumus Kelvin
    
    #Output
    print("-->", reamur, "°R")
    print("-->", fahrenheit, "°F")
    print("-->", kelvin, "K")
    if input("Keluar Program? {Y}: ") == "Y":
        break