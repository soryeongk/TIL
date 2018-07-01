# Preview the Git Bash (Branch)
Branch 사용 예습
  * 파일을 특정 위치에 다운로드한 후, 해당 위치에서 Giy Bash를 실행
  * git chechout -b 2018 : 2018이라는 브랜치를 새로 생성
    - git branch : 현재 branch목록을 보여주는데, 현재 위치의 branch명 앞에 별표가 있음
    - git chechout "브랜치명" : 해당 브랜치로 이동
  * git add "파일명" : 파일을 stage로 옮겨 commit할 준비
  * git commit -m "blah blah" : 메시지를 입력하고 stage의 파일을 commit
  * git push -u origin : 깃헙으로 푸시
      Q. 파일 푸시 이후 바로 실행이 아니라, 새로 실행하는 경우라면, remote해야 하는 것인가?
