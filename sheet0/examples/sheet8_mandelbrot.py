from Tkinter import *
import random

class Gui(object):
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Mandelbrot-Menge")
        self.start = (-1.04072265625+0.4012890625j)
        self.end = (-1.02119140625+0.3817578125j)
        self.start = -1.5+1j
        self.end = 0.5-1j

        self.iterations = 50

        # Setup the canvas
        self.pointsize = 2
        self.size = 200
        self.canvas = Canvas(self.parent, width=self.pointsize*self.size, height=self.pointsize*self.size)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.mouseCanvasPressed)

        # Setup other widgets
        self.resetButton = Button(self.parent, text='reset')
        self.resetButton.configure(command=self.resetButtonPressed)
        self.resetButton.pack()

        self.drawMandelbrot()

    def resetButtonPressed(self):
        self.start = -1.5+1j
        self.end = 0.5-1j
        self.drawMandelbrot()

    def mouseCanvasPressed(self, event):
        """  Zoom in """
        x, y = event.x, event.y
        scale = 1/5.0  # Zoom-faktor

        scale_x = complex((self.end-self.start).real/(self.size*self.pointsize), 0)
        scale_y = complex(0, (self.end-self.start).imag/(self.size*self.pointsize))

        # Mitte = Punkt wo die Maus geklickt worden ist, konvertiert ins Komplexe
        mitte = self.start + x*scale_x + y*scale_y
        width = abs((self.end-self.start).real * scale)
        height = abs((self.end-self.start).imag * scale)

        # Rotes Rechteck um Mitte
        a = (self.size * scale * 0.5 * self.pointsize)
        self.canvas.create_rectangle(x-a, y-a, x+a, y+a, fill='', outline='red')

        # Update start and endpunkt
        self.start = mitte - 0.5 * width + 0.5j * height
        self.end = mitte + 0.5 * width - 0.5j * height

        self.drawMandelbrot()

    def getColor(self, c):
        if not 0 <= c <= self.iterations:
            # Fehler wird rot ausgegeben
            return '#FF0000'

        # Farbe am Anfang (c = 0)
        r1, g1, b1 = 255, 255, 255
        # Farbe am Ende (c = iterations)
        r2, g2, b2 = 0, 0, 0

        r = (r2 - r1)*c/self.iterations + r1
        g = (g2 - g1)*c/self.iterations + g1
        b = (b2 - b1)*c/self.iterations + b1

        return '#%02x%02x%02x' % (r, g, b)

    def drawMandelbrot(self):

        start = self.start
        end = self.end

        print "drawing mandelbrot! ", start, end

        scale_x = complex((end-start).real/self.size, 0)
        scale_y = complex(0, (end-start).imag/self.size)

        for y in range(self.size):
            for x in range(self.size):
                z = 0j
                c = start + x*scale_x + y*scale_y
                for count in range(self.iterations):
                    if abs(z) <= 2:
                        z = z * z + c
                    else:
                        break
                color = self.getColor(count)
                ps = self.pointsize
                self.canvas.create_rectangle(x*ps, y*ps, x*ps + ps, y*ps + ps, fill=color, outline=color)

            if y % 32 == 0:
                root.update()

root = Tk()
app = Gui(root)
root.mainloop()
