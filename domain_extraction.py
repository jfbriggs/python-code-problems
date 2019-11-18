"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

Examples:

domain_name("http://github.com/carbonfive/raygun") == "github"
domain_name("http://www.zombie-bites.com") == "zombie-bites"
domain_name("https://www.cnet.com") == "cnet"
"""

def domain_name(url):
    url_split = url.split("/")

    if url_split[0][:4] == "http":
        domain_iso = url_split[2]
    else:
        domain_iso = url_split[0]

    domain_split =  domain_iso.split(".")

    if domain_split[0] == "www":
        return domain_split[1]
    else:
        return domain_split[0]


## TEST CODE ##

print(domain_name("http://github.com/carbonfive/raygun")) # "github"
print(domain_name("http://www.zombie-bites.com")) # "zombie-bites"
print(domain_name("https://www.cnet.com")) # "cnet"
print(domain_name("www.xakep.ru")) # "xakep"
