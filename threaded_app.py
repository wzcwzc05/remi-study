"""
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import remi.gui as gui
from remi import start, App
import threading
import time


class MyApp(App):
    def __init__(self, *args):
        super(MyApp, self).__init__(*args)

    def idle(self):
        # this function is called automatically by remi library at specific interval
        # so here I can assign values to widget
        self.lbl.set_text('Thread result:' + str(self.my_thread_result))

    def main(self):
        print("Hello World")
        # margin 0px auto allows to center the app to the screen
        wid = gui.VBox(width=300, height=200, margin='0px auto')
        self.lbl = gui.Label('Thread result:', width='80%', height='50%')
        self.lbl.style['margin'] = 'auto'

        bt = gui.Button('Start algorithm', width=200, height=30)
        bt2 = gui.Button('Stop', width=200, height=30)
        bt.style['margin'] = 'auto 50px'
        bt.style['background-color'] = 'red'
        bt2.style['margin'] = 'auto 50px'
        bt2.style['background-color'] = 'red'

        wid.append(self.lbl)
        wid.append(bt)
        wid.append(bt2)
        
        self.thread_alive_flag = False
        self.my_thread_result = 0
        # Here I start a parallel thread that executes my algorithm for a long time
        t = threading.Thread(target=self.my_intensive_long_time_algorithm)
        t.start()

        bt.onclick.do(self.on_button_pressed)
        bt2.onclick.do(self.on_button2_pressed)

        # returning the root widget
        return wid

    def my_intensive_long_time_algorithm(self):
        while self.thread_alive_flag:
            time.sleep(0.2)
            self.my_thread_result = self.my_thread_result + 1

    def on_button_pressed(self, emitter):
        self.my_thread_result=0
        self.thread_alive_flag = True
        t = threading.Thread(target=self.my_intensive_long_time_algorithm)
        t.start()
    
    def on_button2_pressed(self, emitter):
        self.thread_alive_flag = False
        print(self.my_thread_result)

    def on_close(self):
        self.thread_alive_flag = False
        print("On Closing!")
        super(MyApp, self).on_close()


if __name__ == "__main__":
    start(MyApp, debug=True, address='0.0.0.0', port=0, update_interval=0.1)
