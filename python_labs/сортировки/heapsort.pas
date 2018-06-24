const MX = 10000000;
type vector = array[0..MX] of integer;

procedure heap(n,k: integer; var x: vector);
  var ch,newel,el: integer;
  begin
    el := x[k];
    while 2*k+1 < n do
    begin
      ch := 2*k+1;
      if (ch+1 < n) and (x[ch] < x[ch+1]) then
        ch := ch + 1;
      if x[ch] > el then 
      begin
        x[k] := x[ch];
        k := ch;
      end
      else
        break;
    end;
    x[k] := el;
  end;
  
  
procedure sort_pir(el: integer; var a: vector);
  var i,n, newel: integer;
   
  begin
  for i := (el div 2)-1 downto 0 do
    heap(el,i,a);

  for i := el-1 downto 0 do
    begin
      newel := a[i];
      a[i] := a[0];
      a[0] := newel;
      heap(i,0,a); 
    end;
   
end;
  
var 
  i,el: integer;
  finish,start:real;
  a: vector;



begin
writeln('Количество элементов   Время выполнения');

el:=1000;
for i := 0 to el-1 do
a[i] := random(-300,300);
start := Milliseconds; 
sort_pir(el,a);
finish := Milliseconds; 
writeln(el:12,(finish-start):20:4);


el:=10000;
for i := 0 to el-1 do
a[i] := random(-300,300);
start := Milliseconds; 
sort_pir(el,a);
finish := Milliseconds; 
writeln(el:12,(finish-start):20:4);

el:=100000;
for i := 0 to el-1 do
a[i] := random(-300,300);
start := Milliseconds; 
sort_pir(el,a);
finish := Milliseconds; 
writeln(el:12,(finish-start):20:4);

el:=1000000;
for i := 0 to el-1 do
a[i] := random(-300,300);
start := Milliseconds; 
sort_pir(el,a);
finish := Milliseconds; 
writeln(el:12,(finish-start):20:4);
end.
//44 55 12 42 94 18 06 67





