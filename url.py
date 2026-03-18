# Phishing URL Detection System A basic code to check the website is safe or not
url = input("Enter a URL: ")
print("\nChecking the URL for phishing indicators...\n")

if url.startswith("http://"):
    print("Insecure protocol detected (HTTP).")
else:
    print("Secure protocol (HTTPS).")

if "@" in url or "-" in url:
    print("Unusual symbols found in the URL.")
else:
    print("No unusual symbols detected.")

if url.count(".") > 3:
    print("Suspicious domain structure detected.")
else:
    print("Domain structure looks normal.")

print("\nAnalysis Complete.")
