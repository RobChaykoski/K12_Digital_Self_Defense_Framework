# K-5 Treasure Hunt Adventure

## Learning Objectives
- Discover live hosts on the network
- Identify open service ports
- Retrieve a flag from a public share

## Solution Walkthrough

### Step 1: Find Your Target Computer
First, let's see what computers are awake in our range.

```bash
ping <target_ip>
```

You should see responses like:
```
64 bytes from <target_ip>: icmp_seq=1 ttl=64 time=0.123 ms
```

### Step 2: Scan for Services
Now let's see what services are available on that computer.

```bash
nmap -p 80 <target_ip>
```

You should see:
```
PORT   STATE SERVICE
80/tcp open  http
```

### Step 3: Access the Treasure
Let's check out what's in the treasure room:

```bash
curl http://<target_ip>/treasure/map.txt
```

Or examine it with a browser at `http://<target_ip>`

## What You Learned
- How to find computers on a network using ping
- How to discover open services using nmap  
- How to access web content and retrieve files

## Success!
You found the treasure map! Great job explorer!
