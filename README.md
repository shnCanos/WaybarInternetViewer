# WaybarInternetViewer



Probably my worst code yet.

This is a simple, written in python, internet viewer for waybar. The code is absolutely awful and I have absolutely no idea whether it actually works or even how it works (I just used random libraries) so use at your own discretion.

This is extremely small, only twelve lines, so you can see it yourself!

It depends on psutil so yeah

```bash
pip install psutil
```

An example waybar configuration:

```
"custom/internet": {
		"format": "{}",
		"exec": "python -u ~/main.py"
	},
```

And welp, have fun. (I think another person had already done this but better in every aspect, so you might want to check that out)
