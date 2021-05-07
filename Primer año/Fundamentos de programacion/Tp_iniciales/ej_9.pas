program naturales;

var 
	Num: 1..100;
	I, ContQ, ContC,ContCom: Integer;

begin
	ContQ:=0;
	ContC:=0;
	ContCom:=0;
	 	
	 	For I:=1 to 100 do
	 	Begin
	 		writeln('Ingrese un numero natural');
	 		readln(Num);
	 	     If (Num>15) then
	 			ContQ:=ContQ+1;
	 		 If (Num>50) then
	 		 	ContC:=ContC+1;
	 		 If (Num>25) and (Num<45) then
	 		 	ContCom:=ContCom+1;
	 	end;
	 	writeln(ContQ , 'Son la cantidad de números que son mayores que 15');
	 	writeln(ContC , 'Son la cantidad de números que son mayores que 50');
	 	writeln(ContCom , 'Son la cantidad de numeros comprendidos entre 25 y 45');
	 	


end.