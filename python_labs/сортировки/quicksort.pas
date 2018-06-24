const max=20; { можно и больше... }
type
  list = array[1..max] of integer;
  
procedure quicksort(var a: list; Lo,Hi: integer);
  
  procedure sort(l,r: integer);
  var
    i,j,x,y: integer;
  begin
    i:=l; j:=r; x := a[(r+l) div 2]; {- для выбора среднего элемента }
    repeat
      while a[i]<x do i:=i+1; { a[i] > x  - сортировка по убыванию}
      while x<a[j] do j:=j-1; { x > a[j]  - сортировка по убыванию}
      if i<=j then
      begin
        y:=a[i]; a[i]:=a[j]; a[j]:=y;
        i:=i+1; j:=j-1;
      end;
    until i>=j;
    if l<j then sort(l,j);
    if i<r then sort(i,r);
  end; {sort}
  
begin {quicksort};
  sort(Lo,Hi)
end; {quicksort}

var i,j,n,min,x: integer;
a: list;
begin
read(n);
for i:=1 to n do 
read(a[i]);

quicksort(a,1,n);


for i:=1 to n do 
write(a[i],' ');
end.