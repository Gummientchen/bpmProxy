# bpmProxy

![Example Screenshot of bpmProxy](assets/screenshot.png)  
This tool allows you to use [Cardia](https://github.com/uwburn/cardia) to connect a heart beat sensor and display it in OBS with a browser source.

## Installation/Usage

1. Download Cardia from their official GitHub Repository -> https://github.com/uwburn/cardia/releases
1. Start Cardia and go to "Log". Enable logging and choose "UDP" as the log format. Use IP address "127.0.0.1" and Port "60900".
1. Press the "Start" button in Cardia.
1. Start bpmProxy.exe
1. Add a browser source to any scene in OBS. Use the following URL: `http://127.0.0.1:8765/`
1. Set the **width** to 1920 and **height** to 1080.

## Customizing styles

In the OBS browser source you can change some CSS to adjust the styling of the heart beat:

`.heart path { fill: #e00 }` to change the color of the animated heart  
`.bpm-number { color:#eee }` to change the text color of the heart beat number

---

## Version History

### v0.1

First Version. This is basically a proof of concept. It allows you to use [Cardia](https://github.com/uwburn/cardia) to get the heartbeat of a compatible heartbeat sensor (like Polar H10) and integrate it into OBS with a browser source.

---

## How to build

1. Install Python 3.10
2. Install all dependencies with `pip install -r requirements.txt`
3. Run `pyinstaller bpmProxy.spec`

## Resources used

- https://gist.github.com/artizirk/04eb23d957d7916c01ca632bb27d5436
- https://gist.github.com/xposedbones/75ebaef3c10060a3ee3b246166caab56
- https://docs.w3cub.com/dom/keyframeeffect
- https://codepen.io/rachelnabors/pen/eJyWzm/?editors=0010
