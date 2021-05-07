Program Veter;

	var
		opcion, i, codigo, edad, contp, acumep : Integer;
		cuota:real;
		nombre_de_mascota, especie: String;
		sucursal_mayor_recaudacion, promedio_edad_perros: integer;
		total_suc, recaudacion_veterinaria, recaudacion_sucursal: real;	
		begin
			contp := 0;
			acumep := 0;
			recaudacion_veterinaria:=0;
			sucursal_mayor_recaudacion:=0;
			promedio_edad_perros := 0;

			for i:= 1 to 4 do
				begin
				//writeln('HOLA');
					recaudacion_sucursal := 0;
					//opcion:=1;
					writeln('ingrese una opcion para continuar');
					readln(opcion);
					while (opcion <> 0) do
						begin
							writeln('Cargue los siguientes datos.');
							write('Ingrese el codigo: '); readln(codigo);
							write('Ingrese la edad de su mascota: '); readln(edad);
							write('Ingrese el nombre de su mascota: '); readln(nombre_de_mascota);
							write('Ingrese la especie de su mascota: '); readln(especie);
							write('Ingrese su cuota: '); readln(cuota);
							
							writeln('Mascota');
							writeln('Codigo: ', codigo);
							writeln('Nombre: ', nombre_de_mascota);
							writeln('Edad: ', edad, 'años');
							writeln('Especie: ', especie);
							writeln('Cuota: ', cuota:2:2);
					
							//Contamos perros y acumulamos sus edades
							if (especie = 'Perro') or (especie = 'perro') then
								begin
									contp := contp + 1;
									acumep := acumep + edad;
								end;
							
							recaudacion_sucursal := recaudacion_sucursal + cuota;

							if (sucursal_mayor_recaudacion < recaudacion_sucursal) then
								begin
									sucursal_mayor_recaudacion := i;
									total_suc := recaudacion_sucursal;
								end;
							writeln('¿Desea continuar? 1/0');
							readln(opcion);
						end;
					
					recaudacion_veterinaria:= recaudacion_veterinaria + recaudacion_sucursal;

					writeln('El promedio de edad de perros de la sucursal ', i , ' es: ', (acumep/contp):2:2);
				end;
				
				writeln('La sucursal con mayor recaudacion recaudo: ', sucursal_mayor_recaudacion);
				writeln('La recaudacion de la sucursal ', i ,'es: ', recaudacion_sucursal:2:2);
				writeln('El monto de recaudacion por veterinaria es: $', recaudacion_veterinaria:2:2);
		end.

