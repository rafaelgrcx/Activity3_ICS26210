import requests

user_database = {
    'martha': 'user11',
    'rain': 'user22',
    'rafael': 'user33',
    'gerard': 'user44',
    'andrew': 'user55'
}

def login():
    # Get user input for username and password
    username_input = input('Enter your username: ')
    password_input = input('Enter your password: ')

    # Check login credentials
    if username_input in user_database and user_database[username_input] == password_input:
        print(f'Login successful. Welcome, {username_input}!\n')
        return True
    else:
        print('Login failed. Please check your credentials.\n')
        return False
        
def get_public_ip_info():
    try:
        #user authentication
        if login():
            # Request geolocation information from the ipinfo.io API
            response = requests.get('https://ipinfo.io/json')
            ipstack_api_key = 'YOUR_IPSTACK_API_KEY'  # Replace with your actual IPStack API key

            #check if the HTTP response status code is successful (200)
            if response.status_code == 200:
                data = response.json()

                #extract and print ipv4 address
                print(f'Public IPv4 Address: {data["ip"]}')

                #check and print if ipv6 is available
                if 'ip6' in data:
                    print(f'Public IPv6 Address: {data["ip6"]}')
                else:
                    print('IPv6 Address not available')

                #extract and print detailed geolocation information
                loc = data.get("loc", "").split(",")
                latitude = loc[0] if loc else "N/A"
                longitude = loc[1] if len(loc) > 1 else "N/A"
                print(f'Latitude: {latitude}')
                print(f'Longitude: {longitude}')
                print(f'Geolocation: {data["city"]}, {data["region"]}, {data["country"]}')

                # Get continent information from ipstack.com
                continent = get_continent_info(data["ip"], ipstack_api_key)
                print(f'Continent: {continent}')

                print(f'Postal Code: {data["postal"]}')
                print(f'Time Zone: {data["timezone"]}')
                print(f'ISP: {data["org"]}')

                #check if ASN (Autonomous System Number) is available
                if 'asn' in data:
                    print(f'ASN: {data["asn"]}')
                else:
                    print('ASN: Information not available')

                #extract and print country code
                print(f'Country Code: {data["country"]}')

                #log ip address for history tracking
                log_ip_address(data["ip"])

            else:
                print(f'Failed to retrieve data. Status code: {response.status_code}')

    except Exception as e:
        print(f'An error occurred: {str(e)}')

def log_ip_address(ip_address):
    #implement IP history tracking by logging the IP address to a txt file
    with open('ip_history.txt', 'a') as file:
        file.write(f'{ip_address}\n')
    #print a message stating that the ip address is saved for history tracking
    print('IP Address logged for history tracking.\n')

if __name__ == "__main__":
    print("Retrieving Geolocation Information...\n")
    get_public_ip_info()
