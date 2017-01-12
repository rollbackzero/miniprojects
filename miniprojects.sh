WHOAMI=`whoami`

SRCREPO=https://github.com/rollbackzero/miniprojects.git

# check we're running the correct version of the code
LOCAL=`git status -s`
HEAD=`git rev-parse HEAD`
REMOTE=`git ls-remote --heads $SRCREPO | cut -f1`

if [ "$HEAD" != "$REMOTE" ] ; then
    echo "* This code doesn't match the GIT server copy, aborting!"
    echo "* Run 'git pull' to update to the current version"
    exit 1
fi

# if [ -n "$LOCAL" ] ; then
#    echo "* This code has uncommited changes, aborting!"
#    exit 1
# fi

# get a copy of the config
# echo "* Fetching the most recent config from the git server"
# echo "* You may be prompted for a username/password, use the same one you use to access the wiki"
# git clone --quite https://github.com/rollbackzero/miniprojects.git 
# cd miniprojects


# save the changes back to the git server
    echo "* Pushing new config to the git server"
    echo "* You may be prompted for a username/password, use the same one you use to access the wiki"
    git add .
    git commit -a -m "automatic update invoked by $WHOAMI"
    git push
    sleep 5

# git init
# git add .
# git commit -m "commiting"
# git remote -v
# git remote remove origin
#  git remote add origin https://github.com/rollbackzero/miniprojects.git
# git remote add origin git@github.com:rollbackzero/miniprojects.git
# git push -u origin master
