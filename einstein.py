def main():
    mass = int(input("Please write the mass in kilograms: "))
    #convert(mass)
    print("E: ",convert(mass))

def convert(mass):
    #E=mc*2
    energy = mass*(300000000**2)
    return energy

main()
