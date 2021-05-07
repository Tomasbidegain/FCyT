Program Ahorcadoo;
uses crt;
var   
errores,j , i,longitud_palabra_sec, longitud_palabra:Integer;      
palabra_secreta,palabra,palabra_:String;
error,a:boolean;

begin
error:=false;
a:=false;
longitud_palabra:=0;
errores:=0;
longitud_palabra_sec:=0;
 writeln('Juguemos el ahorcado , COMENCEMOS!!');
 //Ingresamos la palabra a adivinar.
 writeln('Ingrese una palabra para adivinar.');
 read(palabra_secreta);
 clrscr;
 longitud_palabra_sec:= length(palabra_secreta);

    
    for i:=1 to longitud_palabra_sec do
    begin
     insert('_', palabra_, i);
    end;

    //Comienzo del juego.
    writeln('El tamaño de la palabra que tienes que adivinar es de ', longitud_palabra_sec, ' caracteres.');
    writeln('......');
    writeln('Palabra a adivinar: ');
    while (a = false) do
    begin
    writeln(palabra_);
    
    write('Palabra o letra:');
     readln(palabra);
    //Arriesga
     longitud_palabra:= length(palabra);
        if (longitud_palabra > 1) and (palabra=palabra_secreta) then
        begin
        a:=true;
         writeln('Adivinaste la palabra, GANASTE!!');
        end;
        //Arriesga y pierde
        if (longitud_palabra >1) and (palabra <> palabra_secreta) then
        begin
        clrscr;
         a:=true;
         writeln('_____');
         writeln('|   |');
         writeln('| (*_*)');
         writeln('|  ===');
         writeln('|  /|\');
         writeln('|  / \');
         writeln('=');
         writeln('La palabra que acabas de ingresar es incorrecta, PERDISTE.');
         writeln('La palabra a adivinar era: ',palabra_secreta);
        end;
        if (longitud_palabra=1) then
        begin
            //Inserto letras en los _       
            for j:= 1 to longitud_palabra_sec do
            begin
             if (palabra=palabra_secreta[j]) then
                begin
                 error:=true;
                 delete (palabra_,j,1);
                 insert(palabra,palabra_,j);
                end;      
            end;
            //Incremento errores y los muestro con el cuerpito
             if (error=false) then
             begin
             inc(errores);
             end;            
             case errores of
                1:
                begin
                clrscr;
                writeln('                                                   ____');
                writeln('                                                   |   |');
                WriteLn('                                            Fallos:| (*_*)');
                writeln('                                                   |');
                writeln('                                                   |');
                writeln('                                                   =');
                end;
                2:
                begin
                clrscr;
                writeln('                                                   _____');
                writeln('                                                   |   |');
                WriteLn('                                            Fallos:| (*_*)');
                WriteLn('                                                   |   | ');
                writeln('                                                   |');
                writeln('                                                   =');
                end;
                3:
                begin
                clrscr;
                writeln('                                                   _____');
                writeln('                                                   |   |');
                WriteLn('                                            Fallos:| (*_*)');
                WriteLn('                                                   |  /|');
                writeln('                                                   |');
                writeln('                                                   =');
                end;
                4:
                begin
                clrscr;
                writeln('                                                    _____');
                writeln('                                                    |   |');
                WriteLn('                                             Fallos:| (*_*)');
                WriteLn('                                                    |  /|\');
                writeln('                                                    |');
                writeln('                                                    =');
                end;
                5:
                begin
                clrscr;
                writeln('                                                     _____');
                writeln('                                                     |   |');
                WriteLn('                                              Fallos:| (*_*)');
                WriteLn('                                                     |  /|\');
                WriteLn('                                                     |  /  ');
                writeln('                                                     =');
                end;
                6:
                begin
                clrscr;
                writeln('                                                      _____');
                writeln('                                                      |   |');
                WriteLn('                                               Fallos:| (*_*)');
                WriteLn('                                                      |  /|\');
                WriteLn('                                                      |  / \');
                writeln('                                                      =')
                end;
                7:
                begin
                clrscr;
                error:=true;
                writeln('                                                      _____');
                writeln('                                                      |   |');
                WriteLn('                                               Fallos:| (*_*)');
                WriteLn('                                                      |  ===');
                WriteLn('                                                      |  /|\');
                WriteLn('                                                      |  / \');
                writeln('                                                      =');
                writeln('                                                      PERDISTE.');
                writeln('La palabra a adivinar era: ',palabra_secreta);
                a:=true;
                end;
            end;
            error:=false;
            //Adivina todas las palabras
            if (palabra_secreta = palabra_) then
                begin
                clrscr;
                a:=true;
                writeln('GANASTE!!');
                writeln('La palabra elegida fue: ', palabra_secreta);
                end;
                
            end;
        end;   
   readkey;
    end.


