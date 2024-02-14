#-- t
#-- u

## for sql
run_sql() {
    cat $1 | mysql -hlocalhost -uroot -pwriteyourpasswordhere hbtn_0d_tvshows
}

alias rs='run_sql'