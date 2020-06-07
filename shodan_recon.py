#!/usr/bin/python

import shodan


def get_host_details(IP, api):
    host = api.host(IP)
    p = ""
    for item in host['data']:
        p += str(item['port']) + " "

    return p



def search_dork(dork, api):
    try:
        results = api.search(dork)

        print("\nTotal = {} \n".format(results['total']))       
        
        for result in results['matches']:
            print("IP: {}".format(result['ip_str']))
            port = get_host_details(result['ip_str'], api)
            print("Ports: {}\n".format(port))

    except shodan.APIError as e:
        print("Shodan Error : {}".format(e))


def main():
    SHODAN_API_KEY = input('Enter your shodan api key : ')
    dork = input('Enter your dork : ')
    api = shodan.Shodan(SHODAN_API_KEY)
    search_dork(dork, api)


if __name__ == '__main__':
    main()
