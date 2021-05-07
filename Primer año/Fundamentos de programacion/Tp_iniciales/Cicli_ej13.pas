Program obreros;

Var 
	I,Sec,edad,NumEm:Integer;

	Sec1, Sec2, Sec3, Sec4, Sec5: integer;

	Promed1, Promed2, Promed3, Promed4, Promed5: integer;

Begin
	Sec1:=0;

	Sec2:=0;
	
	Sec3:=0;
	
	Sec4:=0;
	
	Sec5:=0;
	
	Promed1:=0;
	
	Promed2:=0;
	
	Promed3:=0;
	
	Promed4:=0;
	
	Promed5:=0;
	
	For I:=1 to 10 do 
	
		begin
		
			Writeln('Ingrese la seccion a la que pertenece.');

			readln(Sec);

			Writeln('Ingrese su numero de empleado.');

			readln(NumEm);

			Writeln('Ingrese su edad');

			readln(edad);

		end;

		begin
		
		 case Sec of

				
			1:
			begin
				 Sec1:= Sec1+1;

			   	Promed1:=Promed1+edad;
			end;

			

			2: 

			begin

				Sec2:= Sec2+1;

				Promed2:= Promed2+edad;

			end;
			
				
			3: 

			begin

				Sec3:= Sec3+1;
				Promed3:= Promed3+edad;

			end;
			
				
			4: 

			begin

				Sec4:= Sec4+1;
				Promed4:= Promed4+edad;

			end;

				
			5:

			begin

				Sec5:= Sec5+1;

				Promed5:= Promed5+edad;
			end;

		end;
	
	end;
		
	Writeln('La cantidad de empleados en la seccion 1 son: ', Sec1);

	Writeln('La edad promedio en la seccion 1 es de: ', Promed1/sec1);

	Writeln('La cantidad de empleados en la seccion 2 son: ', Sec2);

	Writeln('La edad promedio en la seccion 2 es de: ', Promed2/sec2);

	Writeln('La cantidad de empleados en la seccion 3 son: ', Sec3);

	Writeln('La edad promedio en la seccion 3 es de: ', Promed3/sec3);

	Writeln('La cantidad de empleados en la seccion 4 son: ', Sec4);

	Writeln('La edad promedio en la seccion 4 es de: ', Promed4/sec4);

	Writeln('La cantidad de empleados en la seccion 5 son: ', Sec5);

	Writeln('La edad promedio en la seccion 5 es de: ', Promed5/sec5);

end.



