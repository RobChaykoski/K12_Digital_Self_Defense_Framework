# K-5 Enhanced Exercise: Digital Treasure Hunt Adventure

## Learning Objectives

By completing this adventure, students will:

- Learn to discover computers on a network using ping
- Identify open services using nmap scanning
- Retrieve files from web servers and shared directories
- Understand that digital information can be protected with flags

## Adventure Story

Welcome to the K-5 Cyber Range, brave explorer! 🌟

You've been chosen for an important mission: find the legendary Digital Treasure Map that's hidden somewhere in our secure range! This treasure map will help you discover even more exciting adventures.

Your journey begins with simple tools. Don't worry - we'll guide you through each step!

## Solution Walkthrough

### Step 1: Discover Your Target

First, let's see if there are any computers around us that might have the treasure.

In your terminal, type:

```
ping <target_ip>
```

You should see responses like:

```
64 bytes from <target_ip>: icmp_seq=1 ttl=64 time=0.123 ms
```

### Step 2: Scan for Services

Now that we know there's a computer awake, let's see what services it's offering.

Type:

```
nmap -p 80 <target_ip>
```

You should see something like:

```
PORT   STATE SERVICE
80/tcp open  http
```

### Step 3: Access the Treasure Room

Great! We found an HTTP service. Let's check what's inside the treasure room:

```
curl http://<target_ip>/treasure/map.txt
```

Or open it in your browser at `http://<target_ip>/treasure/`

### Step 4: Capture Your Flag

You found the treasure map! The flag is: `OCR{treasure_map_found}`

Submit this to complete your mission!

## What You Learned

- How to find computers on a network using ping
- How to discover open services using nmap
- How to access web content and retrieve files
- That digital treasure can be protected with special "flags"

## Success!

Congratulations, young explorer! You've completed your first mission in the K-5 Cyber Range. You're now a certified Digital Detective!

---

*This exercise was created for OpenCyberRange - Educational Cybersecurity Platform*