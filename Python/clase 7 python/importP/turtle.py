import turtle

window = turtle.screen() #abre una ventana y muestra los diferentes movimientos que hace
turtle.forward.screen(100)
turtle.right(90) 



# cuadrado

for i in range(4):
    turtle.forward.screen(100)
    turtle.right(90) 
    turtle.forward.screen(100)
    turtle.right(90) 
    
turtle.shape("turtle")
turtle.color("blue")
turtle.pencolor("green")    
window.mainloop()