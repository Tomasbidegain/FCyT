Program Ej_3;

uses crt,matriz;

const
    n=2;
    m=2;

type
    t_dato = integer;
    t_matriz = array [1..n,1..m] of t_dato;

var
    mat:t_matriz;
    ac_col,max_col,menor,c,f: t_dato;

procedure suma_matriz (var mat:t_matriz; var ac_col:t_dato);
var i,j: t_dato;

begin
    for i:=1 to n do
    begin
        ac_col:=0;
        for j:= 1 to m do
        begin
            ac_col:= (ac_col + mat [i,j]);   
        end;
    writeln('La suma de esta columna es: ', ac_col);
    end;
end;

procedure mayor_matriz(var mat: t_matriz; var max_col:t_dato);

var 
    i,j: t_dato;

begin

    for i:= 1 to n do
    begin
        max_col:=0;
        for j:= 1 to m do
        begin
            if (max_col < mat[i,j]) then
            begin
                max_col:= mat[i,j];
            end;
        end;
        writeln('El mayor de la culumna ',i,' es: ', max_col);
    end;
end;
procedure menor_matriz(var mat:t_matriz;var menor: t_dato; var c: t_dato; var f: t_dato);
var
    i,j:t_dato;

begin
    menor:=mat[1,1];

    for i:=1 to n do
    begin
        for j:= 1 to m do
        begin
            if menor > mat[i,j] then
            begin
                menor:= mat[i,j];
                f:=i;
                c:=j;
            end;
        end;

    end;
end;

begin
    inicializar_matriz(mat);
    cargar_matriz(mat);
    suma_matriz(mat,ac_col);
    mayor_matriz(mat, max_col);
    menor_matriz(mat,menor,c,f);
    writeln('El menor elemento de la matriz se encuentra en la posicion: [', c,',',f, ']');

end.



