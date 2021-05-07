Program Ocho_caracteres;

var
	C: char;
	i:integer;
	ConA, ConAst: integer;

begin
	
	for i:=1 to 8 do
	begin
	
		writeln('ingrese el caracter');

		readln(c);
		begin
			if (c='*') then
			ConAst:=ConAst+1
		 	else 
		 	if (c='a') then
		 	ConA:=ConA+1
		 	
		end;
	end;
	writeln(ConAst, ' cantidad de *');
	writeln(ConA, ' cantidad de a')
end.


