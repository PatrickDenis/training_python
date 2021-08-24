import jinja2
  
bgp_vars = {
    "peers1_ip": "10.255.255.2",
     "peers1_ip": "20",
}
 
bgp_template = '''
feature bgp
router bgp 10
    address-family ipv4 unicast
        netw 10.10.200.1.0/24
    neigh   {{ peer1_ip }} remote-as {{ peer1_as }}
    update-source lo1
    ebgp-multihop 2
    address-family ipv4 unicast
'''
t = jinja2.Template(bgp_template)
print(t.render(bgp_vars))

