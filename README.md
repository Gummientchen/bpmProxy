# bpmProxy

![Example Screenshot of bpmProxy](assets/screenshot.png)  
This tool allows you to use [HeartRate](https://github.com/jlennox/HeartRate) to connect a heart beat sensor and display it in OBS with a browser source.

## Features

- Browser source for heartrate in OBS
- Heart animation based on heartrate (size and speed)
- Hides automatically if connection is lost. Reappears if connection is reestablished.

## Installation/Usage

First run:

1. Download HeartRate from their official GitHub Repository -> https://github.com/jlennox/HeartRate/releases
2. Start HeartRate. Right click on the HearRate icon in the taskbar tray and choose "Edit settings XML..."
3. Change the line `<UDP> </UDP>` to `<UDP>127.0.0.1:60900</UDP>`
   - Optional: you can disable alarms by changing the following Lines; `<AlertLevel>` and `<WarnLevel>` to a high number like 300
4. Save the file and close the editor.
5. Start bpmProxy
6. Add a browser source to any scene you want in OBS. Use the following URL: `http://127.0.0.1:8765/`
7. Set the **width** to 1920 and **height** to 1080.

Normal usage:

1. Start HeartRate
2. Start bpmProxy
3. Start OBS (or click the "refresh" button of your browser source if you had it already started)

## Customizing styles

In the OBS browser source you can change some CSS to adjust the styling of the heart beat:

`.heart path { fill: #e00 }` to change the color of the animated heart  
`.bpm-number { color:#eee }` to change the text color of the heart beat number

### Example Styles

Green Heart, Font "Tahoma"

```css
body {
  background-color: rgba(0, 0, 0, 0);
  margin: 0px auto;
  overflow: hidden;
}
.heart path {
  fill: #0e0;
}
.bpm-number {
  font-family: "Tahoma";
}
```

---

## TODO

- ...

---

## Version History

### v0.2

- Changed from Cardia to [HeartRate from Joseph Lennox](https://github.com/jlennox/HeartRate).
- Heartrate now gets hidden if connection with HeartRate is lost.

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

## Thanks to the following people

Many thanks to [Joseph Lennox](https://github.com/jlennox) for implementing the UDP functionality into HeartRate for me.
