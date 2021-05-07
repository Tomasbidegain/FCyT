Program CandidatosB;

var
	
	I, voto, c1, c2, c3, b: Integer;

	TotalV, TotalC1, TotalC2, TotalC3 , TotalB: integer;

	Promed: real;


begin
	
	C1:= 0;

	C2:= 0;

	c3:= 0;

	B:=0;

	TotalV:=0;

	TotalC1:=0;

	TotalC2:=0;

	TotalC3:=0;

	TotalB:=0;

	for I:= 1 to 17 do
	
	write('Ingrese su voto: ');

	read(voto);

	begin

		C1:= 0;

		C2:= 0;

		c3:= 0;

		B:=0;

		while voto > 0 do

		begin

			TotalV:=TotalV+1;

			case voto of 

	   		
				1: 
				begin
			
					c1:=c1+1;

					TotalC1:= totalc1+1;


				end;

				2: 
				begin
			
					c2:=c2+1;

					TotalC2:= totalc2+1;
			

				end;

				3: 
				begin
			
					c3:=c3+1;

					TotalC3:= totalc3+1;
			

				end;

				else 
				begin
			
					b:=b+1;

					totalb:= totalb+1;

		

			write('ingrese su voto: ');

			readln(voto);



		end;
		
		write('Depto: ', I);

		if (c1>c2) and (c1>c3) then

		writeln('el candidato 1 es el ganador.')
	


		     else

			if (c2>c3)then

				writeln(' el candidato 2 es el ganador.')

			

			else

				writeln ('el cadidato 3 es el ganador.');
	
			end;
	end;


end.
