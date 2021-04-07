import re, requests

# baseURL = input('baseURL: ')

baseURL = 'http://192.168.1.180'
f = open('robots.txt', 'r')

userAgents = ('testing', 'stage', 'dev', 'prod')
urls = []

content = f.readlines()
pattern = '^.* (.*)$'
found = []

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
				# print(url+' : '+agent)
				success = url+' : '+agent
				found.append(success)
				# print(r.content)
				flagPattern = 'Central-InfoSec{(.*\w)}'
				if re.search(flagPattern, str(r.content)):
					match = re.search(flagPattern, str(r.content))
					foundFlag = match.group(0)
					print('************************')
					print('Found a flag on '+url)
					print('UserAgent: '+agent)
					print(foundFlag)
					print('************************')

				# pass
			# elif r.status_code == 500:
				# print(r.status_code)
				# print(url+' : '+agent)
				# pass
			# elif r.status_code != 200:
				# print(url+' : '+agent)

			# print(r.status_code)
		except Exception as error:
			print(error)

found.sort()
for x in found:
	print(x)
