
var A:array[1..100] of integer;
    max:integer;//������ �������
procedure ShakerSort;
    var
      l, r, j : Integer;
      x : integer;
    begin
      l := 2; //����� ���� =2
      r := max; //������ ����=�����
      while l <= r do //���� �� ����������
        begin
          { "�������" ����� ������� }//���� ������� �� �����
          for j := l to r do
          if A[j] < A[j - 1] then //���� ��������� ������
            begin
              x := A[j];
              A[j] := A[j - 1]; //����������
              A[j - 1] := x;
            end;
          r := r - 1; //�������� ����� ���� �����
          { "�������" ������ ������ }//���� � ����� � ������
          for j := r downto l do
          if A[j] < A[j - 1] then //������� ������
            begin
              x := A[j];
              A[j] := A[j - 1]; //����������
              A[j - 1] := x;
            end;
          l := l + 1; //����� ���� �������� ������
        end;
    end;
var i:byte;
begin
randomize;
write('������ ������� �� 100 max=');
read(max);
writeln('�������� ������:');
for i:=1 to max do
 begin
  A[i]:=random(100);
  write(A[i]:4);
 end;
writeln;
ShakerSort;
writeln('����������:');
for i:=1 to max do
write(A[i]:4);
end.