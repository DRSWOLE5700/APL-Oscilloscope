import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib.animation as animation
from ArduinoInput import oscilloscope_input

trigger_voltage = 1

class CustomGraph(animation.TimedAnimation):
    def __init__(self):
        
        time_interval = 90 
        #   trigger_voltage = 1
        
        self.n = np.linspace(0, time_interval, time_interval + 1)
        self.y = []
        #self.y = np.zeros(self.n.size)
        print(self.y)
        #print('ho')
        # The window
        self.fig = plt.figure()
        ax1 = self.fig.add_subplot(1, 2, 1)
        self.mngr = plt.get_current_fig_manager() 
        self.mngr.window.setGeometry(100,200,800, 600)

        # ax1 settings
        ax1.set_xlabel('time')
        ax1.set_ylabel('raw data')
        self.line1 = Line2D([], [], color='blue')
        ax1.add_line(self.line1)
        ax1.set_xlim(0, time_interval)
        ax1.set_ylim(-3, 1027)


        animation.TimedAnimation.__init__(self, self.fig, interval=20, blit=True)

#04/25/22:
#Good news: I can graph my own function point by point, whatever that function may be.  I am currently
#calling oscilloscope_input from ArduinoInput.py, but I can change that when we hook up the actual analog
#input from the Arduino.  Now, I need to figure out how to use the trigger voltage (i.e. start the graph 
#at a specific y-intercept of voltage).


    def _draw_frame(self, framedata):
        #boolean = False
        i = framedata
        #print(i)
        x_data = self.n[0:i]
        #print(x_data)
        #if abs(oscilloscope_input()-trigger_voltage) < 0.1:
	
        while True:
            a = oscilloscope_input()
            if a.isdigit() and  a != '':
                self.y.append(np.float(a))
                break

        #    g = True
        y_data = self.y[0:i]
        print(y_data)
        #print(type(self.y)  )
        #print(float(oscilloscope_input()))
        #print("\033[1;32;40m yo")      It would be nice to use ANSI escape codes to tell the status of the application
        #print(self.y)
        
        
        self.line1.set_data(x_data, y_data)
        self._drawn_artists = [self.line1]

    def new_frame_seq(self):
        return iter(range(self.n.size))
        

    def _init_draw(self):
        lines = [self.line1]
        for l in lines:
            l.set_data([], [])
        print('hi')
        self.y = []

    def showMyAnimation(self):
        plt.show()


    ''' End Class '''


if __name__== '__main__':
    print("Define myGraph")
    myGraph = CustomGraph()
    myGraph.showMyAnimation()

