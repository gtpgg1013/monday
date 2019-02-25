import os

# 해당 폴더로 들어가기
os.chdir("/home/ubuntu/workspace/monday/student_list")
# 폴더 안에 모든 파일 돌면서
# 이름을 바꾼다.

# 현재 폴더의 존재하는 파일 이름들 리스트로 묶어줌
for filename in os.listdir("."):
    os.rename(filename, filename.replace("student","mc"))
    # 수정할 때에는!