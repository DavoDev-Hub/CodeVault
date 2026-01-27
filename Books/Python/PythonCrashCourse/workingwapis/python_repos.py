import requests

# MAke an API call and store the response.
url = 'https://api.github.com/search/repositories'
url += '?q=language:python&sort=stars:>10000'

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

# Convert the response to a dictionary.
response_dict = r.json()
# Process results.
print(response_dict.keys())

print(f"Total repositories: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository
repo_dict = repo_dicts[0]
print('\nKeys:', len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)