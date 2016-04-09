## Fill in station 

#### Thông tin chung
Bài tập lớn số 1  
Nhóm 12  
Thành viên 
  + Trần Tuấn Nghĩa  
  + Lưu Trường Sinh  

#### Các file cần lưu ý:  
+ `fillstation.py` chứa các hàm chính để giải bài toán và tối ưu bài toán  
+ `letters` chứa 2 input mặc định của đầu bài  
+ `1000_inputs`  chứa 1000 input có lời giải  

#### Các phương pháp tối ưu hiệu năng
**Forward checking**  
Sau khi gán giá trị cho biễn x nào đó ta sẽ loại bỏ tất cả các giá trị không thỏa mãn các ràng buộc của tất các biến có ràng buộc với x    
**Most constrained variable**  
Ta sẽ chọn biến có nhiểu ràng buộc nhất(hay biến có ít giá trị thỏa mãn các ràng buộc trong doiman nhất) là biến tiếp theo để gán giá trị  
**Heuristic cho giá trị của biến**  
Dùng 1 trong 2 hàm sau:
+ Greedy heuristic  
Tại bước chọn giá trị cho biến x ta chọn giá trị nào mà tần suất của cặp từ tạo bởi giá trị đó với giá trị của biến bên trái biến x trên ma trận là lớn nhất trước  
+ Better greedy heuristic  
Gần giống hàm trên nhưng thay vì chỉ tính với biến bên trái ta tính trung bình cộng tần suất của tất cả các biến có ràng buộc với biến x  

#### Mô tả các hàm quan trọng  
|Tên hàm | Input | Output |
| --- | --- | --- |
|`back_track(assignment, csp, domain)`|assignment, csp, domain|`return assignment, csp` Nếu đầu vào có đáp án, `return False` Nếu đầu vào không có đáp án|
|`forward_checking(assignment, csp, domain, x)`|assignment, csp, domain, x|`return new_domain` Trả về 1 domain mới cho các biến có ràng buộc với biến x sau khi đã loại bỏ các giá trị không cần thiết|
|`get_most_constrained_variable(assignment, domain)`|assignment, domain|`return most_variable` Trả về biến chưa có giá trị mà có nhiều ràng buộc nhất|
|`greedy_heristic_domain(assignment, csp, domain, x)`|assignment, csp, domain, x|`return result, greedy_info` Trả về list chứa các giá trị của biến x được sắp xếp giảm dần theo tần suất xuất hiện của cặp từ được tạo bới giá trị đó với giá trị của biến bên trái x và thông tin tần suất của từng giá trị|
|`better_heristic_domain(assignment, csp, domain, x)`|assignment, csp, domain, x|`return result, greedy_info` Gần giống với hàm trên nhưng giá trị heuristic của giá trị của biến x giựa vào trung bình cộng tần số của các cặp từ tạo bởi giả trị đó và các giá trị của các biến có ràng buộc với biến x|

#### Các câu lệnh chạy  
Giải 2 input của để bài  
`python fillstation.py -p 1 -f -m -h greedy -d`  
+ flag `-p 1` là đầu bài 1 (thay 1 bằng 2 để giải đầu bài 2)  
+ flag `-f` là dùng forward checking  
+ flag `-m` là dùng most constrained variable  
+ flag `-h greedy` là dùng hàm greedy
+ flag `-d` bật chể độ debug (bỏ flag -d đi đẻ tắt chế độ debug)

So sánh hiệu năng giữa các hàm heuristic  
`python fillstation.py -c -n 10`
+ flag `-c` để chạy chế độ so sánh 2 hàm greedy và better_greedy
+ flag `-n 10` sô lượng input (thay 10 bằng số nhỏ hơn 101 để chỉnh lượng input)

Lưu ý rằng hàm better_greedy trung bình mà nói thì sẽ tốt hơn greedy 1 chút cũng có trường hợp greedy tốt hơn













