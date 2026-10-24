import requests

user_input = input("[Input]:")


user_agent  = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win 64; x64) AppleWebKit/537.36 (KHTML,"
        "like Gecko) Chrome/120.0.0.0 Safari/537.36"
    )
}

answer      = requests.head(user_input, headers=user_agent) #source

server_info = answer.headers.get("Server", "Not found")
backend     = answer.headers.get("X-Powered-By","Not found")
cookies     = answer.cookies.get("sessionid", "Not found")


print(f"[DOMAIN]  {user_input}")     #domain

if answer.status_code == 200:
   print("[STATUS]: OK")

elif answer.status_code == 403:
   print("[STATUS]: FORBIDDEN")

elif answer.status_code == 404:
    print("[STATUS]: NOT FOUND")

elif answer.status_code == 429:
    print("[STATUS]: TOO MANY REQUESTS")

elif answer.status_code == 503:
    print("[STATUS]: SERVICE UNAVAILABLE")

print(f"[COOKIES] {answer.cookies}") #cookies
print(f"[SERVER]  {server_info}")    #server_info
print(f"[BACKEND] {backend}")        #backend



