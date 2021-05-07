Program Tabla;

var I,num1, num2:Integer;


begin

	Writeln('Ingrese un numero');

	Readln(num1);

	Writeln('Ingrese el numero por el cual lo quiere multiplicar');

	readln(num2);

		For I:=1 to 10 do;
			
			case num1 of

			1: begin
				
			   writeln('1 por ', num2, ' es: ' ,  1*num2);

			   end;

			2: begin
				
				writeln('2 por ', num2, ' es: ' ,  2*num2);

			   end;

			3: begin
				
				writeln('3 por ', num2, ' es: ' ,  3*num2);

			end;

			4: begin
				
				writeln('4 por ', num2, ' es: ' ,  4*num2)

			end;

			5: begin

				writeln('5 por ', num2, ' es: ' ,  5*num2)

			end;

			6: begin
				
				writeln('6 por ', num2, ' es: ' ,  6*num2)

			end;

			7: begin

			writeln('7 por ', num2, ' es: ' ,  7*num2);

			end;

			8:begin
				
				writeln('8 por ', num2, ' es: ', 8*num2);
			end;

			9: begin
				
				writeln('9 por ', num2, ' es: ' , 9*num2);

			end;

			10: begin
				
				writeln('10 por ', num2, ' es: ' , 10*num2);

			end;


end;

end.
