from netmiko import ConnectHandler


device = {
    'device_type': 'cisco_ios',
    'host': '192.168.56.102',  
    'username': 'cisco',
    'password': 'cisco123!',
    'port': 22,  
    'secret': 'tu_enable_password',  
}


output_file = 'output.txt'


try:
    net_connect = ConnectHandler(**device)
    net_connect.enable()  

 
    eigrp_config_commands = [
        'ipv6 unicast',
        'router eigrp DRY7122',  
        'address-family ipv4 autonomous-system 100',
        'network 10.0.0.0 0.255.255.255',
        'passive-interface default',
        'no passive-interface GigabitEthernet0/1', 
        'exit-address-family',
        'address-family ipv6 autonomous-system 100',
        'af-interface default',
        'no shutdown',
        'exit-af-interface',
        'exit-address-family',
        'exit',
    ]


  
    output_ipv4 = net_connect.send_config_set(eigrp_config_commands)


    eigrp_show_command = 'show running-config | section eigrp'
    eigrp_output = net_connect.send_command(eigrp_show_command)
    with open(output_file, 'a') as f:
        f.write("\nSalida del comando 'show running-config | section eigrp':\n")
        f.write(eigrp_output + '\n')

    
    ip_interface_command = 'show ip interface brief'
    ip_interface_output = net_connect.send_command(ip_interface_command)
    with open(output_file, 'a') as f:
        f.write("\nSalida del comando 'show ip interface brief':\n")
        f.write(ip_interface_output + '\n')

    ipv6_interface_command = 'show ipv6 interface brief'
    ipv6_interface_output = net_connect.send_command(ipv6_interface_command)
    with open(output_file, 'a') as f:
        f.write("\nSalida del comando 'show ipv6 interface brief':\n")
        f.write(ipv6_interface_output + '\n')


    running_config_command = 'show running-config'
    running_config_output = net_connect.send_command(running_config_command)
    with open(output_file, 'a') as f:
        f.write("\nSalida del comando 'show running-config':\n")
        f.write(running_config_output + '\n')


    show_version_command = 'show version'
    show_version_output = net_connect.send_command(show_version_command)
    with open(output_file, 'a') as f:
        f.write("\nSalida del comando 'show version':\n")
        f.write(show_version_output + '\n')


    net_connect.disconnect()

    print(f"Todas las salidas se han guardado en {output_file}")

except Exception as e:
    print(f"Error: {str(e)}")
