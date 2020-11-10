# LightControlAmbilight
Setting the light of [LED strips](https://github.com/aul12/LightControlFirmware) to the average color of my monitor. The color is selected by taking a screenshot from a region of interest, bluring the image
and applying a median filter (implemented via resize and order), the final color is then smoothened using exponential smoothing.

Paramaters (i.e. ROI, blur, smoothing) are tuned for running [Zwift](https://zwift.com/) on a 1080p monitor.
