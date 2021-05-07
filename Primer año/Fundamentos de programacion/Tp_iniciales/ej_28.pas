Program Dias;
Var dia:1..7;
begin

writeln('Ingrese un numero del 1 al 7 para saber que dia de la semana le corresponde');

begin
readln(dia);
end;

Case dia of

	1: writeln ('El primer dia de la semana es: Domingo');
	2: writeln ('El segundo dia de la semana es: Lunes');
	3: writeln ('El tercer dia de la semana es: Martes');
	4: writeln ('El cuarto dia de la semana es: Miercoles');
	5: writeln ('El quinto dia de la semana es: Jueves');
	6: writeln ('El sexto dia de la semana es: Viernes');
	7: writeln ('El septimo dia de la semana es: Sabado');

 
Else
	begin
	writeln ('El numero que ingreso no corresponde a ningun dia');
 	end;
end;
end.