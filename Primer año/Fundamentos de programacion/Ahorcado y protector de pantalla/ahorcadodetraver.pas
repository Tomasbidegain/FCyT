program ahorcado;
uses crt;
var
   palabra,palabra2,letra,tema:String;
   L,I,aux,aux2,errores:Integer;
   aux3,aux4:Boolean ;
BEGIN
   errores:=0;
   aux3:=false;
   aux4:=false;
   Write('palabra: ');
   ReadLn(palabra);
   Write('tematica: ');
   ReadLn(tema);
   aux:= Length(palabra);
   for I:= 1 to aux do
   begin
      Insert('_',palabra2,I);
   end;
   clrscr;
   WriteLn('------------');
   WriteLn('#tamano de la palabra: ', aux);
   WriteLn('tematica: ',tema);
   WriteLn('------------');
   while (aux3 = false) do
   begin
      WriteLn('#',palabra2);
      Write('#letra o palabra: ');
      ReadLn(letra);
      aux2:= Length(letra);
      if (aux2>1) and (letra = palabra) then
        begin
          aux3:=true;
          WriteLn('------------');
          WriteLn('#GANASTE');
        end;
      if (aux2>1) and (letra <> palabra) then
        begin
          aux3:=true;        
          WriteLn('------------');
          WriteLn('#PERDISTE');
          WriteLn('( )');
          WriteLn('---');
          WriteLn('/|\');
          WriteLn('/ \');
          WriteLn('palabra elegida: ',palabra);
        end;
      if (aux2=1) then
      begin
      for L:= 1 to aux do
        begin
          if (letra = palabra[L]) then
           begin
             aux4:= true;
             delete (palabra2,L,1);
             Insert (letra,palabra2,L);
           end;
        end;
        if (aux4 = false) then
           inc (errores);
      case errores of
         1:
         begin
           WriteLn('( )');
         end;
         2:
         begin
          WriteLn('( )');
          WriteLn(' | ');
         end;
         3:
         begin
          WriteLn('( )');
          WriteLn('/|');
         end;
         4:
         begin
          WriteLn('( )');
          WriteLn('/|\');
         end;
         5:
         begin
          WriteLn('( )');
          WriteLn('/|\');
          WriteLn('/  ');
         end;
         6:
         begin
          WriteLn('( )');
          WriteLn('/|\');
          WriteLn('/ \');
         end;
         7:
         begin
          aux3:=true;
          WriteLn('------------');
          WriteLn('#PERDISTE');
          WriteLn('( )');
          WriteLn('---');
          WriteLn('/|\');
          WriteLn('/ \');
          WriteLn('palabra elegida: ',palabra);
         end;
      end;
      aux4:=false;
      if (palabra = palabra2) then
      begin
         aux3:=true;
         WriteLn('------------');
         WriteLn('#GANASTE');
         WriteLn('palabra elegida: ',palabra);
      end;
      end;
      WriteLn('------------');
   end;
readKey;
END.