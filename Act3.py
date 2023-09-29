import requests

def get_public_ip_info():
    try:
        # get request to ipinfo.io API to retrieve information
        response = requests.get('https://ipinfo.io/json')

        # check if the http response status code is 200
        if response.status_code == 200:
            data = response.json()
            
            # extract and print ipv4 address
            print(f'Public IPv4 Address: {data["ip"]}')

            # check and print if ipv6 is available
            if 'ip6' in data:
                print(f'Public IPv6 Address: {data["ip6"]}')
            else:
                print('IPv6 Address not available')

            # extract and print geolocation information
            loc = data.get("loc", "").split(",")
            latitude = loc[0] if loc else "N/A"
            longitude = loc[1] if len(loc) > 1 else "N/A"
            print(f'Latitude: {latitude}')
            print(f'Longitude: {longitude}')
            print(f'Geolocation: {data["city"]}, {data["region"]}, {data["country"]}')
            print(f'ISP: {data["org"]}')
            
            # check if asn is available
            if 'asn' in data:
                print(f'ASN: {data["asn"]}')
            else:
                print('ASN: Information not available')
                
            #extract and print country code
            print(f'Country Code: {data["country"]}')
        else:
            print(f'Country Code: Failed to retrieve data. Status code: {response.status_code}')
    
    except Exception as e:
        print(f'An error occurred: {str(e)}')

if __name__ == "__main__":
    print("Retrieving Information...\n")
    get_public_ip_info()
