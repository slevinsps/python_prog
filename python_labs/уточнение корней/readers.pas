program Pr2s;

{$APPTYPE CONSOLE}

uses
  SysUtils;


type
  W = function(x:Real):Real;


// ���������� �������
function f(x:real):real;
  var g: real;
  begin
  g:= x*x-ln(x)-2*cos(x)-1;
  result:=g;
  end;
  
// ����� �������
procedure ridders_method(f:W;a:real;b:real;eps:real;var x1: real);
    // ������� ������� ���������� ���� � ��������� �������� get_x
    function sign(q1:real;q2:real):integer;
    begin
       if q1-q2<0 then
           result:= -1;
       if q1-q2>0 then
           result:= 1
       else
           result:= 0;
    end;

    // ��������� ��������� x
    function get_x(f:W;a:real;b:real):real;
    var c,x: real;
    begin

        c:= (a+b)/2;
        x:= c+(c-a)*(sign(f(a),f(b))*f(c))/sqrt(f(c)*f(c)-f(a)*f(b));
        result:=x;
    end;

    var x2: real;
    begin
    x1:= 0;  // ��������� x
    x2:= get_x(f,a,b);  // ��������� x

    // ���� ��� ����������� ����� � ��������� eps
    while abs(x2-x1)>eps do
      begin
        x1:= x2;
        // ���������� ����� ������� ���������
        if f(a)*f(x2)<0 then
            b:= x2
        else if f(x2)*f(b)<0 then
            a:= x2;
        x2:= get_x(f,a,b);
      end;
     end;


var r,x1,a,b,eps: real;
begin
writeln('������� ����� ������ �����, ������ ������� ��������� � �������:');
read(a,b,eps); 
ridders_method(f,a,b,eps,x1);
write('�������� ����� �� ���������� = ',x1:5:3);
readln;
readln;
end.


