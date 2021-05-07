program Protector;

uses crt;

var
    i: integer;

begin
   begin
       for i:= 1 to 15 do 
        write('Dentro de ', i,' segundos, se activara el protector de pantalla.')
    end;
write('Para salir del protector de pantalla oprima cualquier letra.');
repeat
write('*******************************************************************************');
write('*                                                                             *');
write('*                      *Protector de pantalla*                                *');
write('*                      *Protector de pantalla*                                *');
write('*                      *Protector de pantalla*                                *');
write('*                      *Protector de pantalla*                                *');
write('*                      *Protector de pantalla*                                *');
write('*                      *Protector de pantalla*                                *');
write('*                      *Protector de pantalla*                                *');
write('*                      *Protector de pantalla*                                *');
write('*                                                                             *');
write('*******************************************************************************');
until keypressed;
end.

