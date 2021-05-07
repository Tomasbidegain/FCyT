program facturas;

uses crt;

var
	tecla, tecla_1, razon_s, descripcion, max_desc: string;
	cantidad, cont_fac, cont_luces: integer;
	precio_u, subtotal_ar, subtotal, iva, max_prod, mont_luces, total, ac_total: real;

begin
cont_fac:=0;
ac_total:=0;
writeln('1. Para cargar el talonario');
readln(tecla);
while (tecla='1') do 
begin
	subtotal:=0;
	iva:=0;
	total:=0;
	max_prod:=0;
	max_desc:='';
	cont_luces:=0;
	mont_luces:=0;
	writeln('Ingrese la razon social.');
	readln(razon_s);
	writeln(razon_s);
	writeln('1. Para cargar articulo');
	readln(tecla_1);
	while (tecla_1='1') do 
	begin
		subtotal_ar:=0;
		writeln('Ingrese la descripcion del articulo: ');
		readln(descripcion);
		writeln('Ingrese la cantidad: ');
		readln(cantidad);
		writeln('Ingrese precio unitario: ');
		readln(precio_u);
		writeln('Descripcion: ', descripcion);
		writeln('Cantidad: ', cantidad);
		writeln('Precio unitario: ', precio_u);
		subtotal_ar:= (precio_u * cantidad);
		writeln('Subtotal de ',descripcion,': $',subtotal_ar);
		subtotal:= (subtotal + subtotal_ar);
		if (max_prod < precio_u) then
		begin
			max_prod:=precio_u;
			max_desc:= descripcion;
		end;
		if (descripcion = 'Luces de emergencia') then
		begin
			inc(cont_luces);
			mont_luces:= (cont_luces * precio_u);
		end;
		writeln('1. Para cargar otro articulo');
		writeln('2. Para dejar de cargar articulos');
		readln(tecla_1);
	end;
	iva:= (subtotal * 0.21);
	total:= (subtotal + iva);
	ac_total:= (ac_total + total);
	inc(cont_fac);
	writeln('El producto mas caro es: ', max_desc,' de: $',max_prod:2:0);
	if (cont_luces <> 0) then
	begin
		writeln('Se vendieron ', cont_luces, ' luces de emergencia.');
		writeln('Monto recaudado con las luces de emergencia: ', mont_luces:2:0);
	end;
	writeln('Subtotal de la factura: $',subtotal:2:0);
	writeln('Iva: $',iva:2:0);
	writeln('Total de la factura: $', total:2:0);
	writeln('1. Para cargar otra factura.');
	writeln('2. Para salir.');
	readln(tecla);
end;
	writeln('Cantidad de facturas emitidas: ', cont_fac);
	writeln('Monto total vendido: $', ac_total:2:0);
end.