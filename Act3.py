import requests

def get_public_ip_info():
    try:
        # ipinfo.io API
        response = requests.get('https://ipinfo.io/json')
        
        if response.status_code == 200:
            data = response.json()
            
            # Extract ipv4 address
            print(f'Public IPv4 Address: {data["ip"]}')
            
            # Check if IPv6 is available
            if 'ip6' in data:
                print(f'Public IPv6 Address: {data["ip6"]}')
            else:
                print('IPv6 Address cannot be found')

            loc = data.get("loc", "").split(",")
            latitude = loc[0] if loc else "Information nit available"
            longitude = loc[1] if len(loc) > 1 else "Information not available"
            print(f'Latitude: {latitude}')
            print(f'Longitude: {longitude}')
            
            print(f'Location: {data["city"]}, {data["region"]}, {data["country"]}')
            print(f'ISP: {data["org"]}')
            
            # Check if 'asn' is available
            if 'asn' in data:
                print(f'ASN: {data["asn"]}')
            else:
                print('ASN information not available')
            
            print(f'Country Code: {data["country"]}')
        else:
            print(f'Failed to retrieve data. Status code: {response.status_code}')
    
    except Exception as e:
        print(f'An error occurred: {str(e)}')

if __name__ == "__main__":
    print("Retrieving public IP addressing information...\n")
    get_public_ip_info()
