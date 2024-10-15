
# torProxy

Is a tool for Windows that allows automatic IP rotation using the Tor proxy,ensuring greater anonymity and privacy when browsing or making requests over the internet. It makes use of Tor's auto-restart system to periodically change the IP address, providing an additional layer of protection and making tracking more difficult.


## Features

- Automatically rotate IP at defined time intervals.
- Use SOCKS5 proxies to redirect your network traffic via Tor.
- Easily integrate the script into other automations that require anonymity or frequent IP switching.
- Operate in Windows environment with native support.
  
## How to install?
Download [Tor Browser](https://www.torproject.org/download/) and [Python](https://www.python.org/downloads/). <br />
Open your command prompt and write.

```bash
  pip install requests
  open main.py and edit 'tor_path' to your tor.exe path
  python main.py
```

## Usage
To use this rotating tor proxy system, just use '127.0.0.1:9050' as a proxy. (socket5)

## Screenshot

[ProgramScreenShot](https://github.com/y9b/torProxy/blob/main/screenshot.png?raw=true)

