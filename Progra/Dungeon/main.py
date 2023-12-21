

from MapGrid import MapGrid
mapa = MapGrid(30,15)
mapa.get_walls(porcentaje=0.9)
mapa.draw_grid()
while mapa.is_final():
    move= input("Introduce: w,a,s o d para moverte\n>")
    mapa.move_player(move)

print("Felicidades, completaste la mazmorra")