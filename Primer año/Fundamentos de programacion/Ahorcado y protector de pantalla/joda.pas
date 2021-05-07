
program Matriz;

var
 mat: array[1..9,1..9] of char;
 i,j,valor: integer;
 carNum: string;
 car: char;

BEGIN
 for i:=1 to 9 do
  for j:=1 to 9 do
   begin
     if (j=1) and (i<>9) then
      begin
       valor:= 9-i;
       str(valor,carNum);
       car:=carNum[1];
       mat[i,j]:= car;
      end
     else if (j=1) and (i=9) then
       mat[i,j]:= ' '
          else  if (i<>9) then
           mat[i,j]:= 'X'
                else
                  mat[i,j]:= chr(j+95);
   end;


 for i:=1 to 9 do
  begin
    for j:=1 to 9 do
     write(mat[i,j],' ');
    writeln;
  end;

 readln;
END.