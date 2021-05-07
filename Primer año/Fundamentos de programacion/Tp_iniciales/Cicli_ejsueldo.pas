Program Sueldo;

var
	Suel, VH, HT: Real;

	I,J,Acus: Integer;

	 Prom: Real;

Begin
 
	
	begin
		
		For J:= 1 to 3 Do

			begin
				
				Acus:=0;

					For I:=1 to 10 do

					begin
						
						Writeln('Ingrese las horas trabajadas.');

						Readln(HT);

						Writeln('Ingrese el valor de las horas trabajadas.');

						Readln(VH);

						Suel:= VH*HT;

						Writeln('Su sueldo es de :$', Sueldo);

						Acus:=Acus+1;

					end;

				 Prom:= Acus/10;

				 Writeln ('El promedio de sueldo es:', Prom);

 			end;

	end;

end.