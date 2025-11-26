#Create a dictionary with country codes as key and their population in millions as the value
popData = {
    'US': 340.1, 'CA': 41.29, 'MX': 130.9, 'BR': 212.0, 'UK': 69.23, 'FR': 68.52, 'DE': 83.51, 'JP': 124.0, 'IN': 1451.0,
    'CN': 1409.0, 'NG': 232.7, 'ZA': 64.01, 'AU': 27.2}

#Function to retrieve the population
def retrieve_pop(country_code, data_dict):

    if country_code in data_dict:
        return data_dict[country_code]
    else:
        return None

#Main function
def main():

    valid_codes = list(popData.keys())

    while True:

            #Prompt for user input (convert lowercase to upper and remove extra white space
            user_input = input('Please enter a country code: ').strip().upper()

            population = retrieve_pop(user_input, popData)

            if population is not None:
                #If code found, display result and exit
                print(f'{user_input} population = {population}')
                break
            else:
                #If code not found display error and show hints
                valid_codes_str = ', '.join(valid_codes)
                print(f"Error: '{user_input}' not recognized. Valid codes: {valid_codes_str}")

                    #Ask user if they would like to try again
                try_again = input('Would you like to try again? (yes/no): ').strip().lower()

                if try_again in ['no']:
                    print('Program terminated.')

                    break

                elif try_again not in ['yes']:
                    print("Invalid input. Please enter 'yes' or 'no'.")
                    break

#Call the main function
if __name__ == "__main__":
    main()