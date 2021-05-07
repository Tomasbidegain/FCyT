Program Cartas;

uses crt;

Var

	Cont: Integer;

	Car1, Car2: 1..12;

	Palo1, Palo2: String;

Begin

	Writeln ('Ingrese el numero de una carta.');

	Readln(car1);

	writeln ('Ingrese el palo de la carta.');

	Readln(Palo1);

	Writeln('Ingrese el numero de una segunda carta.');

	Readln(Car2);

	Writeln('Ingrese el palo de la segunda carta.');

	Readln(palo2);
	cont:=1;

		While ((car1>Car2) or (Palo1<>Palo2)) do

			begin 
				
				Cont:=Cont+1;

				writeln('Ingrese el numero de una siguiente carta.');

				readln(Car2);

				Writeln('Ingrese el palo de la siguiente carta.');

				readln(Palo2);
			end;

	Writeln('La cantidad de cartas que fueron necesarias extraer del maso es: ' , cont);

	Readkey;

end.
