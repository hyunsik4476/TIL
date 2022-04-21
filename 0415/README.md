# Git

## 수정사항 취소하기

### git restore \<filename>

* 모디파이된 상태를 취소할 수 있음
* 다만 파일을 덮어씌우는 것이기 때문에 사라진 수정사항을 복구 못함



### git rm --cached \<filename>

* 커밋이 없을 때 사용가능
* staging area 에 있는 파일을 WD 로 이동시키기



### git restore --staged \<filename>

* 커밋이 있을 때 사용 가능 (아예?)
* 커밋을 해야 HEAD가 생기기 때문에 다른 명령어를 사용



### git commit --amend

* 직전의 커밋을 수정하기
  	1. 커밋 메시지만 수정
      * 마지막으로 커밋하고 나서 수정한 것이 없을 때 vim 에서 수정(`i`) 저장(`:wq`)
      * 원래 해시 : e44bcdd3aa0fabc4048ec7182eea71c658daf705
      * 바꾼 뒤 해시 : f893d4b0209a3467e1a6ede01d20e63c694e6880
  	2. 이전 커밋 덮어쓰기
      * 마지막 커밋이후 Staging Area에 새로 올라온 내용이 있을 때



## Reset & Revert

> 과거로 되돌리기
>
> 되돌린 내용을 기록할것인가의 차이

#### 해시 확인하기

* `git log --oneline`

### reset

* git reset [option] \<commit hash>
* 특정 커밋으로 돌아갔을 때, 해당 커밋 이후의 커밋들이 전부 사라짐

#### 옵션

1. `--soft`
   * 돌아가려는 커밋으로 되돌아가고 이후의 commit 된 파일을 staging area 로 돌려놓음
2. `--mixed`
   * 옵션 미입력시 기본값
   * 이후의 commit 을 WD로 돌려놓음
3. `--hard`
   * 이후의 commit된 파일들을 WD에서 삭제
   * 단, untracked 파일은 그대로

#### 복구

* `git reflog` 로 삭제된 커밋 해시를 찾고 `--hard` 로 reset 하면 복구됨



### revert

> 다른 사람들과 협업할 때 커밋 내역의 차이로 인해 발생하는 충돌을 막기 위해 사용

* `git revert <commit hash>`
* 특정 사건을 없었던 일로 한다는 행위, 이전 커밋을 취소한다는 새 커밋을 만듬

* commit hash 에 해당하는 commit 을 없었던 일로 만든다
* 기존의 commit 에 새 commit이 추가



## Branch

### 1

* 각 사용자가 원격 저장소의 소유권을 가진 상태 - clone을 통해 저장소로
* 기능 추가를 위해 branch를 생성하고 기능 구현
* `git push origin <branchname>`
* pull request 로 master 브랜치가 바뀌면
  * 팀원들은 master브랜치로 이동해 pull 받음
  * 역할이 끝난 로컬 브랜치를 삭제

### 2

* repository를 복제 후 클론
* `git remote add upstream [원본url]` 으로 원본 원격저장소와 연결
* 복제본에 push후 오픈소스 원격 저장소로 PR을 보냄