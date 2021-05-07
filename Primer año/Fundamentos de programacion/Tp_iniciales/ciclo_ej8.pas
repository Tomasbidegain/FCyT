Program Encuesta;
var
	resp:1..3;
	I:1..1200;
	cont1, cont2, cont3: integer;

begin
	cont1:=0;
	cont2:=0;
	cont3:=0;
	begin
		for I:=1 to 1200 do
		readln(resp);
			case resp of
				
			
					1:cont1:=cont1+1;
					2:cont2:=cont2+1;
					3:cont3:=cont3+1;

					
	 
	 end;	
	 
	 begin
	 
	 if(cont2>cont1)and(cont1>cont3)then;
	  writeln('S.O. Nro1')
	 end;
	 begin
	  if (cont3>cont1)then;
	   writeln('S.O Nro3');
	   else
	   writeln('S.O Nro1')
	 					
	 			
end.
