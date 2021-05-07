Program Matrices;
const
	fila = 5;
	col= 4;
type
	t_dato=integer;
	t_matriz = array [1 to .. do,1 .. col] of t_dato;
	t_vector = array [1 .. col] of t_dato;

var 
	mat: t_matriz;
	vec:t_vector;

procedure maximo (var m: t_matriz; var v:t_vector);
	var 
	i: 1 .. col;
	j: 1..fila;
	max: t_dato;

begin
	for i :=1 to col do
	max:= m [1,i];
	begin
		if m[j,i]>max then
			max:=m[j,i]
	end;
	v[i]:=max;
end;