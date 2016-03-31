
import math

# *_BORDER_WIDTH is the width INCLUDING the border.
STOKE_BORDER_WIDTH   = 4.5
STOKE_BORDER_COLOR   = "#666"
STOKE_UNFILLED_COLOR = "#eee"
STOKE_UNFILLED_WIDTH = 3
STOKE_FILLING_COLOR  = "#f00"
STOKE_FILLED_COLOR   = "#000"
STOKE_FILLED_WIDTH   = 3.1

SHOW_BRUSH              = True
SHOW_BRUSH_FRONT_BORDER = True
BRUSH_COLOR        = "#f00"
BRUSH_WIDTH        = 5.5
BRUSH_BORDER_COLOR = "#666"
BRUSH_BORDER_WIDTH = 7

WAIT_AFTER = 1.5

DELETE_TEMPORARY_FILES = True
GIF_SIZE               = 200
GIF_FRAME_DURATION     = 0.045

GENERATE_SVG           = True
GENERATE_JS_SVG        = True
GENERATE_GIF           = False

# sqrt, ie a stroke 4 times the length is drawn
# at twice the speed, in twice the time.
def stroke_length_to_time(length):
    return math.sqrt(length)/8

# global time rescale, let's make animation a bit
# faster when there are many strokes.
def time_rescale(interval):
    return math.pow(3 * interval, 2.0/3)

# Possibilities are linear, ease, ease-in, ease-in-out, ease-out, see
#   https://developer.mozilla.org/en-US/docs/Web/CSS/timing-function
# for more info.
TIMING_FUNCTION = "ease-in-out"

#
# colorful debug settings
#
#STOKE_BORDER_COLOR   = "#00f"
#STOKE_UNFILLED_COLOR = "#ff0"
#STOKE_FILLING_COLOR  = "#f00"
#STOKE_FILLED_COLOR   = "#000"
#BRUSH_COLOR = "#0ff"
#BRUSH_BORDER_COLOR = "#0f0"
