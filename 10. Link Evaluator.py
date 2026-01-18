# Written using this tutorial: https://www.youtube.com/watch?v=sCpsr4gH65k. Comments added by me for understanding
# Scanning URLs in this manner is legal and doesn't require a disclaimer


# Import libraries
import tldextract
import Levenshtein as lv

# A list of legitimate domains to compare links to
legitimateDomains = ["example.com", "google.com", "microsoft.com", "amazon.com"]

# A list of URLs to test
testURLs = [
    "http://example.com",
    "https://example.com",
    "https://google.com",
    "https://microsoft.com",
    "http://amazpn.com",
    "https://amazn.com",
    ]

# Breaks a URL down into its composite parts
def extractDomainParts(url):
    extracted = tldextract.extarct(url)
    return extracted.subdomain, extracted.domain, extracted.suffix

# Check if a domain is misspelt by comparing the spelling based on the list of legitimate domains
def isMisspeltDomain(domain, legitimateDomains, threshold=0.9):
    for legitDomain in legitimateDomains:
        similarity = lv.ratio(domain, legitDomain)
        if similarity >= threshold:
            return False  # Domain is legitimate as it's similar enough to a legitimate domain
        
    return True  # No close match found so probably misspelt


# Check if the URL is illegitimate
def isPhishingURL(url, legitimateDomains):
    subdomain, domain, suffix = extractDomainParts(url)
    
    # Check if it's in the list of legitimate domains
    if f"{domain}.{suffix}" in legitimateDomains:
        return False  # Known domain so can't be phishing
    
    # Check if domain name is misspelt
    if isMisspeltDomain(domain, legitimateDomains):
        print(f"Potential phishing URL detected: {url}")
        return True
    
    return False

"""
    Things I've learned
    1. How to use tldextract to break down text
    2. How to use Levenshtein to generate a comparison ratio
    3. How to declare a parameter with a constant value in a function declaration
"""
