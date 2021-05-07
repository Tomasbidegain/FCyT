Program Candidatos;

var
	
	voto, c1, c2, c3, B: Integer;

begin
	
	c1:=0;

	c2:=0;

	c3:=0;

	B:=0;

	writeln ('Ingrese su voto');

	Read (voto);

		begin
			
			while voto > 0 do

				begin

				case voto of

				1:c1:= c1+1;
					
					

				2: c2:= c2+1;


				3:c3:= c3+1;			
				else
	
				b:=b+1;

				end;

				  writeln('Ingrese su voto');

				  readln (voto);
		
		end;

	writeln ('el candidato 1 tiene ' , c1 , '  votos.' );

	writeln ('el candidato 2 tiene ' , c2 , '  votos.' );

	writeln ('el candidato 3 tiene ' , c3 , '  votos.' );

	writeln (' la cantidad de votos nulos o en blanco son: ', b);

	

		if (c1>c2) and (c1>c3) then

		writeln('el candidato 1 es el ganador.')
	


		     else

			if (c2>c3)then

				writeln(' el candidato 2 es el ganador.')

			

			else

				writeln ('el cadidato 3 es el ganador.');

			

end;

end.


