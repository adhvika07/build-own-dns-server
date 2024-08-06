# build-own-dns

## Project Overview

This project demonstrates how to create a simple DNS server using Python. The server listens for DNS queries and responds with appropriate DNS records based on predefined zone files. The implementation includes handling various DNS record types and constructing proper DNS response packets.

## Files

### `main.py`
This is the main script that sets up and runs the DNS server. The key functionalities include:
- **Loading Zone Files**: Reads and parses DNS zone files to retrieve DNS records.
- **Parsing DNS Requests**: Interprets incoming DNS query packets.
- **Building DNS Responses**: Constructs DNS response packets based on the query and available records.
- **Socket Communication**: Listens for DNS queries on a specified port and sends back responses.

### `howcode.org.zone`
This is a zone file for the domain `howcode.org`. It includes:
- **SOA Record**: Start of Authority record, containing administrative information about the zone.
- **NS Records**: Nameserver records, specifying the authoritative DNS servers for the zone.
- **A Records**: Address records, mapping domain names to IP addresses.

## Getting Started

### Prerequisites

- Python 3.x
- Basic understanding of DNS concepts and networking

### Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/dns-server-python.git
    cd dns-server-python
    ```

2. **Install Required Libraries**:
    The project requires no external libraries other than Python's standard library.

### Running the Server

1. **Prepare Zone Files**:
    Ensure your zone files are placed in the `zones` directory. For this example, we have `howcode.org.zone`.

2. **Start the DNS Server**:
    ```sh
    python main.py
    ```

    The server listens on `127.0.0.1:53` (port 53 is the default port for DNS).

## Zone File Structure

Zone files are written in JSON format. Here is the structure of a typical zone file:

```json
{
    "$origin": "example.org.",
    "$ttl": 3600,
    "soa": {
        "mname": "ns1.example.org.",
        "rname": "admin.example.org.",
        "serial": "2024040601",
        "refresh": 3600,
        "retry": 600,
        "expire": 604800,
        "minimum": 86400
    },
    "ns": [
        { "host": "ns1.example.org." },
        { "host": "ns2.example.org." }
    ],
    "a": [
        { "name": "@", "ttl": 400, "value": "192.168.1.1" }
    ]
}
```

### Explanation of Fields

- **$origin**: The base domain for this zone.
- **$ttl**: The default time-to-live for records in this zone.
- **soa**: The Start of Authority record, containing essential information about the domain.
- **ns**: Nameserver records for the domain.
- **a**: Address records, mapping domain names to IP addresses.

## Code Explanation

### `main.py`

#### Key Functions

- **load_zones()**:
    Loads and parses all zone files in the `zones` directory into a dictionary.

- **getflags(flags)**:
    Constructs the flags portion of the DNS response.

- **getquestiondomain(data)**:
    Parses the domain name and query type from the DNS request.

- **getzone(domain)**:
    Retrieves the zone data for a given domain.

- **getrecs(data)**:
    Retrieves the DNS records for a given query.

- **buildquestion(domainname, rectype)**:
    Builds the DNS question section for the response.

- **rectobytes(domainname, rectype, recttl, recval)**:
    Converts a DNS record to bytes for inclusion in the response.

- **buildresponse(data)**:
    Constructs the entire DNS response packet.

#### Main Loop

The server runs an infinite loop, waiting for incoming DNS requests. Upon receiving a request, it processes the query and sends back a response.

```python
while True:
    data, addr = sock.recvfrom(512)
    response = buildresponse(data)
    sock.sendto(response, addr)
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.


## Acknowledgments

- Inspired by various online tutorials and the need to understand DNS server implementation: howcode.org


---

Feel free to modify and expand this README to fit the specifics of your project and personal preferences.
