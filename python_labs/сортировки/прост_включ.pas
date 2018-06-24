var i,j,n,x: integer;
a: array[1..15] of integer;
begin
read(n);
for i:=1 to n do 
read(a[i]);

for i := 2 to n do begin
  x := a[i];
  j:=i-1;
  while (x > a[j]) do begin
    a[j+1]:=a[j];
    j:=j-1;
    if j = 0 then
      break;
  end;
  a[j+1]:=x;
end;
for i:=1 to n do 
write(a[i],' ');
end.