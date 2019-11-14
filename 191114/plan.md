https://git-school.github.io/visualizing-git/
https://github.com/FredrikNoren/ungit

Идеология: воспроизводимость
Идеология: контроль версий
Идеология: деление на коммиты, что такое "коммит"
Система контроля версий: общая функциональность, отличия SVN и Git
!!! Git vs GitHub, git init, git clone
Модель репозиториев Git: commit, branch, tag, remote, трекаются только содержимое по файлам, нет безопасности, децентрализация
Имена веток, тэгов, коммитов (можно префикс), HEAD~1
HEAD, HEAD@{1} против HEAD~1, reflog
Состояния файлов: ignored, untracked, unmodified, modified, staged
Переводы между состояниями: зачем и когда, git status
!!! Книга Pro Git v2 (есть на русском), git --help, git add --help
git clone, один remote, fetch/push, но что делать с ветками?
!!! Клон с GitHub
Слияние веток: fast-forward, squash, merge commit, rebase
Слияние файлов внутри merge: независимо по файлам, независимо в разных кусках
Слияние файлов внутри merge: конфликты и разрешение
Pull из репозитория как fetch+merge
git rebase -i для чистой истории и выпиливания коммитов
git cherry-pick как аналог squash
Перевод веток с push --force: reset --hard, commit --amend; почему не стоит
!!! Репозитории на GitHub: форк
!!! push/fetch/pull со своего репозитория в GitHub
!!! Синхронизация upstream с origin (только ветка master, остальные не трогать)
!!! Независимые Pull Request на GitHub из нескольких веток одновременно, их редактирование (чтобы надо было переключаться)
