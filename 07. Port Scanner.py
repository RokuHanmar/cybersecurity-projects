# Written using this tutorial: https://www.youtube.com/watch?v=UZ6VDgTm3vw. Comments added by me for understanding
# Disclaimer: port scanning without consent is illegal. This tool is made for demonstration purposes only

# Import libraries
import nmap3

# Opens nmap, scans the target port, and returns what it finds in JSON
nmap = nmap3.Nmap()
results = nmap.scan_top_ports("scanme.nmap. org")
print(results)

"""
    Things I've learned
    1. The basics of integrating nmap with Python
"""
