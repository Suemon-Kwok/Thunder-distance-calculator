def calculate_distance():
    while True:
        T = float(input("Enter the temperature in Celsius: "))
        v = 331 + (0.61 * T)
        t = float(input("Enter the time in seconds: "))
        d = v * t
        print(f"The distance the thunder is traveling is {d} meters.")
        
        repeat = input("Do you want to calculate again? (yes/no): ")
        if repeat.lower() != "yes":
            break

calculate_distance()

