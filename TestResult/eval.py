import json
import pickle
from urllib.parse import urlparse
from pprint import pprint

############ Test No extension HAR #############

# request_noDNT = 0
# request_noDNT_third = 0
# unique_noDNT_third = 0
# unique_noDNT_cookie_third = 0
# num_noDNT_succeed = 0
# num_noDNT_tested = 0

# database_orig = []

# noDNT_f = open("firefox_noDNT.txt")
# noDNT_sites = noDNT_f.readlines()
# for noDNT in noDNT_sites:
# 	orig = json.loads(noDNT)
# 	num_noDNT_tested += 1
# 	pair = {}
# 	if len(orig["log"]["entries"]) == 0:
# 		continue
# 	else:
# 		request_noDNT += len(orig["log"]["entries"])
# 		num_noDNT_succeed += 1
# 		url = urlparse(orig["log"]["entries"][0]["request"]["url"])
# 		firstParty = '{uri.scheme}://{uri.netloc}/'.format(uri=url)
# 		unique_third_set = set()

# 		for i in range(0, len(orig["log"]["entries"])):
# 			check_url = urlparse(orig["log"]["entries"][i]["request"]["url"])
# 			thirdParty = '{uri.scheme}://{uri.netloc}/'.format(uri=check_url)
# 			if thirdParty != firstParty:
# 				request_noDNT_third += 1
# 				if thirdParty not in unique_third_set:
# 					unique_third_set.add(thirdParty)
# 					if orig["log"]["entries"][i]["request"]["cookies"]:
# 						unique_noDNT_cookie_third += 1

# 			key = (orig["log"]["entries"][i]["request"]["url"], 
# 				orig["log"]["entries"][i]["request"]["method"], 
# 				orig["log"]["entries"][i]["request"]["httpVersion"],
# 				orig["log"]["entries"][i]["response"]["status"],
# 				orig["log"]["entries"][i]["request"]["bodySize"],
# 				orig["log"]["entries"][i]["response"]["headersSize"],
# 				orig["log"]["entries"][i]["response"]["bodySize"])
# 			value = orig["log"]["entries"][i]["request"]["headers"]
# 			if key in pair:
# 				continue
# 			else:
# 				pair[key] = value 
# 		unique_noDNT_third += len(unique_third_set)
# 	database_orig.append(pair)
# noDNT_f.close()

# print("No extension")
# print("Websites tested: " + str(num_noDNT_tested))
# print("Websites succeed: " + str(num_noDNT_succeed))
# print("total requests: " + str(request_noDNT))
# print("Average requests " + str(request_noDNT/num_noDNT_succeed))
# print("Third party requests: " + str(request_noDNT_third))
# print("Average third party requests: " + str(request_noDNT_third/num_noDNT_succeed))
# print("Unique third party: " + str(unique_noDNT_third))
# print("Average unique third party: " + str(unique_noDNT_third/num_noDNT_succeed))
# print("Unique third party with cookies: " + str(unique_noDNT_cookie_third))
# print()

############ Test Extension HAR #############
# file_list = ["100Ghostery.har", "2000Ghostery.har", "100pb.har", "2000pb.har"]

# for file in file_list:

# 	request_DNT = 0
# 	request_DNT_third = 0
# 	unique_DNT_third = 0
# 	unique_DNT_cookie_third = 0
# 	num_DNT_succeed = 0
# 	num_DNT_tested = 0
# 	header_changed = 0

# 	with open(file) as DNT_f:
# 		DNT_sites = json.load(DNT_f)
# 		out_of_bound = False
# 		for orig in DNT_sites:
# 			num_DNT_tested += 1
# 			if num_DNT_tested > num_noDNT_tested:
# 				out_of_bound = True
# 			if len(orig["log"]["entries"]) == 0:
# 				continue
# 			else:
# 				request_DNT += len(orig["log"]["entries"])
# 				num_DNT_succeed += 1
# 				url = urlparse(orig["log"]["entries"][0]["request"]["url"])
# 				firstParty = '{uri.scheme}://{uri.netloc}/'.format(uri=url)
# 				unique_third_set = set()
# 				for i in range(0, len(orig["log"]["entries"])):
# 					check_url = urlparse(orig["log"]["entries"][i]["request"]["url"])
# 					thirdParty = '{uri.scheme}://{uri.netloc}/'.format(uri=check_url)
# 					if thirdParty != firstParty:
# 						request_DNT_third +=1
# 						if thirdParty not in unique_third_set:
# 							unique_third_set.add(thirdParty)
# 							if orig["log"]["entries"][i]["request"]["cookies"]:
# 								unique_DNT_cookie_third += 1
# 					key = (orig["log"]["entries"][i]["request"]["url"], 
# 						orig["log"]["entries"][i]["request"]["method"], 
# 						orig["log"]["entries"][i]["request"]["httpVersion"],
# 						orig["log"]["entries"][i]["response"]["status"],
# 						orig["log"]["entries"][i]["request"]["bodySize"],
# 						orig["log"]["entries"][i]["response"]["headersSize"],
# 						orig["log"]["entries"][i]["response"]["bodySize"])
# 					value = orig["log"]["entries"][i]["request"]["headers"]

# 					if not out_of_bound:
# 						if key in database_orig[num_DNT_tested-1]:
# 							if value != database_orig[num_DNT_tested-1][key]:
# 								header_changed += 1


# 				unique_DNT_third += len(unique_third_set)
# 	DNT_f.close()
# 	print("Extension with " + file)
# 	print("Websites tested: " + str(num_DNT_tested))
# 	print("Websites succeed: " + str(num_DNT_succeed))
# 	print("total requests: " + str(request_DNT))
# 	print("Average requests " + str(request_DNT/num_DNT_succeed))
# 	print("Third party requests: " + str(request_DNT_third))
# 	print("Average third party requests: " + str(request_DNT_third/num_DNT_succeed))
# 	print("Unique third party: " + str(unique_DNT_third))
# 	print("Average unique third party: " + str(unique_DNT_third/num_DNT_succeed))
# 	print("Unique third party with cookies: " + str(unique_DNT_cookie_third))
# 	print("Header changed in total: " + str(header_changed))
# 	print("Header changed per site: " + str(header_changed/num_DNT_succeed))
# 	print()


############# Test with Tianyu's format HAR file (firefox_withDNT, firefox_ABP, chrome_DNT) ############

request_noDNT = 0
request_noDNT_third = 0
unique_noDNT_third = 0
unique_noDNT_cookie_third = 0
num_noDNT_succeed = 0
num_noDNT_tested = 0

noDNT_f = open("firefox_noDNT.txt")
noDNT_sites = noDNT_f.readlines()
for noDNT in noDNT_sites:
	orig = json.loads(noDNT)
	num_noDNT_tested += 1
	if len(orig["log"]["entries"]) == 0:
		continue
	else:
		request_noDNT += len(orig["log"]["entries"])
		num_noDNT_succeed += 1
		url = urlparse(orig["log"]["entries"][0]["request"]["url"])
		firstParty = '{uri.scheme}://{uri.netloc}/'.format(uri=url)
		unique_third_set = set()
		for i in range(0, len(orig["log"]["entries"])):
			check_url = urlparse(orig["log"]["entries"][i]["request"]["url"])
			thirdParty = '{uri.scheme}://{uri.netloc}/'.format(uri=check_url)
			if thirdParty != firstParty:
				request_noDNT_third += 1
				if thirdParty not in unique_third_set:
					unique_third_set.add(thirdParty)
					if orig["log"]["entries"][i]["request"]["cookies"]:
						unique_noDNT_cookie_third += 1
		unique_noDNT_third += len(unique_third_set)

noDNT_f.close()

print("Websites tested: " + str(num_noDNT_tested))
print("Websites succeed: " + str(num_noDNT_succeed))
print("total requests: " + str(request_noDNT))
print("Average requests " + str(request_noDNT/num_noDNT_succeed))
print("Third party requests: " + str(request_noDNT_third))
print("Average third party requests: " + str(request_noDNT_third/num_noDNT_succeed))
print("Unique third party: " + str(unique_noDNT_third))
print("Average unique third party: " + str(unique_noDNT_third/num_noDNT_succeed))
print("Unique third party with cookies: " + str(unique_noDNT_cookie_third))
print()

