from docker import from_env

client = from_env()

# start a tiny web container on port 8082
name = "ux-hello"
# clean if exists
try:
    client.containers.get(name).remove(force=True)
except:
    pass

c = client.containers.run(
    "nginx:alpine",
    name=name,
    detach=True,
    ports={"80/tcp": 8082},
)
print("started:", c.name, c.status)

# list
for cont in client.containers.list(all=True):
    if cont.name.startswith("ux-"):
        print("found:", cont.name, cont.status)

