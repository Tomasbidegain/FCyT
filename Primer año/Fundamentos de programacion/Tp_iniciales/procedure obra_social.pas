program obra_social;

var
	apynom,tecla:string;
	edad,i,afiliados,cont_edad,max_edad,obra:integer;
	monto_aportado,monto_total: real;

procedure cargar_datos(var apynom:string; var edad: integer; var monto_aportado:real);
begin
	writeln('ingrese apellido y nombre : ');
	readln(apynom);
	writeln'(ingrese su edad');
	readln(edad);
	writeln('Ingrese monto aportado: ');
	readln(monto_aportado);
end;

begin
	max_edad:=0;
	obra:=0;
	for i:= 1 to 3 do 
	begin
		afiliados:=0;
		cont_edad:=0;
		monto_total:=0;
		writeln('ingrese un tecla para cargar: ');
		readln(tecla);
		while (tecla <> ' ') do 
		begin
			cargar_datos(apynom,edad,monto_aportado);
			inc(afiliados);
			monto_total:= (monto_total + monto_aportado);
			if (edad = 65) then
			begin
				inc(cont_edad);
			end;
			writeln('ingrese una tecla para seguir cargando afiliados: ');
			readln(tecla);
		end;
		writeln ('Afiliados de la obra social N° ',i,' es: ',afiliados);
		writeln('El monto total aportado para la obra social N° ',i,' es: ',monto_total:2:0);
		if max_edad < cont_edad then
		begin
			max_edad:= cont_edad;
			obra:= i;
		end;
		writeln('La obra social con mas afiliados mayores a 65 años es la obra N° ', obra,' con ',max_edad,' afiliados ');
	end;