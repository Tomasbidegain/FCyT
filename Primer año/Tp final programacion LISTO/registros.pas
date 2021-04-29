unit registros;

interface

uses crt;


type 
	t_cliente = record
		razon_social: string [30];
		cuit: string[13];
		telefono: string [10];
		domicilio: string [80];
		email: string [80];
		vigente: boolean;
	end;
	t_proyec = record
		id_proyecto: Longint;
		titulo: string [100];
		costo: real;
		cuit: string [13];
		director: string [80];
		mes:word;
		dia:word;
		anio:word;
		exporta: boolean;
		vigente: boolean;
	end;

var 
	reg_cliente: t_cliente;
	reg_proyecto: t_proyec;
	
implementation

end.