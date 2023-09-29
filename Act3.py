import requests

def get_public_ip_info():
    try:
        response = requests.get('https://ipinfo.io/json')
        
        if response.status_code == 200:
            data = response.json()
            
            print(f'Public IPv4 Address: {data["ip"]}')
            
            if 'ip6' in data:
                print(f'Public IPv6 Address: {data["ip6"]}')
            else:
                print('IPv6 Address not available')
            
            print(f'Location: {data["city"]}, {data["region"]}, {data["country"]}')
            print(f'ISP: {data["org"]}')
            
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
