<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# `alias yolo='git push --force'`
---

Chaochih Liu and Paul Hoffman

Applied Bioinformatics Discussion

June 24<sup>th</sup>, 2016

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# What is Git?
---

Version Control System
- Keep track of changes
- Use specific version of code
- Free software

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Git Vs. MS Word
---

MS Word Track Changes         | Git Track Changes
:---------------------------: | :---------------------------:
![](https://raw.githubusercontent.com/MorrellLAB/Applied-Bioinformatics-Discussion/master/Chapter5-Git/images/ms_word_track_changes.png) | ![](https://raw.githubusercontent.com/MorrellLAB/Applied-Bioinformatics-Discussion/master/Chapter5-Git/images/Git_Track_Changes.png)

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Git Basics
---

To create a new repository

```
git init [directory]
```

Check Git's status of files in repository.

```
git status
```

See commit history.

```
git log --graph
```

<!-- Have to be in a Git repository for these commands to work -->

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Git Basics
---

To move and rename files:

```
git mv fileName1 fileName2
git mv filepath1/fileName1 filepath3/fileName1
```
<!-- elaborate on why we would use git mv instead of mv -->

To remove files:

```
git rm filename
```

For more git commands, refer to [Git Cheat Sheet](https://services.github.com/kit/downloads/github-git-cheat-sheet.pdf)

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Git Basics
---

Add files to be tracked by Git

```
git add
```

Commit a file and it's changes to Git

```
git commit
```

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# [`.gitignore`](https://www.gitignore.io/)

Special file that tells Git to not track certain files
- Data files
- Temporary files
- Byte/compiled code

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Git Remotes

<!--# GitHub SSH keys-->

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Git Remotes
---

Git Remotes allow for a backup of your repository on some other devices
- Can be hosted service like [BitBucket](https://bitbucket.org/) or [GitHub](https://github.com/)
- Can be on private server

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Git Remotes
---

Obtain a repository from an existing URL

```
git clone [url]
```

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Git Remotes
---

**Synchronize Changes**
- Downloads history and updates changes
- You must be in the repository before you run this command

```
git pull
```

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Git Remotes
---

- Uploads all local changes (use all three commands in order)
- You add the change, commit the change, and push the change

```
git add
git commit -m "commit message"
git push
```

<!-- Advice on commit messages!!! -->

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Git Remotes
---

Common examples of Git Remotes are [GitHub](https://github.com) and [BitBucket](https://bitbucket.com)

![](https://raw.githubusercontent.com/MorrellLAB/Applied-Bioinformatics-Discussion/master/Chapter5-Git/images/github.png)

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Authenticating Git Remotes
---

Two methods
 - SSH
 - HTTPS

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# VINCE BUFFALO IS WRONG

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Git Remotes
---

It is recommended to use *HTTPS* over *SSH* when working with Git, especially GitHub

- HTTPS is simpler to set up than SSH
- Git's `credential.helper` only works with HTTPS, not SSH
- HTTPS is an open port on all networks, SSH may be blocked
- HTTPS has the same, or better, level of security as SSH
 - Users unfamiliar with SSH best practices will find SSH less secure due to improper management of private keys

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Intro to GitHub
---

Collaboration
- Review changes
- Comment on code
- Report issues

Sharing of code
- Get feedback

User friendliness
- Web-based graphical interface
- READMEs and Wiki pages

An account is not necessary to view and download public repositories.

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Collaborating with GitHub

<!-- Show them GitHub's Issues/Graphs/Collaborators & teams -->

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Working with Your Collaborators
---

Caution!

Always pull before you start editing a file!!

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# What (NOT) to Use GitHub For?

<!-- GitHub upload size limit -->

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Using GitHub
---

GitHub is used to store code and documentation

GitHub can also be used for writing in [Markdown](https://help.github.com/articles/basic-writing-and-formatting-syntax/)/LaTeX

Website hosting through [GitHub Pages](https://pages.github.com/) is an acceptable use of GitHub

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# Abusing GitHub
---

GitHub is **not** used for data storage
 - Example datasets are acceptable

GitHub is **not** used for compiled machine code or interpreted byte code
 - Python `.pyc` files should **not** be uploaded

GitHub is **not** used for non-human readable files
 - Binary files should **not** be uploaded

<sub>See [Bryan J et al. (2016) Good enough practices for scientific computing.](http://swcarpentry.github.io/good-enough-practices-in-scientific-computing/)</sub>

***

<!-- background: #000100 -->
<!-- color: #f1f1f2 -->
<!-- font: metronova -->

# *Possibly* Abusing GitHub
---

Figure sharing on GitHub should only be done if the figure is being used elsewhere on GitHub
- Wiki pages/[READMEs](https://github.com/MorrellLAB/Applied-Bioinformatics-Discussion/tree/master/Chapter5-Git)
- GitHub Pages
- Writings hosted on GitHub
 - Example: [ANGSD-wrapper manuscript](https://github.com/arundurvasula/aw-mer)

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Working with Past Commits

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Undo and Edit Commits
---

```
git commit --amend
git reset --hard
git checkout --force
```

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Git Branches, Forks, and Pull Requests
---

![](http://i.stack.imgur.com/F00b8.png)

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Merge Errors
## <sub>Chaochih's Favorite!</sub>

***

<!-- background: #000100 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# More Advanced Git Topics
---

Submodules

Searching revisions with `git grep`

Rebasing `git rebase`

***

<!-- Exercises color scheme -->
<!-- background: #063852 -->
<!-- color: #F1F1F2-->
<!-- font: metronova -->

# Exercise: Test the waters!
---

Get into groups of 3-5. Make sure **at least 1** person has a computer with Git installed on it.

If you need a reference for Git commands, take a look at [GitHub's cheat sheet](https://services.github.com/kit/downloads/github-git-cheat-sheet.pdf).