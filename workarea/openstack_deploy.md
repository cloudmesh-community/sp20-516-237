# Deploy openapi to OpenStack

1. Get set up locally
```pip install -U cloudmesh-installer```

```cloudmesh-installer get openstack```

2. Check set up

```cms openstack```

```cms help vm```

- to checck that I can connect to chameleon

```cms vm list --refresh```

```cms config get default.cloud```
   - output:  cloudmesh.default.cloud=chameleon


3. Start up VM

4. Try to run shell commands on VM

5. Try to install openapi on VM  (install pre-reqs like python 3.8 and pip 20.x)

6. Try to run cpu example
