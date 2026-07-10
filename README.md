# Git Branching Strategies and Team Workflow Simulation

## Overview

Builds a Git repository following the GitFlow branching model, simulating a team environment with features, pull requests, merge conflicts, branch protection rules, and release tagging. The project demonstrates how to safely manage production-ready code (`main`), integrate features (`develop`), handle emergency fixes (`hotfix`), and enforce team discipline via GitHub branch protection rules.

## Architecture

```
main (Production)  <--- release/v0.1.0 (Release) <--- develop (Integration) <--- feature/* (Features)
      ^                                                           ^
      |                                                           |
      +--- hotfix/v0.1.1 (Emergency)                              +--- feature/add-config-file (Concurrent work)
```

- **`main`:** Production-ready code only. Protected by branch rules.
- **`develop`:** Integration branch where all features are merged before release. Protected by branch rules.
- **`feature/*`:** Individual feature branches (e.g., `add-goodbye-message`, `add-config-file`).
- **`release/*`:** Branch used to prepare a release (e.g., `release/0.1.0`).
- **`hotfix/*`:** Emergency branch for fixing production bugs immediately.

## Tech Stack

- Git, GitHub, VS Code, Git Bash / PowerShell

## How to Access

```bash
# 1. Clone / Initialize and push to GitHub
git init
git remote add origin https://github.com/<USER>/gitflow-demo.git
git push -u origin main
git checkout -b develop && git push -u origin develop

# 2. Create Feature A (add-goodbye-message)
git checkout develop && git checkout -b feature/add-goodbye-message
# Edit app.py and tests/test_app.py
git add . && git commit -m "feat: enhance greet and farewell messages"
git push -u origin feature/add-goodbye-message
# Open PR on GitHub: feature/add-goodbye-message -> develop and merge it.

# 3. Create Feature B (add-config-file)
git checkout develop && git checkout -b feature/add-config-file
# Create config.py and modify app.py
git add . && git commit -m "feat: add config module and update greet function"
git push -u origin feature/add-config-file
# Open PR on GitHub -> Merge conflict detected. Resolve locally.
git checkout feature/add-config-file
git merge develop  # Conflict occurs in app.py
# Edit app.py to fix the conflict
git add app.py && git commit -m "merge: resolve conflict in greet()"
git push origin feature/add-config-file
# Click "Merge pull request" on GitHub.

# 4. Release Workflow
git checkout develop && git checkout -b release/0.1.0
# Add CHANGELOG.md
git add . && git commit -m "chore: prepare release 0.1.0"
git push -u origin release/0.1.0
# Open PR: release/0.1.0 -> main. Merge it.
git tag -a v0.1.0 -m "Release version 0.1.0"
git push origin v0.1.0

# 5. Hotfix Workflow
git checkout main && git checkout -b hotfix/fix-greet-typo
# Fix app.py
git add . && git commit -m "fix: add input validation to greet/farewell"
git push -u origin hotfix/fix-greet-typo
# Open PR: hotfix -> main. Merge it.
git checkout develop && git merge main
git push origin develop
git tag -a v0.1.1 -m "Hotfix: add input validation"
git push origin v0.1.1
```

## Problems Faced & Fixes

**Issue:**
<br/>Opened the PR for Feature B (`add-config-file`) against `develop`, but Git reported `Already up to date` when running `git merge develop` locally, even though GitHub clearly showed a merge conflict.

**Investigation:** 
<br/>Feature A (`add-goodbye-message`) was merged into `develop` on GitHub. However, the local `develop` branch was not updated to reflect this remote change. So when `git merge develop` was run from the feature branch, Git compared it to the stale local `develop` (which didn't have Feature A's code yet), saw no difference, and reported "Already up to date".

**Root cause:** 
<br/>Forgot to run `git checkout develop` and `git pull origin develop` before creating the feature branch or before running the merge command.

**Fix:** 
<br/>Explicitly fetched the latest changes and pulled `develop` to update the local branch:
```bash
git fetch origin
git checkout develop
git pull origin develop
git checkout feature/add-config-file
git merge develop  # Conflict appears as expected
```

## Screenshots

### Git installation and global configuration
![Git Version](./screenshots/verified_git.png)
![Git Config List](./screenshots/git_config_list.png)
![Git Config All](./screenshots/git_config_all.png)
![Gitconfig File](./screenshots/gitconfig_file.png)

### Repository initialization and remote setup
![Git Init](./screenshots/git_init.png)
![Git Add and Commit](./screenshots/git_add_commit.png)
![Git Remote Add and Push](./screenshots/git_remote_add_push.png)
![Git Checkout Develop](./screenshots/git_checkout_branch_develop_and_push.png)

### Branch protection rules
![Protection Rule Main](./screenshots/branch_protection_rule_main.png)
![Protection Rule Develop](./screenshots/branch_protection_rule_develop.png)
![Protection Rule General](./screenshots/branch_protection_rule.png)

### Feature A workflow
![New Branch Feature A](./screenshots/add_new_branch_featureA_make_changes_add_commit_push.png)
![Pull Request Feature A](./screenshots/pull_requests_featureA.png)
![PR Feature A Blocked](./screenshots/pull_requests_featureA_merge_blocked_byrules.png)
![PR Feature A Unblocked](./screenshots/pull_requests_featureA_merge_no_longer_blocked.png)
![PR Feature A Merged](./screenshots/pull_requests_featureA_success_merged_closed.png)

### Feature B workflow and conflict resolution
![New Branch Feature B](./screenshots/add_new_branch_featureB_make_changes_addnew_configpy_add_commit_push.png)
![PR Feature B Conflict](./screenshots/pull_requests_featureB_has_conflict.png)
![Conflict in Local Editor](./screenshots/conflict_in_local_editor.png)
![Try Merge and Solve Conflict](./screenshots/try_merge_and_solve_conflict_locally.png)
![Modifying Code to Resolve Conflict](./screenshots/modifying_code_to_resolve_conflict.png)
![Git Add Commit Resolved Conflict](./screenshots/git_add_commit_resolved_conflict.png)
![PR Feature B Merged](./screenshots/pull_requests_featureB_successful_merged_closed.png)

### Release workflow
![New Branch Release](./screenshots/add_new_branch_release.png)
![PR Release Branch](./screenshots/pull_requests_releaseBranch.png)
![PR Release Merged](./screenshots/pull_requests_releaseBranch_successful_merged_closed.png)
![Merge Release with Develop via CLI](./screenshots/next_merge_releaseBranch_with_develop_but_using_cli.png)

### Tagging and GitHub Release
![Git Tag](./screenshots/git_tag.png)
![GitHub Release from Tag](./screenshots/github_created_releases_from_tag.png)

### Hotfix workflow
![PR Hotfix to Main](./screenshots/pull_requests_hotfix_to_main.png)
![Git Merge Main to Develop](./screenshots/git_merge_main_to_develop.png)

## Notes & Interesting Details

- **Why the `diff3` conflict style?** 
Setting `merge.conflictstyle diff3` shows the original code alongside your version and the incoming version during a conflict. This is significantly easier to resolve because you can see what the code looked like before either side modified it.

- **Why merge `main` into `develop` after a hotfix?** 
A hotfix directly patches production (`main`). If this commit is not merged back into `develop`, it will be lost in the next feature release. Merging `main` into `develop` ensures the bug fix is permanently part of the integration branch.

- **Why use Branch Protection Rules?** 
They enforce discipline in a team setting, preventing direct pushes to critical branches (`main`, `develop`). This forces all changes to go through Pull Requests, enabling code reviews, automated tests, and a clear audit trail of who merged what and when.

- **Why are tags immutable?** 
Unlike branches, tags are meant to be permanent markers for specific releases (e.g., `v0.1.0`). They should never be updated or force-pushed once created, as they represent a fixed point in history that other developers and CI/CD pipelines rely on.
