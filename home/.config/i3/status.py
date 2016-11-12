#!/usr/bin/env python3

from i3pystatus import Status
import netifaces

st = Status()

#NOTE# modules show up right-to-left

st.register('clock', format=('%Y-%m-%d %H:%M:%S'))

st.register("battery",
    not_present_text="",
    #format="{status} {consumption:.1f}W {percentage:.0f}% [{percentage_design:.0f}%] {remaining:%E%hh:%Mm}",
    format="{status} {consumption:4.1f}W {remaining:%E%h:%M} {percentage:.0f}%",
    alert=False, #TODO# Enable later. alert_percentage=5,
    status={"DIS": "↓", "CHR": "↑", "FULL": "⤒",}, #"FULL": "⥍ ⇞ ☢",}
#    status={"DIS": "⇂", "CHR": "↿", "FULL": "⥍",},
#    status={"DIS": "⇂", "CHR": "↿", "FULL": "⥮",},
)

try:
    st.register('backlight', backlight='intel_backlight', format='☀{percentage:3.0f}%') #TODO# make portable
except FileNotFoundError: # there is no intel_backlight
    pass

# Note: requires both netifaces and basiciw (for essid and quality)
wl = next((i for i in netifaces.interfaces() if i.startswith('wl')), None)
if wl:
    st.register("network", interface=wl,
        format_up="{essid} {quality:.0f}%")

st.register("disk", path="/media/data", format="data {avail:.0f}G",)

st.register("disk", path="/", format="root {avail:.0f}G",)

st.register('temp', format='{temp:.0f}°C')

st.register('load')

st.register('clock', format=('%Y-%m-%d %H:%M:%S UTC', 'UTC'))

st.run()
