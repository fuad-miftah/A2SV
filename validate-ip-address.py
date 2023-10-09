class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        
        def ip4(query):
            c = Counter(query)
            if c["."] != 3:
                return False 
            ips = query.split(".")
            if len(ips) != 4:
                return False
            for ip in ips:
                if len(ip) > 3:
                    return False
                if len(ip) > 1 and ip[0] == '0':
                    return False
                if ip.isdigit() == False:
                    return False
                if 255 < int(ip):
                    return False
            return True
        def ip6(query):
            c = Counter(query)
            if c[":"] != 7:
                return False 
            ips = query.split(":")
            print(ips)
            if len(ips) != 8:
                return False
            for ip in ips:
                if ip == "":
                    return False
                if len(ip) > 4:
                    return False
                for i in ip:
                    if not i.isdigit():
                        if 'f' < i.lower():
                            return False
            return True
        if ip6(queryIP):
            return "IPv6"
        if ip4(queryIP):
            return "IPv4"
        return "Neither"