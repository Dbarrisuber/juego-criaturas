#include <iostream>
#include <string>
class Pocion{public: std::string nombre; int curacion;
Pocion(std::string miNombre, int miCuracion)
{nombre=miNombre;
curacion=miCuracion;}};
class Jugador{public: int vida;std::string nombre;
void recibirCuracion(int cantidad)
{vida+=cantidad;}
Jugador(std::string miNombre,int miVida )
{vida=miVida;
nombre=miNombre;}};
void usarPocion(Pocion*miPocion, Jugador*miJugador)
{miJugador->recibirCuracion(miPocion->curacion);
std::cout<<"He usado la pocion"<<std::endl;}
int main()
{Jugador miJugador("David",50);
Pocion miPocion("Pocion Mayor",50);
usarPocion(&miPocion,&miJugador);
std::cout<<"La vida del jugador es:"<<miJugador.vida<<std::endl;}















