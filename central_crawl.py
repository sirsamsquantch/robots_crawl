import re, requests

# baseURL = input('baseURL: ')

baseURL = 'http://192.168.1.180'
f = open('robots.txt', 'r')

userAgents = ('testing', 'stage', 'dev', 'prod')
urls = []
found = []

content = f.readlines()
pattern = '^.* (.*)$'


for line in content:
	if re.search(pattern,line):
		m = re.search(pattern,line)
		url = m.group(1)
		try:
			if url[0] == '/':
				# print(url)
				urls.append(url)
		except:
			pass

for agent in userAgents:
	for url in urls:
		url = baseURL+url
		# print(url)
		headers = {'User-Agent':agent}
		try:
			r = requests.get(url, headers=headers)
			if r.status_code == 200:
				print(url+' : '+agent)
			# print(type(r.status_code))
		except:
			pass