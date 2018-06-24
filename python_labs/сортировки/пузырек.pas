var i,j,n,min,x: integer;
a: array[1..15] of integer;
begin
read(n);
for i:=1 to n do 
read(a[i]);

for i:=1 to n-1 do 
    for j:=i+1 to n do {В этой строке начинающие программисты чаcто допускают ошибку}
      if a[i]>a[j] then 
        begin
          x:=a[i]; 
          a[i]:=a[j]; 
          a[j]:=x;
        end;

for i:=1 to n do 
write(a[i],' ');
end.