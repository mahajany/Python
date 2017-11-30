#Used to make requests
import sys
import json
import urllib.request
def main():
	try:
    	CITY=sys.argv[1]
    	API="https://maps.googleapis.com/maps/api/geocode/json?address="
    	GOOGLE_API_KEY=get_google_api_key()
    	URL=API+CITY+"&key="+GOOGLE_API_KEY+'&sensor=false'
    	print(URL)
	    response= json.load(urllib.request.urlopen(URL))
    	status=response['status']
    	results=response['results']
	   print(status , " --> ", results)
    	if status=='OK':
	    	pass
    	else:
	    	print("ERROR:", response['error_message'])
	except:
	  	   print("Dr.Watson, when you see an error, all I see is possibilities.")

def get_google_api_key():
	f=open('../../../google-api-key-1.txt')
	key=f.read()
	return str(key)
if __name__=="__main__":
	main()	

	
