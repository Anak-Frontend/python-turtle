from sketchpy import canvas

pen = canvas.sketch(x_offset=250)
pen.draw_fn("./banteng/bull-red", co=(212, 31, 38), mode=0)
pen.draw_fn("./banteng/bull-head", co=(0, 0, 0), mode=0, retain=True)
