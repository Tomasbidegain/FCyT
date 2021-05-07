Program cien;
uses crt;
var 
	num:integer;
	i:1..100;
	c:integer;
begin
	for i:=1 to 100 do
	c:=1;
	writeln('ingrese un numero');
	readln(num);	
	 writeln('~', c ,' veces');  
	if ((num mod 2)=0) then
	writeln(num,': es multiplo de 2')
       	
       			
       			
       else 
       			
       writeln(num, ' no es multiplo de 2');
       c:=c+1;
       				
       		
       		

       	
       	readkey;
end.

