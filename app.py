#!/bin/python3

import logging
import dearpygui.dearpygui as dpg
from app_actions import step_action, start_auto_mode, start_step_mode, stop_action


from app_tags import *


logging.basicConfig(filename='app.log', filemode='w', level=logging.DEBUG)


dpg.create_context()


with dpg.window(tag="primary-window"):

    dpg.add_text("Simulation Settings")

    dpg.add_separator()
    dpg.add_input_int(label="num. of sources",
                      tag=SETTINGS_NUM_SOURCES,
                      default_value=10,
                      min_value=1, min_clamped=True,
                      max_value=20, max_clamped=True)

    dpg.add_input_int(label="num. of devices",
                      tag=SETTINGS_NUM_DEVICES,
                      default_value=10,
                      min_value=1, min_clamped=True,
                      max_value=20, max_clamped=True)
    dpg.add_input_int(label="buffer capacity",
                      tag=SETTINGS_BUFFER_CAPACITY,
                      default_value=10,
                      min_value=1, min_clamped=True,
                      max_value=20, max_clamped=True)
    dpg.add_separator()
    dpg.add_spacer()
    dpg.add_separator()
    dpg.add_input_float(label="approx. generation freq.",
                        tag=SETTINGS_GENERATION_FREQ,
                        default_value=1.0,
                        min_value=0.1, min_clamped=True,
                        max_value=1.0, max_clamped=True,
                        step=0.1, format="%.1f")
    dpg.add_separator()
    dpg.add_spacer()
    dpg.add_separator()
    dpg.add_input_float(label="min. bid processing time",
                        tag=SETTINGS_MIN_PROCESSING_TIME,
                        default_value=20.0,
                        min_value=1.0, min_clamped=True,
                        max_value=100.0, max_clamped=True,
                        step=0.1,
                        format="%.1f")
    dpg.add_input_float(label="max. bid processing time",
                        tag=SETTINGS_MAX_PROCESSING_TIME,
                        default_value=80.0,
                        min_value=1.0, min_clamped=True,
                        max_value=100.0, max_clamped=True,
                        step=0.1, format="%.1f")
    dpg.add_separator()

    with dpg.window(label="Error", tag=ERROR_WINDOW, modal=True, show=False):
        dpg.add_text(ERROR_DEFAULT_MESSAGE, tag=ERROR_MESSAGE)

    with dpg.group(horizontal=True):
        dpg.add_button(label="start step mode", callback=start_step_mode)
        dpg.add_button(label="start auto mode", callback=start_auto_mode)

    with dpg.window(label="Event Calendar",
                    tag=EVENT_CALENDAR_WINDOW,
                    show=False,
                    width=300, height=300):

        with dpg.group(horizontal=True):
            dpg.add_button(label="step", tag=STEP_BUTTON, callback=step_action)
            dpg.add_button(label="stop", tag=STOP_BUTTON, callback=stop_action)

        dpg.add_spacer()
        dpg.add_group(tag=EVENT_CALENDAR_CONTENT_BLOCK)

    with dpg.window(label="Memory Buffer",
                    tag=MEMORY_BUFFER_WINDOW,
                    show=False,
                    width=300, height=300):

        dpg.add_group(tag=MEMORY_BUFFER_CONTENT_BLOCK)

    with dpg.window(label="Summary Table",
                    tag=SUMMARY_TABLE_WINDOW,
                    show=False,
                    width=300, height=300):

        dpg.add_group(tag=SUMMARY_TABLE_CONTENT_BLOCK)


dpg.set_primary_window(window="primary-window", value=True)

dpg.create_viewport(title='abc', width=854, height=480)
dpg.setup_dearpygui()
dpg.show_viewport()

dpg.start_dearpygui()
dpg.destroy_context()
