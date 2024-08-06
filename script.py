import json

zone_data = {
    "$origin": "educational.local.",
    "$ttl": 3600,
    "soa": {
        "mname": "ns1.educational.local.",
        "rname": "admin.educational.local.",
        "serial": "2024080601",
        "refresh": 3600,
        "retry": 600,
        "expire": 604800,
        "minimum": 86400
    },
    "ns": [
        { "host": "ns1.educational.local." },
        { "host": "ns2.educational.local." }
    ],
    "a": [
        { "name": "@", "ttl": 400, "value": "192.168.1.1" },
        { "name": "www", "ttl": 400, "value": "192.168.1.2" },
        { "name": "mail", "ttl": 400, "value": "192.168.1.3" },
        { "name": "ftp", "ttl": 400, "value": "192.168.1.4" }
    ],
    "cname": [
        { "name": "files", "ttl": 400, "value": "ftp.educational.local." }
    ],
    "mx": [
        { "name": "@", "ttl": 400, "preference": 10, "value": "mail.educational.local." }
    ],
    "txt": [
        { "name": "@", "ttl": 400, "value": "v=spf1 include:educational.local ~all" }
    ],
    "srv": [
        { "name": "_sip._tcp", "ttl": 400, "priority": 10, "weight": 60, "port": 5060, "target": "sipserver.educational.local." }
    ],
    "ptr": [
        { "name": "1.168.192.in-addr.arpa", "ttl": 400, "value": "educational.local." }
    ]
}

with open('educational.local.zone', 'w') as zone_file:
    json.dump(zone_data, zone_file, indent=4)
