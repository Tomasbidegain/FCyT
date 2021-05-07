Program parcial;

uses crt;

const
	n = 3;

var
	edad,goles_conv,tarjetas_rojas,i,cont_jugadores,ac_tarjetas,ac_goles,ac_edad,max_gol,max_gol_supremo,club_max,club: Integer;
	ape_nom,tecla, max_nom,max_nom_supremo:string;
	prom_edad:real;

begin
	i:=0;
	club_max:=0;
	max_nom_supremo:='';
	max_gol_supremo:=0;
	club:=0;

	for i:=1 to n do
	begin
		writeln('#CLUB:', i);
		writeln('#Ingrese una tecla para comenzar.');
		readln;
		read(tecla);
		max_gol:=0;
		max_nom:='';
		ac_tarjetas:=0;
		ac_edad:=0;
		ac_goles:=0;
		cont_jugadores:=0;
			while (tecla <> '') do
			begin
				readln;
				write('Ingrese su apellido y nombre: ');
				readln(ape_nom);

				write('Ingrese su edad: ');
				read(edad);
				write('Ingrese la cantidad de goles convertidos: ');
				read(goles_conv);
				write('Ingrese la cantidad de tarjetas rojas: ');
				read(tarjetas_rojas);
				clrsc;
				writeln('Listado: ', ape_nom);
				if (ape_nom = 'Rodriguez James') then
				begin
					writeln('James Rodriguez es jugador del club ',i);
				end;
				cont_jugadores:= cont_jugadores + 1;
				ac_tarjetas:= ac_tarjetas + tarjetas_rojas;
				ac_goles:= ac_goles + goles_conv;
				ac_edad:=ac_edad + edad;

				if (max_gol < goles_conv) then
				begin
					max_gol:=goles_conv;
					max_nom:=ape_nom;
				end;
				readln;
				writeln('#Ingrese una tecla para continuar.');
				read(tecla);
			end;
		
		if (club_max < ac_goles) then
		begin
			club_max:= ac_goles;
			club:=i;
		end;
        
		if (max_gol_supremo < max_gol) then
		begin
		max_gol_supremo:=max_gol;
		max_nom_supremo:=max_nom;
		end;

		prom_edad:= (ac_edad / cont_jugadores);
		writeln('La cantidad de jugadores en el club ',i, ' son: ',cont_jugadores);
		writeln('La cantidad de tarjetas rojas en el club' ,i ,' es de: ',ac_tarjetas);
		writeln('La cantidad de goles convertidos en el club ', i ,' es de: ',ac_goles);
		writeln('La edad promedio de el club N° ',I,'  es ', prom_edad:2:2);
		readkey;
		clrsc;
	end;
	writeln('**Resultado final**');
	writeln('El jugador que mas goles convirtio de los 3 clubes es: ', max_nom_supremo ,' con ', max_gol_supremo, ' goles.');
	writeln('El club con mas goles convertidos es el N°: ', club);
end.