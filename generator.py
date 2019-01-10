import os
import subprocess

print("\n\n------------- Welcome to WEB SDK Generator -------------\n")
print("\nYour current directory is: " + str(os.getcwd()))
base_dir = os.getcwd()
print("\nEnter the following customer details to generate a new Web app for the customer:")

customer_name = input("\n\nCustomer Name: ")
customer_url = input("\nCustomer Home Page URL: ")

project_dir = os.path.join(base_dir, customer_name)

os.mkdir(project_dir, 0o755)
os.chdir(project_dir)
print("\nYour current directory is: " + str(os.getcwd()))
project_dir = os.getcwd()

bashCommand = "wget " + customer_url \
              + " --domains website.org --no-parent --page-requisites --html-extension --convert-links"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

bashCommand = "git clone https://github.com/Koredotcom/web-kore-sdk.git"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

print("\n\nEnter the following bot details to setup the Kore bot on the web page:")

bot_name = input("\nBot Name: ")
bot_id = input("\nBot ID: ")
client_id = input("\nClient ID: ")
client_secret = input("\nClient Secret: ")

os.chdir(project_dir)

