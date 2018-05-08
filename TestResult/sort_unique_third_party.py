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
third_dict = {}

noDNT_f = open("2000pb.har")
noDNT_sites = json.load(noDNT_f)
# noDNT_sites = noDNT_f.readlines()
# for noDNT in noDNT_sites:
for orig in noDNT_sites:
	# orig = json.loads(noDNT)
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
						if thirdParty not in third_dict:
							third_dict[thirdParty] = 1
						else:
							third_dict[thirdParty] += 1 
		unique_noDNT_third += len(unique_third_set)

noDNT_f.close()

sorted_names = sorted(third_dict, key=lambda x: third_dict[x], reverse=True)
for k in sorted_names:
    print("{} : {}".format(k, third_dict[k]))

# print("Websites tested: " + str(num_noDNT_tested))
# print("Websites succeed: " + str(num_noDNT_succeed))
# print("total requests: " + str(request_noDNT))
# print("Average requests " + str(request_noDNT/num_noDNT_succeed))
# print("Third party requests: " + str(request_noDNT_third))
# print("Average third party requests: " + str(request_noDNT_third/num_noDNT_succeed))
# print("Unique third party: " + str(unique_noDNT_third))
# print("Average unique third party: " + str(unique_noDNT_third/num_noDNT_succeed))
# print("Unique third party with cookies: " + str(unique_noDNT_cookie_third))


print()