var i,j,n,min,x: integer;
a: array[1..15] of integer;
begin
read(n);
for i:=1 to n do 
read(a[i]);

for i := 1 to n-1 do begin
  min := i;
  for j := i+1 to n do begin
    if a[j]<a[min] then
      min := j;
  end;
  x := a[i];
  a[i] := a[min];
  a[min] := x;
end;

for i:=1 to n do 
write(a[i],' ');
end.