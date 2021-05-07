Program Pares;

uses crt;

var
    I: 20..500;

	Prod,ac:integer;

begin
	Prod:=1;

	ac:=0;


	for I:= 20 to 500 do;

	begin 
		if (I mod 2=0) then
			begin
				ac:= ac+I;
				Prod:=Prod*I;
			end;
	end;
	writeln('el producto es:');
	writeln(Prod*ac);

	readkey;

end.