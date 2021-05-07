program Obreros;

uses crt;

var

   I,sec,edad,emp:Integer;

   ed1,ed2,ed3,ed4,ed5:Integer;

   s1,s2,s3,s4,s5:Integer;  

begin

  ed1:=0;

  ed2:=0;

  ed3:=0;

  ed4:=0;

  ed5:=0;

  s1:=0;

  s2:=0;

  s3:=0;

  s4:=0;

  s5:=0;

  for I:= 1 to 4000 do

    begin
  
      Write('ingresar edad: ');

      Read(edad);

      Write('ingresar sección: ');

      read(sec);

      write('ingresar número de empleado: ');

      read (emp);

      case sec of

      1:

      begin

        s1:=s1+1;

        ed1:=ed1+edad;
      end;

      2:

      begin

        s2:=s2+1;   

        ed2:=ed2+edad;

      end;

      3:  

      begin

        s3:=s3+1;

        ed3:=ed3+edad;

      end;

      4:

      begin

        s4:=s4+1;

        ed4:=ed4+edad;

      end;

      5: 

      begin

        s5:=s5+1;

        ed5:=ed5+edad;

      end;

    end;

  end;

  WriteLn('empleados en la sección 1: ', s1);

  WriteLn('promedio de edad en la sección 1: ', ed1/s1);


  WriteLn('empleados en la sección 2: ', s2);

  WriteLn('promedio de edad en la sección 2: ',ed2/s2);

 
  WriteLn('empleados en la sección 3: ', s3);

  WriteLn('promedio de edad en la sección 3: ',ed3/s3);


  WriteLn('empleados en la sección 4: ', s4);
  WriteLn('promedio de edad en la sección 4: ',ed4/s4);

  WriteLn('empleados en la sección 5: ', s5);
  WriteLn('promedio de edad en la sección 1: ',ed5/s5);

end.