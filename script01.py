#!/usr/bin/env python3

import os
import subprocess

def get_default_gateway():
    #retrieve default gateway dynamically using 'ip r' command.
    result = subprocess.run(['ip', 'r'], capture_output=True, text=True)
    for line in result.stdout.splitlines():
        if 'default via' in line:
            return line.split()[2]
    return None

def test_local_connectivity():
    print("\nTesting local connectivity (pinging default gateway)...")
    gateway_ip = get_default_gateway()
    if gateway_ip:
        response = os.system("ping -c 4" + gateway_ip)
        if response == 0:
            print("Local connectivity to + gateway_ip + successful.")
        else:
            print("Local connectivity to" + gateway_ip + "failed.")
    else:
        print("Unable to retrieve the default gateway.")

def test_remote_connectivity():
    print("\nTesting remote connectivity (pinging 129.21.3.17 - RIT's DNS server)...")
    response = os.system("ping -c 4 129.21.3.17")
    if response == 0:
        print("Remote connectivity successful.")
    else:
        print("Remote connectivity failed.")

def test_dns_resolution():
    print("\nTesting DNS resolution (pinging www.google.com)...")
    response = os.system("ping -c 4 www.google.com")
    if response == 0:
        print("DNS resolution and connectivity to www.google.com successful.")
    else:
        print("DNS resolution or connectivity to www.google.com failed.")

def display_menu():
    print("Welcome to cool sysadmin connectivity tools v1.0")
    print("What would you like to do?")
    print("1. Display the default gateway")
    print("2. Test Local Connectivity")
    print("3. Test Remote Connectivity")
    print("4. Test DNS Resolution")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == '1':
            gateway_ip = get_default_gateway()
            if gateway_ip:
                print(f"\nDefault Gateway: {gateway_ip}")
            else:
                print("\nUnable to retrieve the default gateway.")
        elif choice == '2':
            test_local_connectivity()
        elif choice == '3':
            test_remote_connectivity()
        elif choice == '4':
            test_dns_resolution()
        elif choice == '5':
            print("\nExiting...")
            break
        else:
            print("\nInvalid. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
