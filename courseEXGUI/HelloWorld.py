
# -*- coding: utf-8 -*-

from editor import *
from remi.gui import *
from remi import start, App


class untitled(App):
    def __init__(self, *args, **kwargs):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        if not 'editing_mode' in kwargs.keys():
            super(untitled, self).__init__(*args, static_file_path={'my_res':'./res/'})

    def idle(self):
        #idle function called every update cycle
        pass
    
    def main(self):
        return untitled.construct_ui(self)
        
    @staticmethod
    def construct_ui(self):
        #DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        container0 = Container()
        container0.attr_class = "Container"
        container0.attr_editor_newclass = False
        container0.css_height = "315.0px"
        container0.css_left = "20px"
        container0.css_position = "absolute"
        container0.css_top = "20px"
        container0.css_width = "420.0px"
        container0.variable_name = "container0"
        label0 = Label()
        label0.attr_class = "Label"
        label0.attr_editor_newclass = False
        label0.css_font_size = "20px"
        label0.css_height = "45.0px"
        label0.css_left = "135.0px"
        label0.css_position = "absolute"
        label0.css_top = "105.0px"
        label0.css_visibility = "visible"
        label0.css_width = "195.0px"
        label0.text = "My label"
        label0.variable_name = "label0"
        container0.append(label0,'label0')
        button0 = Button()
        button0.attr_class = "Button"
        button0.attr_editor_newclass = False
        button0.css_height = "30px"
        button0.css_left = "135.0px"
        button0.css_position = "absolute"
        button0.css_top = "180.0px"
        button0.css_width = "100px"
        button0.text = "Hello World"
        button0.variable_name = "button0"
        container0.append(button0,'button0')
        container0.children['button0'].onclick.do(self.onclick_button0)
        

        self.container0 = container0
        return self.container0
    
    def onclick_button0(self, emitter):
        self.container0.children['label0'].set_text("Hello World")



#Configuration
configuration = {'config_project_name': 'untitled', 'config_address': '0.0.0.0', 'config_port': 8081, 'config_multiple_instance': True, 'config_enable_file_cache': True, 'config_start_browser': True, 'config_resourcepath': './res/'}

if __name__ == "__main__":
    # start(MyApp,address='127.0.0.1', port=8081, multiple_instance=False,enable_file_cache=True, update_interval=0.1, start_browser=True)
    start(untitled, address=configuration['config_address'], port=configuration['config_port'], 
                        multiple_instance=configuration['config_multiple_instance'], 
                        enable_file_cache=configuration['config_enable_file_cache'],
                        start_browser=configuration['config_start_browser'])
