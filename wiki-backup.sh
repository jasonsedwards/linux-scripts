#!/usr/bin/expect
set fp [open "/root/wiki_password" r]
set pass_wd [read $fp]
spawn rsync -av jason.edwards@wiki.stuart-edwards.info:/usr/share/nginx/html/dokuwiki/ /tmp
expect "password:"
send "$pass_wd\n"
expect eof
if [catch wait] {
    puts "rsync failed"
    exit 1
}
exit 0
