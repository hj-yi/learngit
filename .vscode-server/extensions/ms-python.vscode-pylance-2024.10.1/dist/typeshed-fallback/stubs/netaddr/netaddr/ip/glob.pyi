from typing_extensions import TypeGuard

from netaddr.ip import IPAddress, IPNetwork, IPRange, _IPAddressAddr, _IPNetworkAddr

def valid_glob(ipglob: object) -> TypeGuard[str]: ...
def glob_to_iptuple(ipglob: str) -> tuple[IPAddress, IPAddress]: ...
def glob_to_iprange(ipglob: str) -> IPRange: ...
def iprange_to_globs(start: _IPAddressAddr, end: _IPAddressAddr) -> list[str]: ...
def glob_to_cidrs(ipglob: str) -> list[IPNetwork]: ...
def cidr_to_glob(cidr: _IPNetworkAddr) -> str: ...

class IPGlob(IPRange):
    def __init__(self, ipglob: str) -> None: ...
    @property
    def glob(self) -> str: ...
    @glob.setter
    def glob(self, value: str) -> None: ...
