import dns.resolver
import time
import requests
import dns.exception
import dns.query
import dns.zone
import argparse
from rich.console import Console
from rich.table import Table

Red = "\033[1;31m"
Reset = "\033[0m"
Green = "\033[1;32m"
Cyan = "\033[1;36m"
Blue = "\033[1;34m"
White = "\033[1;37m"

print(fr"""{Green}
███████╗██╗  ██╗ █████╗ ██████╗  ██████╗ ██╗    ██╗     ██████╗ ██╗   ██╗███████╗██████╗ ██╗   ██╗
██╔════╝██║  ██║██╔══██╗██╔══██╗██╔═══██╗██║    ██║    ██╔═══██╗██║   ██║██╔════╝██╔══██╗╚██╗ ██╔╝
███████╗███████║███████║██║  ██║██║   ██║██║ █╗ ██║    ██║   ██║██║   ██║█████╗  ██████╔╝ ╚████╔╝ 
╚════██║██╔══██║██╔══██║██║  ██║██║   ██║██║███╗██║    ██║▄▄ ██║██║   ██║██╔══╝  ██╔══██╗  ╚██╔╝  
███████║██║  ██║██║  ██║██████╔╝╚██████╔╝╚███╔███╔╝    ╚██████╔╝╚██████╔╝███████╗██║  ██║   ██║   
╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝  ╚═════╝  ╚══╝╚══╝      ╚══▀▀═╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   
                                                                                                  
{Reset}ShadowQuery{Green} v3.6{Reset}
This Tool Was Programming by Mohammed Alashwali{Blue}(@ZqSii){Reset}
My GitHub is : {Blue}https://github.com/0xzqsii{Reset}""")
print(f"{Cyan}-{Reset}"*70)

console = Console()
DNS_t = ["A", "AAAA", "CNAME", "MX", "NS", "TXT", "SOA", "PTR"]

def dns_lookup(domain, record_type = None, server=None, doh=None):
    resolver = dns.resolver.Resolver()
    if server :
        resolver.nameservers = [server]
    record_to_query = [record_type] if record_type  else DNS_t

    table = Table(title="DNS Table TEST")
    table.add_column("DOMAIN", style="cyan")
    table.add_column("TYPE", style="magenta")
    table.add_column("TIME", style="green")

    for rtype in record_to_query :
        try :
            stet_time = time.time()
            if doh :
                result = dns_test(domain , rtype)
            else :
                data = resolver.resolve(domain, rtype)
                result = ""
                for i in data :
                    result += str(i) + "\n"
                result.strip()
            end_time = time.time()
            response_time = round((end_time - stet_time )* 1000 ,2)
            table.add_row(rtype, result, str(response_time)) 
        except dns.resolver.NoAnswer :
            table.add_row(rtype, "NO record found")
        except dns.resolver.NXDOMAIN :
            console.print(f"[red]Error : domain {domain} dos not exist[/red]")
            return
        except Exception as e :
            table.add_row(rtype , f"Error - {e}")

    console.print(table)


def dns_test(domain, record_type):
    url = f"https://cloudflare-dns.com/dns-query?name={domain}&type={record_type}"
    headers = {"accept": "application/dns-json"}
    try :
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        data = response.json()
        result = ""
        for answer in data.get("Answer", []):
            result += answer["data"] + "\n"

        return result.strip()
    except requests.exceptions.RequestException as e :
        return f"Error {e}"



def dns_axfr(domain, server):
    try:
        test = dns.query.xfr(server, domain, timeout=10.0)
        ttest = dns.zone.from_xfr(test)

        if not ttest :
            print("Axfr faild: no data received")
            return
        for name, node in ttest.nodes.items():
            print(f"{name}: {node.to_text()}")
    except dns.exception.DNSException as e:
        print(f"Axfr faild: {e}")

if __name__ == "__main__":
    parse = argparse.ArgumentParser(description="DNS Tool Record")
    parse.add_argument("-d", "--domain", nargs="+", required=True, help="Domain(s) to query")
    parse.add_argument("-t", "--type", help="DNS Record Type")
    parse.add_argument("-s", "--server", help="Custom DNS server", default=None)
    parse.add_argument("--axfr", action="store_true", help="Zone transfer (axfr)")
    parse.add_argument("--doh", action="store_true", help="use DNS-over-Https(DoH)")

    args = parse.parse_args()
    
    for domain in args.domain :
        if args.axfr :
            if not args.server :
                print("AXFR rquires a custom DNS server")
            else :
                dns_axfr(domain, args.server)
        else :
            dns_lookup(domain, args.type, args.server, args.doh)
