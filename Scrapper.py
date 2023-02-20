from requests import get
base_url = "https://remoteok.com/remote-"
search_term = "python"
end_url = "-jobs"

# url = f"{base_url}{search_term}{end_url}"
url = "https://remoteok.com"
response = get(url)

if response.status_code != 200:
  print("Can't request website")
else:
  print(response.text)
print(response)
print(url)