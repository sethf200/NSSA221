import subprocess

def get_gateway():
    result = subprocess.run(['ip', 'r'], stdout=subprocess.PIPE, text=True)
    for line in result.stdout.splitlines():
        if 'default via' in line:
            gateway = line.split()[2]
            return gateway
        else:
            return print("No default gateway found! Please check your network settings. This can typically be resolved by enabling DHCP or manually entering your gateway's IP in your network settings.")

def main():
    print("Welcome to cool sysadmin tools v1.0.\n\nWhat would you like to do?\n1. Display the default gateway\n2. Test local connectivity\n3. Test remote connectivity\n4. Test DNS resolution\n5. Exit/quit the script")
    print(get_gateway())
    
if __name__ == "__main__":
    main()