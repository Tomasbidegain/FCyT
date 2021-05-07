Program Primos;
uses crt;
Var
	a,b,l,i,i2:integer;
	c:Boolean;

	begin
		
		writeln('ingrese el rango de numeros.');

		readln(a,b);

		if(a>1) and (a<b) then

		begin

			 for i:=a to b do

			    begin

			     	i2:=i div 2;

			     	c:= true;

			    	for l:=2 to i2 do

			    	begin
			    		
			    		if((i mod l)= 0) and (c=true) then
			    	 		
			    	 		begin 
			    	 		
			    	 			writeln(i, ' no es primo.');

			    	 			c:= false;
			    	 		
			    	 		end;

			    	If c=true then

			    	writeln(i,  ' es primo.');
			  	end;

		end;	 	

	end;
	readkey;
end.