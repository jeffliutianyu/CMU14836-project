import json
import pickle
from urllib.parse import urlparse
from pprint import pprint

request_noDNT = 0
request_noDNT_third = 0
unique_noDNT_third = 0
unique_noDNT_cookie_third = 0
num_noDNT_succeed = 0
num_noDNT_tested = 0
unique_third_list = []
final_result_diff = {}

noDNT_f = open("firefox_noDNT.txt")
noDNT_sites = noDNT_f.readlines()
for noDNT in noDNT_sites:
	orig = json.loads(noDNT)
	if len(orig["log"]["entries"]) == 0:
		continue
	else:
		url = urlparse(orig["log"]["entries"][0]["request"]["url"])
		firstParty = '{uri.scheme}://{uri.netloc}/'.format(uri=url)
		unique_third_set = set()
		unique_third_set_cookie = set()
		for i in range(0, len(orig["log"]["entries"])):
			check_url = urlparse(orig["log"]["entries"][i]["request"]["url"])
			thirdParty = '{uri.scheme}://{uri.netloc}/'.format(uri=check_url)
			if thirdParty != firstParty:
				if thirdParty not in unique_third_set:
					unique_third_set.add(thirdParty)
					if orig["log"]["entries"][i]["request"]["cookies"]:
						unique_noDNT_cookie_third += 1
						unique_third_set_cookie.add(thirdParty)
		unique_noDNT_third += len(unique_third_set)
		unique_third_list.append(unique_third_set_cookie)

noDNT_f.close()

chrome_f = open("firefox_withDNT.txt")
chrome_sites = chrome_f.readlines()
for c in chrome_sites:
	orig = json.loads(c)
	num_noDNT_tested += 1
	if len(orig["log"]["entries"]) == 0:
		continue
	else:
		url = urlparse(orig["log"]["entries"][0]["request"]["url"])
		firstParty = '{uri.scheme}://{uri.netloc}/'.format(uri=url)
		unique_third_set = set()
		unique_third_set_cookie = set()
		for i in range(0, len(orig["log"]["entries"])):
			check_url = urlparse(orig["log"]["entries"][i]["request"]["url"])
			thirdParty = '{uri.scheme}://{uri.netloc}/'.format(uri=check_url)
			if thirdParty != firstParty:
				if thirdParty not in unique_third_set:
					unique_third_set.add(thirdParty)
					if orig["log"]["entries"][i]["request"]["cookies"]:
						unique_noDNT_cookie_third += 1
						unique_third_set_cookie.add(thirdParty)
		unique_noDNT_third += len(unique_third_set)
		for ele in unique_third_set_cookie:
			difference = []
			if ele not in unique_third_list[num_noDNT_tested-1]:
				difference.append(ele)
			final_result_diff[firstParty] = difference

chrome_f.close()

# print("Websites tested: " + str(num_noDNT_tested))
# print("Websites succeed: " + str(num_noDNT_succeed))
# print("total requests: " + str(request_noDNT))
# print("Average requests " + str(request_noDNT/num_noDNT_succeed))
# print("Third party requests: " + str(request_noDNT_third))
# print("Average third party requests: " + str(request_noDNT_third/num_noDNT_succeed))
# print("Unique third party: " + str(unique_noDNT_third))
# print("Average unique third party: " + str(unique_noDNT_third/num_noDNT_succeed))
# print("Unique third party with cookies: " + str(unique_noDNT_cookie_third))
# for element in unique_third_temp:
# 	print(element)
for key, value in final_result_diff.items():
	print(key)
	print(value)
	print()
print()


