Program Ahorcadoo;

var         
tecla:char;
letra:String[1];
palabra_secreta,palabra:String[20];

begin
writeln('Juguemos el ahorcado. Para empezar el juego oprima cualquier tecla');
read(tecla);
write('Ingrese una palabra para adivinar (de no mas de 20 letras).');
        read(palabra_secreta);
        
        longitud:=length(palabra_secreta);
        begin
        if (palabra_secreta>longitud) then
            write('La palabra exedio el limite de letras (por favor ingrese la palabra de nuevo.');
            readln(palabra_secreta);
        end;
    begin
        while (tecla<>'');
        writeln('Para comenzar, ingrese una letra');
        read(letra);

    end;
end.