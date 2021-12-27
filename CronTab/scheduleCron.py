from crontab import CronTab

my_cron = CronTab(user=True)
job = my_cron.new(command='python /Users/admin/Desktop/Java/Hoc/SpringMVC/CollaborativeFiltering/DB/ResetDB.py', comment='resetDB')
job.minute.every(1)

my_cron.write()

