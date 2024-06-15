import csv

# Define the list of passwords
passwords = [
    "password", "123456", "qwerty", "123456789", "abc123", 
    "admin", "password123", "iloveyou", "letmein", "football",
    "1234567", "123123", "sunshine", "master", "1234", 
    "welcome", "shadow", "monkey", "password1", "superman",
    "12345", "12345678", "qwertyuiop", "111111", "1234567890",
    "123", "password123456", "admin123", "test", "qazwsx",
    "123qwe", "asdf", "7777777", "777777", "password!",
    "qwerty123", "123321", "123abc", "1234qwer", "dragon",
    "123qweasd", "696969", "mustang", "zaq1zaq1", "football1",
    "passw0rd", "jordan23", "harley", "123456a", "hello123",
    "pass", "baseball", "1qaz2wsx", "qwer1234", "abcd1234",
    "qwe123", "qwerty12345", "access", "flower", "michael",
    "abc123456", "solo", "qazwsxedc", "welcome1", "123abc123",
    "thomas", "killer", "trustno1", "george", "charlie",
    "test123", "1q2w3e4r", "121212", "aaa", "123qwezxc",
    "1qazxsw2", "1234abcd", "password12", "qwertyuio", "jessica",
    "1234abcd", "iloveyou1", "computer", "jennifer", "shadow1",
    "whatever", "hockey", "zaqwsx", "matthew", "asdfgh",
    "123zxcvbn", "letmein1", "pass1234", "1234qazwsx", "12345a"
]

# Create a list of dictionaries for CSV writer
data = []
for rank, password in enumerate(passwords, start=1):
    data.append({'Rank': rank, 'Password': password})

# Define the CSV file path
csv_file = 'top_100_passwords.csv'

# Write to CSV file
with open(csv_file, 'w', newline='') as f:
    fieldnames = ['Rank', 'Password']
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    
    writer.writeheader()
    for row in data:
        writer.writerow(row)

print(f'CSV file "{csv_file}" has been created successfully.')
