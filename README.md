# BPM Proxy

## Version History

### v0.1

First Version. This is basically a proof of concept. It allows you to use Cardia to get the heartbeat of a compatible heartbeat sensor (like Polar H10) and integrate it into OBS with a browser source.

## Installation/Usage

Download Cardia from their official GitHub Repository -> https://github.com/uwburn/cardia/releases

Start Cardia and go to "Log". Enable logging and choose "UDP" as the log format. Use IP address "127.0.0.1" and Port "60900".

Start bpmProxy.exe

Add a browser source to any scene in OBS. Use the following **URL**: `http://127.0.0.1:8765/`  
Set the **width** to 1920 and **height** to 1080.

## Resources used

- https://gist.github.com/artizirk/04eb23d957d7916c01ca632bb27d5436
- https://gist.github.com/xposedbones/75ebaef3c10060a3ee3b246166caab56
- https://docs.w3cub.com/dom/keyframeeffect
- https://codepen.io/rachelnabors/pen/eJyWzm/?editors=0010
