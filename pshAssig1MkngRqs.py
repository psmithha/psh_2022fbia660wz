import requests

# Working URL
urlworking = "https://www.google.com/search?q=tim+berners+lee"
# Wrong URL
urlnotworking = "http://notapage.asg1/"
#Post URL
urlpost = 'https://www.wikipedia.org/'

def test_url(url,callmethod):
    if callmethod == 'get':
        try:
            r = requests.get(url)
            if r.status_code == 200:
                print(f"\n {url}: is reachable \n")
                print(f"The content ('body') of the response is: \n\n {r.text} \n")
                print(f"The status code of the response is: {r.status_code} \n")
                print(f"The response headers is \n\n: {r.headers} \n")
            else:
                print(f"The {url} exist but I cannot contact it successfully Code: {r.status_code}")
                print(f"The content ('body') of the response is: \n\n {r.text} \n")
                print(f"The status code of the response is: {r.status_code} \n")
                print(f"The response headers is \n\n: {r.headers} \n")
        except requests.exceptions.RequestException as e:
            print(f"\n {url}: is Not reachable.")



    elif callmethod == 'post':
        try:
            myobj = {'somekey': 'somevalue'}
            r = requests.post(url, json=myobj)
            if r.status_code == 200:
                print(f"\n {url}: is reachable\n")
                print(f"The content ('body') of the response is: \n\n {r.text} \n")
                print(f"The status code of the response is: {r.status_code} \n")
                print(f"The response headers is \n\n: {r.headers} \n")
            else:
                print(f"\n{url}: is Not reachable\n")
                print(f"The content ('body') of the response is: \n\n {r.text} \n")
                print(f"The status code of the response is: {r.status_code} \n")
                print(f"The response headers is \n\n: {r.headers} \n")

        except requests.exceptions.RequestException as e:
            # print URL with Errs
            raise SystemExit(f"{url}: is Not reachable \n\nErr: {e}")

        except requests.exceptions.InvalidURL as e:
            # print URL with Errs
            raise SystemExit(f"{url}: is Not reachable \nErr: {e}")
    elif callmethod == 'time':
        try:
            r = requests.get(url)
            if r.status_code == 200:
                print(f"\n {url}: is reachable and it took {r.elapsed.total_seconds()} to get the respond\n")
                print(f"The content ('body') of the response is: \n\n {r.text} \n")
                print(f"The status code of the response is: {r.status_code} \n")
                print(f"The response headers is \n\n: {r.headers} \n")
            else:
                print(f"{url}: is Not reachable and it took {r.elapsed.total_seconds()} to respond\n")
                print(f"The content ('body') of the response is: \n\n {r.text} \n")
                print(f"The status code of the response is: {r.status_code} \n")
                print(f"The response headers is \n\n: {r.headers} \n")

        except requests.exceptions.RequestException as e:
            # print URL with Errs
            raise SystemExit(f"{url}: is Not reachable \n\nErr: {e}")

        except requests.exceptions.InvalidURL as e:
            # print URL with Errs
            raise SystemExit(f"{url}: is Not reachable \nErr: {e}")

print("Step 2a - Point A - Google search for the term 'Tim Berners-Lee' ")
test_url(urlworking, 'get')
print()
print("Step 2a - Point B - A POST request to a website that does not accept POST requests.")
test_url(urlpost, 'post')
# print()
print("Step 2a - Point C - A request to a URL that does not exist.")
test_url(urlnotworking, 'get')
print()
print("Step 2b - How much a request 'round trip' a http request takes")
test_url(urlworking, 'time')





