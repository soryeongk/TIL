# Review the Git Bash
Git Bash로 로컬의 파일을 Git Hub의 Repository로 push하여 관리하는 것을 복습했다.
  * 로컬에 파일을 다운로드하고, 파일이 존재하는 폴더에서 Git Bash를 실행한다.
    => 혹은 cd "파일위치"를 사용해 직접 해당 위치로 이동한다.
  * git init : 폴더 내 .git이라는 폴더를 생성
  * git add "파일명" : 파일을 commit할 수 있는 준비
  * git commit -m "blah blah" : 입력할 메시지를 작성하고 commit
  * git remote add origin "git hub repository license" : 누구의 git hub에 어떤 repository인지 명시
  * git push -u origin master : master에 commit된 remote라이센스로 push
