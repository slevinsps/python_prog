var i,j,n,x,step: integer;
a: array[1..15] of integer;
begin
read(n);
for i:=1 to n do 
read(a[i]);

step := n div 2;
while step > 0 do begin
	for i := step+1 to n do begin
	x := a[i];
	j:=i-step;
	while (x < a[j]) do begin
		a[j+step]:=a[j];
		j:=j-step;
		if j <= 0 then
		break;
	end;
	a[j+step]:=x;
	end;
	step := step div 2;
end;


for i:=1 to n do 
write(a[i],' ');
end.