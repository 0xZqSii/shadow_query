# 🌑 Shadow Query

DNS Reconnaissance & Lookup Tool

<p align="center">
  <strong>A lightweight Python tool for DNS reconnaissance, record lookup, and DNS analysis.</strong>
</p><p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS%20%7C%20Termux-lightgrey?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
</p>---

### 📌 Overview

Shadow Query is a lightweight DNS reconnaissance tool written in Python. It allows users to query DNS records, use DNS-over-HTTPS (DoH), specify custom DNS servers, and test DNS zone transfer (AXFR) capabilities.

Designed with simplicity and ease of use in mind, Shadow Query provides a straightforward command-line interface for DNS-related tasks.

---

### ✨ Features

- DNS Record Lookup
- DNS-over-HTTPS (DoH) using Cloudflare
- Custom DNS Server Support
- DNS Zone Transfer (AXFR) Testing
- Response Time Measurement
- Multiple Domain Queries
- Formatted Terminal Output

---

### 🖥️ Supported Platforms

- Linux
- Windows
- macOS
- Termux (Android)

---

### ⚙️ Installation

Python 3 is required.

</p>---
Linux

git clone https://github.com/0xZqSii/shadow_query.git

cd Shadow-Query

python3 -m pip install dnspython requests rich
python3 shadow_query.py -d example.com

</p>---
Windows

git clone https://github.com/0xZqSii/shadow_query.git

cd Shadow-Query

py -m pip install dnspython requests rich
py shadow_query.py -d example.com

</p>---
Termux (Android)

pkg update
pkg install python git -y

git clone https://github.com/0xZqSii/shadow_query.git

cd Shadow-Query

python -m pip install dnspython requests rich
python shadow_query.py -d example.com

</p>---
macOS

git clone https://github.com/0xZqSii/shadow_query.git

cd Shadow-Query

python3 -m pip install dnspython requests rich
python3 shadow_query.py -d example.com

---

### 🚀 Usage

#### Basic DNS Lookup

python shadow_query.py -d example.com

#### Query a Specific Record

python shadow_query.py -d example.com -t A

#### Use a Custom DNS Server

python shadow_query.py -d example.com -t A -s 1.1.1.1

#### DNS-over-HTTPS (DoH)

python shadow_query.py -d example.com --doh

#### DNS Zone Transfer (AXFR)

python shadow_query.py -d example.com --axfr -s DNS_SERVER

#### Query Multiple Domains

python shadow_query.py -d example.com example.org -t A

---

### 🧰 Command-Line Options

#### Option| Description
"-d", "--domain"| Specify one or more domains to query
"-t", "--type"| Specify a DNS record type
"-s", "--server"| Specify a custom DNS server
"--doh"| Use DNS-over-HTTPS
"--axfr"| Attempt a DNS zone transfer

---

### 🛠️ Built With

- Python
- dnspython
- Requests
- Rich
- Argparse

---

### 📂 Project Structure

Shadow-Query/
│
├── shadow_query.py
└── README.md

---

### ⚠️ Disclaimer

Shadow Query is intended for educational purposes and authorized security testing only.

Users are responsible for obtaining proper authorization before performing DNS queries or attempting DNS zone transfers against domains or DNS servers.

The developer assumes no responsibility or liability for any misuse of this tool or any damage resulting from its use.

---

<p align="center">
  <strong>Shadow Query — Learn, Explore, and Analyze.</strong>
</p>
