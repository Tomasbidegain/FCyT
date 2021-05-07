Program Empleados;
var
	ae, edad: Integer;
	I: Integer;
	CL,CD: Integer;
	puesto, titulo, apynom: String;

	begin
		ae:=0;
		CL:=0;
		CD:=0;
		
			For I:=1 to 92 do
		begin
		 writeln('ingrese su apellido y nombre');
		 readln(apynom);
		 writeln('ingrese su puesto');
		 readln(puesto);
		 
		
		 	if puesto='desarrollador'then;
		 	CD:=CD+1;
		 writeln('ingrese su titulo');
		 readln(titulo);
		 	if titulo='Lic. en sistemas de inf.' then
		 	CL:=CL+1;
		 writeln('ingrese su edad');
		 readln(edad);
		 end;

		 writeln('el promedio de edades es:', (ae*edad)/92);
		 writeln('La cantidad de Desarrolladores son:', CD);
		 writeln('La cantidad de Lic. en sistemas de inf. son:', CL);
		 
		 
	end.