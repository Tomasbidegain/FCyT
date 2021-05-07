Program cartas;

var
	i,num_carta1,num_carta2,cont_cartas: Integer;
	palo_carta1,palo_carta2: string;
	aux:Boolean;

begin
	cont_cartas:=0;
	aux:=false;
	writeln('Saque una carta.');
	writeln('');
	writeln('Ingrese el numero de la carta que acaba de sacar: ');
	readln(num_carta1);
	writeln('Ingrese el palo de la carta que acaba de sacar: ');
	readln(palo_carta1);
	writeln('Siga sacando cartas hasta encontrar una del mismo palo y mayor a la primera.');
	writeln('');
	writeln('Ingrese el numero de la carta que acaba de sacar:');
	readln(num_carta2);
	writeln('Ingrese el palo de la carta que acaba de sacar');
	readln(palo_carta2);
	if (palo_carta2 <> palo_carta1) then
	begin
		aux:=false;
	end;
		while (aux=false) do
		begin
			cont_cartas:=cont_cartas+1;
			if (palo_carta2 = palo_carta1) and (num_carta2 > num_carta1) then
			begin
				writeln('¡¡Encontro una carta del mismo palo y mayor que la primera!!');
				aux:=true;
			end
			else if (palo_carta2<>palo_carta1) then
			begin
				aux:=false;
			end;
		end;
	writeln('La cantidad de cartas que se sacaron del maso fueron: ',cont_cartas);
end.