echo "Database Backup started"
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
BACKUP_NAME="db-backup_coderr__`date "+%F__%H:%M"`.db"
cp $SCRIPT_DIR/../db.db $BACKUP_NAME
echo "Uploading file:  $BACKUP_NAME"

echo "
 verbose
 open w0205e9f.kasserver.com
 user f017e7de C8SFgmYsmSRKR8K9G36P
 bin
 put $BACKUP_NAME
 bye
" | ftp -n > ftp_$$.log
echo "Backup successful"

rm $BACKUP_NAME
rm ftp_$$.log