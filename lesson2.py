# # MÔ HÌNH HÓA 1 TEST CASE
# class TestCase:
#     # Hàm khởi tạo: Bắt buộc phải có test_id, còn status có thể có hoặc không
#     def __init__(self, test_id: str, status: str = None):
#         self.test_id = test_id
        
#         # Tư duy Dev (Defensive Programming): Xử lý dữ liệu "rác" ngay tại cửa
#         if status is None or status.strip() == "":
#             self.status = "UNKNOWN"
#         else:
#             self.status = status.upper()  # Đảm bảo luôn in hoa (PASSED, FAILED)

# # --- Thực thi ---
# # Khởi tạo đối tượng (Lúc này __init__ sẽ tự chạy)
# test1 = TestCase(test_id="T1", status="passed") 
# test2 = TestCase(test_id="T6") # Không truyền status

# print(f"Test {test1.test_id}: {test1.status}")  # Output: Test T1: PASSED
# print(f"Test {test2.test_id}: {test2.status}")  # Output: Test T6: UNKNOWN

# class TestSuite:
#     def __init__(self, raw_data: list[dict]):
#         """
#         Nhận vào cục data JSON thô (list các dictionary)
#         và biến chúng thành danh sách các đối tượng TestCase cho xịn xò.
#         """
#         # self.tests sẽ lưu một danh sách các Object TestCase
#         self.tests = []
#         for item in raw_data:
#             # Lấy data từ dict an toàn bằng .get()
#             t_id = item.get("test_id", "NO_ID")
#             t_status = item.get("status")
            
#             # Tạo object TestCase và nhét vào list
#             test_obj = TestCase(test_id=t_id, status=t_status)
#             self.tests.append(test_obj)
            
#     def count_test_status(self, status : str) -> int:
#         count = 0
#         for t in self.tests:
#             if t.status == status:
#                 count += 1
#         return count

#     def print_all_tests(self):
#         """In ra danh sách test đang quản lý"""
#         for t in self.tests:
#             print(f"[{t.test_id}] -> {t.status}")

# jira_tickets = [
#     {"ticket_id": "BUG-101", "severity": "CRITICAL", "status": "OPEN"},
#     {"ticket_id": "BUG-102", "severity": "HIGH", "status": "RESOLVED"},
#     {"ticket_id": "BUG-103", "status": "OPEN"},  # Lỗi: Thiếu key 'severity'
#     {"ticket_id": "BUG-104", "severity": "CRITICAL", "status": "IN_PROGRESS"},
#     {"ticket_id": "BUG-105", "severity": "LOW", "status": None}, # Lỗi: status là None
#     {"ticket_id": "BUG-106", "severity": "CRITICAL", "status": "CLOSED"}
# ]

# Yêu cầu:
# Bạn hãy xây dựng 2 Class: Bug và BugTracker theo các tiêu chí sau:

# 1. Class Bug (Đại diện cho 1 lỗi):

# Hàm __init__: Nhận vào ticket_id, severity, và status.

# Defensive Programming (Bắt lỗi):

# Nếu severity không có, gán mặc định là "UNKNOWN".

# Nếu status là None hoặc rỗng, gán mặc định là "OPEN".

# 2. Class BugTracker (Đại diện cho hệ thống quản lý):

# Hàm __init__: Nhận vào danh sách raw_data (như jira_tickets ở trên), biến chúng thành các đối tượng Bug và lưu vào self.bugs.

# Method 1 - count_critical_bugs(self) -> int: Đếm và trả về số lượng Bug có severity là "CRITICAL". (Lưu ý bài học fix bug lúc nãy: đếm xong hết mới return nhé).

# Method 2 - get_actionable_bugs(self) -> list[str]: Trả về một danh sách các ticket_id của những Bug cần phải làm việc ngay.

# Điều kiện: severity là "CRITICAL" VÀ status đang là "OPEN" hoặc "IN_PROGRESS".
import json

class Bug:
    def __init__(self, ticket_id: str, severity: str = "UNKNOWN", status: str = "UNKNOWN"):
        self.ticket_id = ticket_id

        if severity is None or severity.strip() == "":
            self.severity = "UNKNOWN"
        else:
            self.severity = severity.upper()
            
        if status is None or status.strip() == "":
            self.status = "UNKNOWN"
        else:
            self.status = status.upper()
        
    
class BugTracker:
    def __init__(self, raw_data: list[dict]):
        self.bug = []
        for item in raw_data:
            t_id = item.get("ticket_id", "NO_ID")
            t_severity = item.get("severity")
            t_status = item.get("status")
            bug_obj = Bug(ticket_id=t_id, severity=t_severity, status=t_status)
            self.bug.append(bug_obj)

    def get_all_bugs(self) -> list[dict]:
        all_bugs = []
        for b in self.bug:
            all_bugs.append({"ticket_id": b.ticket_id, "severity": b.severity, "status": b.status})
        return all_bugs

    def count_critical_bugs(self) -> list[str]:
        critical_bugs = []
        for b in self.bug:
            if b.severity == "CRITICAL":
                critical_bugs.append({"ticket_id": b.ticket_id, "severity": b.severity, "status": b.status})
        return critical_bugs
    
    def get_actionable_bugs(self) -> list[str]:
        actionable = []
        for b in self.bug:
            if b.severity == "CRITICAL" and b.status in ["OPEN", "IN_PROGRESS"]:
                actionable.append({"ticket_id": b.ticket_id, "severity": b.severity, "status": b.status})
        return actionable
    
    def add_bug(self, ticket_id: str, severity: str, status: str) -> dict:
        for b in self.bug:
            if b.ticket_id == ticket_id:
                raise ValueError(f"Bug with ticket_id '{ticket_id}' already exists.")
        new_bug = Bug(ticket_id=ticket_id, severity=severity, status=status)
        self.bug.append(new_bug)
        return {"ticket_id": new_bug.ticket_id, "severity": new_bug.severity, "status": new_bug.status} 

    def update_bug(self, ticket_id: str, severity: str = None, status: str = None) -> dict:
        for b in self.bug:
            if b.ticket_id == ticket_id:
                if severity is not None:
                    b.severity = severity.upper()
                if status is not None:
                    b.status = status.upper()
                return {"ticket_id": b.ticket_id, "severity": b.severity, "status": b.status}
        raise ValueError(f"Bug with ticket_id '{ticket_id}' not found.")
    
    def delete_bug(self, ticket_id: str) -> dict:
        for b in self.bug:
            if b.ticket_id == ticket_id:
                self.bug.remove(b)
                return {"message": f"Bug with ticket_id '{ticket_id}' has been deleted."}
        raise ValueError(f"Bug with ticket_id '{ticket_id}' not found.")
    
    def save_to_json(self, file_path: str):
        data_to_save = []
        for b in self.bug:
            data_to_save.append({"ticket_id": b.ticket_id, "severity": b.severity, "status": b.status})
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data_to_save, file, indent=4)
            print(f"Data saved successfully to '{file_path}'.")
        except Exception as e:
            print(f"Error saving data: {e}")

def load_data_from_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' does not contain valid JSON.")
        return []

def export_report_data(data: list[dict], output_path: str):
    try:
        with open(output_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        print(f"Report data exported successfully to '{output_path}'.")
    except Exception as e:
        print(f"Error exporting report data: {e}")


if __name__ == "__main__":
    file_name = "jira_data.json"
    print(f"Loading data from '{file_name}'...")
    raw_tickets = load_data_from_json(file_name)
    
    if raw_tickets:
        tracker = BugTracker(raw_tickets)
        print("Data loaded successfully. Here are the tickets:")
        print(f"Total tickets: {len(tracker.bug)}")
        print(f"Critical tickets: {tracker.count_critical_bugs()}")
        print(f"Actionable tickets: {tracker.get_actionable_bugs()}")
        print("Exporting actionable tickets to 'actionable_report.json'...")
        actionable_data = tracker.get_actionable_bugs()
        export_report_data(actionable_data, "actionable_report.json")
    else:
        print("Failed to load data.")
