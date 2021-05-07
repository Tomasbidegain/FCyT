Program vocals;

var CadenaVo: String;

	R:integer;

	g, S:integer;

	X,z: boolean;



	procedure longitudes(Cadena:string; var R, S:integer);
	
		begin

			R:= Length(cadena);

			s:= R

		end;

	procedure vocal(Cadena:string; var S,G:integer);
	
		var

		I: Integer;

		G:integer
	
	begin

			begin

				For I:= 1 to S do


				If (cadena='a') and (Cadena='e') and (cadena='i') and (cadena='o') and (cadena = 'u') then

				Contador := Contador+1;

				

			end;
			G:=contador
	end;

	procedure mayus(cadena:String; var S:integer,x:boolean);

	var
		J: Integer;
		x: boolean;

		begin

			

				for J:= 1 to S do

			
					
				if (cadena='a') then

				 X:= true

				 else

				 x:=false
			  	 	
		end;

	procedure minus(cadena:string; var s:integer,z:boolean);

	var
		F: Integer;

		z: boolean;
		begin

			for F:=1 to S do

			if (cadena='A') then

			z:=true

			 else
			 
			 z:=false
		end;
				  
begin

	write('ingrese una cadena de caracteres:');

	readln (CadenaVo);

	longitudes(cadenavo, R, S);

	vocal (Cadenavo,S,G);

	minus(cadenavo, s, z);

	mayus(cadenavo,s, x);


	writeln('la cantidad de letras que tiene la cadena que ingreso son :', S);

	writeln('la cantidad de vocales que tiene la cadena que ingreso son:', G );

	
end.