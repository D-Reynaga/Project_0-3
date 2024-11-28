def display_menu():
    print("********************************")
    print("AutoCountry Vehicle Finder v0.3")
    print("********************************")
    print("Please Enter the following number below from the following menu:")
    print("1. PRINT all Authorized Vehicles")
    print("2. SEARCH for Authorized Vehicle")
    print("3. ADD Authorized Vehicle")
    print("4. Exit")
    print("********************************")

def print_authorized_vehicles(allowed_vehicles_list):
    print("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles:")
    for vehicle in allowed_vehicles_list:
        print(vehicle)

def search_vehicle(allowed_vehicles_list, vehicle_name):
    if vehicle_name in allowed_vehicles_list:
        print(f"{vehicle_name} is an authorized vehicle")
    else:
        print(f"{vehicle_name} is not an authorized vehicle, if you received this in error please check the spelling and try again")

def add_authorized_vehicle(allowed_vehicles_list, vehicle_name):
    allowed_vehicles_list.append(vehicle_name)
    print(f'You have added "{vehicle_name}" as an authorized vehicle')

def main():
    allowed_vehicles_list = ['Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan']
    
    while True:
        display_menu()
        user_input = input()

        if user_input == '1':
            print_authorized_vehicles(allowed_vehicles_list)
        elif user_input == '2':
            vehicle_name = input("Please enter the full Vehicle name: ")
            search_vehicle(allowed_vehicles_list, vehicle_name)
        elif user_input == '3':
            vehicle_name = input("Please enter the full Vehicle name you would like to add: ")
            add_authorized_vehicle(allowed_vehicles_list, vehicle_name)
        elif user_input == '4':
            print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
            break
        else:
            print("Invalid input, please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
