# """Mixtemi infrastructure declaration"""

import pulumi

import dns

dns_man = dns.DNSManager()

# - own
dns_man.add_record("A", "@", "75.2.60.5")
dns_man.add_record("CNAME", "www", "mixtemi-landing.netlify.app")

# - email
dns_man.add_MX_record("fwd1.porkbun.com", priority=50)
dns_man.add_MX_record("fwd2.porkbun.com", priority=40)
dns_man.add_MX_record("mx.zoho.com", priority=30)
dns_man.add_MX_record("mx2.zoho.com", priority=20)
dns_man.add_MX_record("mx3.zoho.com", priority=10)
dns_man.add_record("TXT", "@", "v=spf1 include:zoho.com ~all", rs_name="spf-record")
dns_man.add_record("TXT", "@", "zoho-verification=zb18658161.zmverify.zoho.com", rs_name="zoho-verification")

# - envs
dns_man.add_record("A", "app", "45.77.193.253")
dns_man.add_record("CNAME", "dev", "app.@")

# - empanada
dns_man.add_record("CNAME", "api.empanada.app", "app.@")
dns_man.add_record("CNAME", "api.2-empanada.app", "app.@")
dns_man.add_record("CNAME", "empanada-3-api.prod", "app.@")
dns_man.add_record("CNAME", "api.empanada.dev", "dev.@")

# - servers
pluto = dns.KlusterDNS("pluto", "129.153.195.31")
