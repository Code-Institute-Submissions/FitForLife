echo "Commit work in progress changes"
if [ -z $1 ]
then
    COMMENT="Work in progress" 
else
    COMMENT="$1"
fi 
git add  .
git commit -m "$COMMENT"
git push origin master
